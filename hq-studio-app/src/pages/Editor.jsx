import { useEffect, useState, useRef, useCallback } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { supabase } from '../lib/supabase'
import { useEditor, EditorContent } from '@tiptap/react'
import StarterKit from '@tiptap/starter-kit'
import { Markdown } from 'tiptap-markdown'
import { ArrowLeft, Save, Globe, Check } from 'lucide-react'
import Image from '@tiptap/extension-image'
import { Table } from '@tiptap/extension-table'
import { TableRow } from '@tiptap/extension-table-row'
import { TableCell } from '@tiptap/extension-table-cell'
import { TableHeader } from '@tiptap/extension-table-header'

export default function Editor() {
  const { id } = useParams()
  const navigate = useNavigate()
  
  const [docId, setDocId] = useState(id === 'new' ? null : id)
  const [title, setTitle] = useState('')
  const [slug, setSlug] = useState('')
  const [typeId, setTypeId] = useState('BLOG')
  const [statusId, setStatusId] = useState(1) // 1: Draft, 3: Published
  const [coverImage, setCoverImage] = useState('')
  const [author, setAuthor] = useState('')
  const [seoMetadata, setSeoMetadata] = useState({})
  const [saving, setSaving] = useState(false)
  const [lastSaved, setLastSaved] = useState(null)
  
  // Dirty tracking: after a save/publish, block the Publish button until something changes
  const [isDirty, setIsDirty] = useState(false)
  const isLoadingDoc = useRef(false)
  
  const markDirty = useCallback(() => {
    if (!isLoadingDoc.current) {
      setIsDirty(true)
    }
  }, [])
  
  const editor = useEditor({
    extensions: [
      StarterKit, 
      Markdown, 
      Image,
      Table.configure({ resizable: true }),
      TableRow,
      TableHeader,
      TableCell
    ],
    content: '',
    editorProps: {
      attributes: {
        class: 'prose prose-invert prose-sm sm:prose lg:prose-lg xl:prose-2xl mx-auto focus:outline-none min-h-[500px] text-white p-4 border border-white/10 rounded-lg bg-[#111111]',
      },
    },
    onUpdate: () => {
      markDirty()
    },
  })

  useEffect(() => {
    if (docId && docId !== 'new' && editor) {
      loadDocument(docId)
    }
  }, [docId, editor])

  const loadDocument = async (documentId) => {
    isLoadingDoc.current = true
    const { data, error } = await supabase
      .from('documents')
      .select('*')
      .eq('id', documentId)
      .single()
    
    if (data) {
      setTitle(data.title || '')
      setSlug(data.slug || '')
      setTypeId(data.type_id || 'BLOG')
      setStatusId(data.status_id || 1)
      setCoverImage(data.cover_image || '')
      setSeoMetadata(data.seo_metadata || {})
      setAuthor(data.seo_metadata?.author || '')
      if (editor) {
        editor.commands.setContent(data.markdown)
      }
    }
    // Allow a tick for all state to settle before enabling dirty tracking
    setTimeout(() => {
      isLoadingDoc.current = false
      setIsDirty(false)
    }, 100)
  }

  const generateSlug = (text) => {
    return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)+/g, '')
  }

  const handleTitleChange = (e) => {
    setTitle(e.target.value)
    markDirty()
    if (!docId) {
      setSlug(generateSlug(e.target.value))
    }
  }

  const handleSave = async (newStatusId = statusId) => {
    if (newStatusId === 3 && !coverImage.trim()) {
      alert("A Cover Image URL is required to publish this document.");
      return;
    }
    
    setSaving(true)
    const markdown = editor.storage.markdown.getMarkdown()
    const html = editor.getHTML()
    
    const docData = {
      title: title || 'Untitled',
      slug: slug || generateSlug(title || `doc-${Date.now()}`),
      type_id: typeId,
      status_id: newStatusId,
      cover_image: coverImage.trim() || null,
      markdown,
      html,
      seo_metadata: { ...seoMetadata, author: author.trim() },
      updated_at: new Date().toISOString()
    }

    if (newStatusId === 3 && statusId !== 3) {
      docData.published_at = new Date().toISOString()
    }

    if (docId && docId !== 'new') {
      // Update
      const { error } = await supabase.from('documents').update(docData).eq('id', docId)
      if (!error) {
        setLastSaved(new Date())
        setStatusId(newStatusId)
        setIsDirty(false)
      } else {
        alert('Save failed: ' + error.message)
      }
    } else {
      // Insert
      const { data, error } = await supabase.from('documents').insert(docData).select().single()
      if (data) {
        setDocId(data.id)
        setLastSaved(new Date())
        setStatusId(newStatusId)
        setIsDirty(false)
        window.history.replaceState(null, '', `/studio/editor/${data.id}`)
      } else {
        alert(error?.message || 'Error saving')
      }
    }
    setSaving(false)
  }

  // Publish button should be disabled if already published AND no changes have been made
  const isPublishDisabled = saving || (statusId === 3 && !isDirty)

  return (
    <div className="flex h-[calc(100vh)] overflow-hidden bg-[#0a0a0a]">
      {/* Editor Main */}
      <div className="flex-1 flex flex-col h-full overflow-hidden">
        <header className="h-16 border-b border-white/10 flex items-center justify-between px-6 shrink-0 bg-[#111111]">
          <div className="flex items-center gap-4">
            <button onClick={() => navigate('/documents')} className="text-gray-400 hover:text-white">
              <ArrowLeft size={20} />
            </button>
            <span className="text-sm text-gray-500">
              {lastSaved ? `Last saved at ${lastSaved.toLocaleTimeString()}` : (docId === 'new' ? 'New Document' : 'Editing')}
            </span>
          </div>
          <div className="flex items-center gap-3">
            <button 
              onClick={() => handleSave(1)}
              disabled={saving}
              className="flex items-center gap-2 px-4 py-2 bg-transparent text-gray-300 text-sm font-medium rounded-lg border border-white/20 hover:bg-white/5 transition-colors disabled:opacity-50"
            >
              <Save size={16} />
              {saving ? 'Saving...' : 'Save Draft'}
            </button>
            <button 
              onClick={() => handleSave(3)}
              disabled={isPublishDisabled}
              className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-lg transition-colors ${
                isPublishDisabled
                  ? 'bg-green-500/20 text-green-400 border border-green-500/30 cursor-not-allowed'
                  : 'bg-white text-black hover:bg-gray-200'
              }`}
            >
              {statusId === 3 && !isDirty ? (
                <>
                  <Check size={16} />
                  Published
                </>
              ) : (
                <>
                  <Globe size={16} />
                  {statusId === 3 ? 'Update Live' : 'Publish'}
                </>
              )}
            </button>
          </div>
        </header>
        
        <div className="flex-1 overflow-y-auto p-8">
          <div className="max-w-4xl mx-auto">
            <div className="flex flex-wrap gap-2 mb-4">
              <button 
                onClick={() => {
                  const url = window.prompt('Enter Image URL (e.g. Cloudinary link):');
                  if (url && editor) {
                    editor.chain().focus().setImage({ src: url }).run();
                  }
                }}
                className="px-3 py-1.5 bg-white/5 text-gray-300 text-sm rounded hover:bg-white/10 transition-colors flex items-center gap-2 border border-white/10"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                Insert Image
              </button>
              
              <div className="h-8 w-px bg-white/10 mx-1"></div>
              
              <button 
                onClick={() => editor.chain().focus().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()}
                className="px-3 py-1.5 bg-white/5 text-gray-300 text-sm rounded hover:bg-white/10 transition-colors flex items-center gap-2 border border-white/10"
                title="Insert Table"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>
                Table
              </button>
              <button 
                onClick={() => editor.chain().focus().addColumnAfter().run()}
                className="px-2 py-1.5 bg-white/5 text-gray-300 text-sm rounded hover:bg-white/10 transition-colors border border-white/10"
                title="Add Column"
              >
                +Col
              </button>
              <button 
                onClick={() => editor.chain().focus().addRowAfter().run()}
                className="px-2 py-1.5 bg-white/5 text-gray-300 text-sm rounded hover:bg-white/10 transition-colors border border-white/10"
                title="Add Row"
              >
                +Row
              </button>
              <button 
                onClick={() => editor.chain().focus().deleteColumn().run()}
                className="px-2 py-1.5 bg-white/5 text-red-400 text-sm rounded hover:bg-white/10 transition-colors border border-white/10"
                title="Delete Column"
              >
                -Col
              </button>
              <button 
                onClick={() => editor.chain().focus().deleteRow().run()}
                className="px-2 py-1.5 bg-white/5 text-red-400 text-sm rounded hover:bg-white/10 transition-colors border border-white/10"
                title="Delete Row"
              >
                -Row
              </button>
              <button 
                onClick={() => editor.chain().focus().deleteTable().run()}
                className="px-2 py-1.5 bg-white/5 text-red-500 text-sm rounded hover:bg-white/10 transition-colors border border-white/10"
                title="Delete Table"
              >
                Del Table
              </button>
            </div>
            <input 
              type="text" 
              placeholder="Document Title..."
              className="w-full bg-transparent text-5xl font-bold text-white mb-8 focus:outline-none placeholder-gray-700"
              value={title}
              onChange={handleTitleChange}
            />
            {editor && <EditorContent editor={editor} />}
          </div>
        </div>
      </div>

      {/* Sidebar Settings */}
      <aside className="w-80 bg-[#111111] border-l border-white/10 flex flex-col p-6 shrink-0 overflow-y-auto h-full">
        <h3 className="font-bold mb-6 text-white">Document Settings</h3>
        
        <div className="space-y-6">
          <div>
            <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">URL Slug</label>
            <input 
              type="text"
              value={slug}
              onChange={(e) => { setSlug(e.target.value); markDirty(); }}
              className="w-full bg-black border border-white/10 rounded-md px-3 py-2 text-sm focus:outline-none focus:border-white/30 text-gray-300"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Cover Image URL</label>
            <input 
              type="text"
              placeholder="e.g. Cloudinary link"
              value={coverImage}
              onChange={(e) => { setCoverImage(e.target.value); markDirty(); }}
              className="w-full bg-black border border-white/10 rounded-md px-3 py-2 text-sm focus:outline-none focus:border-white/30 text-gray-300 mb-2"
            />
            {coverImage && (
              <div className="w-full aspect-video rounded-md overflow-hidden border border-white/10">
                <img src={coverImage} alt="Cover Preview" className="w-full h-full object-cover" />
              </div>
            )}
          </div>

          <div>
            <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Author Name</label>
            <input 
              type="text"
              placeholder="e.g. Dr. Jane Doe"
              value={author}
              onChange={(e) => { setAuthor(e.target.value); markDirty(); }}
              className="w-full bg-black border border-white/10 rounded-md px-3 py-2 text-sm focus:outline-none focus:border-white/30 text-gray-300 mb-2"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Document Type</label>
            <select 
              value={typeId}
              onChange={(e) => { setTypeId(e.target.value); markDirty(); }}
              className="w-full bg-black border border-white/10 rounded-md px-3 py-2 text-sm focus:outline-none focus:border-white/30 text-gray-300"
            >
              <option value="BLOG">Blog Post</option>
              <option value="RESEARCH">Research Paper</option>
              <option value="WHITEPAPER">Whitepaper</option>
              <option value="CASE_STUDY">Case Study</option>
              <option value="NEWS">News</option>
            </select>
          </div>

          <div>
            <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Current Status</label>
            <div className="flex items-center gap-2 text-sm px-3 py-2 bg-black border border-white/10 rounded-md text-gray-300">
              <div className={`w-2 h-2 rounded-full ${statusId === 3 ? 'bg-green-500' : 'bg-yellow-500'}`}></div>
              {statusId === 3 ? 'Published' : 'Draft'}
            </div>
          </div>

          {statusId === 3 && (
            <div>
              <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Live URL</label>
              <a 
                href={`/article.html?slug=${slug}`} 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-sm text-orange-400 hover:text-orange-300 underline underline-offset-4 break-all transition-colors"
              >
                /article.html?slug={slug}
              </a>
            </div>
          )}
        </div>
      </aside>
    </div>
  )
}
