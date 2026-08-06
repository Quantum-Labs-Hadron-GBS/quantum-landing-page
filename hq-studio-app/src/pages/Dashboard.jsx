import { FileText, Clock, CheckCircle } from 'lucide-react'

export default function Dashboard() {
  return (
    <div className="p-8 max-w-6xl mx-auto">
      <header className="mb-8">
        <h1 className="text-3xl font-bold mb-2">Overview</h1>
        <p className="text-gray-400">Welcome to Hadron Quantum Publisher.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6">
          <div className="flex items-center gap-3 text-gray-400 mb-2">
            <FileText size={18} />
            <h3 className="font-medium">Total Documents</h3>
          </div>
          <p className="text-4xl font-bold">0</p>
        </div>
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6">
          <div className="flex items-center gap-3 text-blue-400 mb-2">
            <Clock size={18} />
            <h3 className="font-medium">Drafts</h3>
          </div>
          <p className="text-4xl font-bold">0</p>
        </div>
        <div className="bg-[#111111] border border-white/10 rounded-xl p-6">
          <div className="flex items-center gap-3 text-green-400 mb-2">
            <CheckCircle size={18} />
            <h3 className="font-medium">Published</h3>
          </div>
          <p className="text-4xl font-bold">0</p>
        </div>
      </div>

      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold">Recent Activity</h2>
          <button className="px-4 py-2 bg-white text-black text-sm font-medium rounded-lg hover:bg-gray-200 transition-colors">
            + New Document
          </button>
        </div>
        
        <div className="bg-[#111111] border border-white/10 rounded-xl divide-y divide-white/10">
          <div className="p-8 text-center text-gray-500">
            No documents yet. Click "+ New Document" to start writing.
          </div>
        </div>
      </div>
    </div>
  )
}
