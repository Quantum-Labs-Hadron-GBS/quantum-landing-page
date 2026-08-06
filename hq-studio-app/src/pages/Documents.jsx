import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { FileText, Plus, Edit2 } from 'lucide-react'
import { supabase } from '../lib/supabase'
import { format } from 'date-fns'

export default function Documents() {
  const [documents, setDocuments] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchDocs()
  }, [])

  const fetchDocs = async () => {
    const { data, error } = await supabase
      .from('documents')
      .select('id, title, type_id, status_id, updated_at')
      .order('updated_at', { ascending: false })
    
    if (data) setDocuments(data)
    setLoading(false)
  }

  const getStatusBadge = (id) => {
    switch(id) {
      case 1: return <span className="px-2 py-1 bg-gray-500/20 text-gray-300 text-xs rounded-md border border-gray-500/30">Draft</span>
      case 2: return <span className="px-2 py-1 bg-yellow-500/20 text-yellow-300 text-xs rounded-md border border-yellow-500/30">Review</span>
      case 3: return <span className="px-2 py-1 bg-green-500/20 text-green-300 text-xs rounded-md border border-green-500/30">Published</span>
      default: return null
    }
  }

  return (
    <div className="p-8 max-w-6xl mx-auto">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold mb-2">Documents</h1>
          <p className="text-gray-400">Manage your published content and drafts.</p>
        </div>
        <Link to="/editor/new" className="flex items-center gap-2 px-4 py-2 bg-white text-black text-sm font-medium rounded-lg hover:bg-gray-200 transition-colors">
          <Plus size={18} />
          New Document
        </Link>
      </div>

      <div className="bg-[#111111] border border-white/10 rounded-xl overflow-hidden">
        {loading ? (
          <div className="p-8 text-center text-gray-500">Loading documents...</div>
        ) : documents.length === 0 ? (
          <div className="p-8 text-center text-gray-500">No documents yet. Create one!</div>
        ) : (
          <table className="w-full text-left text-sm">
            <thead className="bg-white/5 border-b border-white/10">
              <tr>
                <th className="px-6 py-4 font-medium text-gray-300">Title</th>
                <th className="px-6 py-4 font-medium text-gray-300">Type</th>
                <th className="px-6 py-4 font-medium text-gray-300">Status</th>
                <th className="px-6 py-4 font-medium text-gray-300">Last Modified</th>
                <th className="px-6 py-4 font-medium text-gray-300 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/10">
              {documents.map((doc) => (
                <tr key={doc.id} className="hover:bg-white/5 transition-colors">
                  <td className="px-6 py-4 font-medium flex items-center gap-3">
                    <FileText size={16} className="text-gray-400" />
                    {doc.title || 'Untitled Document'}
                  </td>
                  <td className="px-6 py-4 text-gray-400">{doc.type_id}</td>
                  <td className="px-6 py-4">{getStatusBadge(doc.status_id)}</td>
                  <td className="px-6 py-4 text-gray-400">
                    {format(new Date(doc.updated_at), 'MMM d, yyyy HH:mm')}
                  </td>
                  <td className="px-6 py-4 text-right">
                    <Link to={`/editor/${doc.id}`} className="inline-flex items-center gap-1 text-gray-400 hover:text-white transition-colors">
                      <Edit2 size={16} /> Edit
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}
