import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { FileText, Clock, CheckCircle, Plus, TrendingUp } from 'lucide-react'
import { supabase } from '../lib/supabase'
import { format } from 'date-fns'

export default function Dashboard() {
  const [stats, setStats] = useState({ total: 0, drafts: 0, published: 0 })
  const [recentDocs, setRecentDocs] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchDashboardData()
  }, [])

  const fetchDashboardData = async () => {
    try {
      const { data, error } = await supabase
        .from('documents')
        .select('id, title, slug, type_id, status_id, updated_at, published_at')
        .order('updated_at', { ascending: false })

      if (data) {
        const total = data.length
        const drafts = data.filter(d => d.status_id !== 3).length
        const published = data.filter(d => d.status_id === 3).length
        setStats({ total, drafts, published })
        setRecentDocs(data.slice(0, 5))
      }
    } catch (err) {
      console.error('Dashboard fetch error:', err)
    }
    setLoading(false)
  }

  const getStatusBadge = (id) => {
    switch(id) {
      case 1: return <span className="px-2 py-1 bg-gray-500/20 text-gray-300 text-xs rounded-md border border-gray-500/30">Draft</span>
      case 2: return <span className="px-2 py-1 bg-yellow-500/20 text-yellow-300 text-xs rounded-md border border-yellow-500/30">Review</span>
      case 3: return <span className="px-2 py-1 bg-green-500/20 text-green-300 text-xs rounded-md border border-green-500/30">Published</span>
      default: return <span className="px-2 py-1 bg-gray-500/20 text-gray-300 text-xs rounded-md border border-gray-500/30">Draft</span>
    }
  }

  return (
    <div className="p-8 max-w-6xl mx-auto">
      <header className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Overview</h1>
        <p className="text-gray-400">Welcome to Quantum Labs Publisher.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6">
          <div className="flex items-center gap-3 text-gray-400 mb-2">
            <FileText size={18} />
            <h3 className="font-medium">Total Documents</h3>
          </div>
          <p className="text-4xl font-bold">{loading ? '—' : stats.total}</p>
        </div>
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6">
          <div className="flex items-center gap-3 text-blue-400 mb-2">
            <Clock size={18} />
            <h3 className="font-medium">Drafts</h3>
          </div>
          <p className="text-4xl font-bold">{loading ? '—' : stats.drafts}</p>
        </div>
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6">
          <div className="flex items-center gap-3 text-green-400 mb-2">
            <CheckCircle size={18} />
            <h3 className="font-medium">Published</h3>
          </div>
          <p className="text-4xl font-bold">{loading ? '—' : stats.published}</p>
        </div>
      </div>

      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold">Recent Activity</h2>
          <Link 
            to="/editor/new" 
            className="flex items-center gap-2 px-4 py-2 bg-white text-black text-sm font-medium rounded-lg hover:bg-gray-200 transition-colors"
          >
            <Plus size={16} />
            New Document
          </Link>
        </div>
        
        <div className="bg-[#111111] border border-white/10 rounded-xl overflow-hidden">
          {loading ? (
            <div className="p-8 text-center text-gray-500">Loading recent activity...</div>
          ) : recentDocs.length === 0 ? (
            <div className="p-8 text-center text-gray-500">
              No documents yet. Click "+ New Document" to start writing.
            </div>
          ) : (
            <table className="w-full text-left text-sm">
              <thead className="bg-white/5 border-b border-white/10">
                <tr>
                  <th className="px-6 py-4 font-medium text-gray-300">Title</th>
                  <th className="px-6 py-4 font-medium text-gray-300">Type</th>
                  <th className="px-6 py-4 font-medium text-gray-300">Status</th>
                  <th className="px-6 py-4 font-medium text-gray-300">Last Modified</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/10">
                {recentDocs.map((doc) => (
                  <tr key={doc.id} className="hover:bg-white/5 transition-colors">
                    <td className="px-6 py-4 font-medium">
                      <Link to={`/editor/${doc.id}`} className="flex items-center gap-3 hover:text-orange-400 transition-colors">
                        <FileText size={16} className="text-gray-400 shrink-0" />
                        <span className="truncate max-w-xs">{doc.title || 'Untitled Document'}</span>
                      </Link>
                    </td>
                    <td className="px-6 py-4 text-gray-400">{(doc.type_id || 'BLOG').replace(/_/g, ' ')}</td>
                    <td className="px-6 py-4">{getStatusBadge(doc.status_id)}</td>
                    <td className="px-6 py-4 text-gray-400">
                      {format(new Date(doc.updated_at), 'MMM d, yyyy HH:mm')}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  )
}
