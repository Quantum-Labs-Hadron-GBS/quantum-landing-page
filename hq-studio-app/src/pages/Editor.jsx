import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { supabase } from '../lib/supabase'
import { useEditor, EditorContent } from '@tiptap/react'
import StarterKit from '@tiptap/starter-kit'
import { Markdown } from 'tiptap-markdown'
import { ArrowLeft, Save, Globe } from 'lucide-react'

export default function Editor() {
  const { id } = useParams()
  const navigate = useNavigate()
  
  const [docId, setDocId] = useState(id === 'new' ? null : id)
  const [title, setTitle] = useState('')
  const [slug, setSlug] = useState('')
  const [typeId, setTypeId] = useState('BLOG')
  const [statusId, setStatusId] = useState(1) // 1: Draft, 3: Published
  const [saving, setSaving] = useState(false)
  const [lastSaved, setLastSaved] = useState(null)
  
  const editor = useEditor({
    extensions: [StarterKit, Markdown],
    content: '',
    editorProps: {
      attributes: {
        class: 'prose prose-invert prose-sm sm:prose lg:prose-lg xl:prose-2xl mx-auto focus:outline-none min-h-[500px] text-white p-4 border border-white/10 rounded-lg bg-[#111111]',
      },
    },
  })

  useEffect(() => {
    if (docId && docId !== 'new') {
      loadDocument(docId)
    }
  }, [docId])

  const loadDocument = async (documentId) => {
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
      if (editor) {
        editor.commands.setContent(data.markdown)
      }
    }
  }

  const generateSlug = (text) => {
    return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)+/g, '')
  }

  const handleTitleChange = (e) => {
    setTitle(e.target.value)
    if (!docId) {
      setSlug(generateSlug(e.target.value))
    }
  }

  const handleSave = async (newStatusId = statusId) => {
    setSaving(true)
    const markdown = editor.storage.markdown.getMarkdown()
    const html = editor.getHTML()
    
    const docData = {
      title: title || 'Untitled',
      slug: slug || generateSlug(title || `doc-${Date.now()}`),
      type_id: typeId,
      status_id: newStatusId,
      markdown,
      html,
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
        window.history.replaceState(null, '', `/studio/editor/${data.id}`)
      } else {
        alert(error?.message || 'Error saving')
      }
    }
    setSaving(false)
  }

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
              className="flex items-center gap-2 px-4 py-2 bg-transparent text-gray-300 text-sm font-medium rounded-lg border border-white/20 hover:bg-white/5 transition-colors"
            >
              <Save size={16} />
              {saving ? 'Saving...' : 'Save Draft'}
            </button>
            <button 
              onClick={() => handleSave(3)}
              disabled={saving}
              className="flex items-center gap-2 px-4 py-2 bg-white text-black text-sm font-medium rounded-lg hover:bg-gray-200 transition-colors"
            >
              <Globe size={16} />
              Publish
            </button>
          </div>
        </header>
        
        <div className="flex-1 overflow-y-auto p-8">
          <div className="max-w-4xl mx-auto">
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
              onChange={(e) => setSlug(e.target.value)}
              className="w-full bg-black border border-white/10 rounded-md px-3 py-2 text-sm focus:outline-none focus:border-white/30 text-gray-300"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Document Type</label>
            <select 
              value={typeId}
              onChange={(e) => setTypeId(e.target.value)}
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
        </div>
      </aside>
    </div>
  )
}
