import { useEffect, useState } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { supabase } from './lib/supabase'
import Auth from './components/Auth'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Documents from './pages/Documents'
import Editor from './pages/Editor'

export default function App() {
  const [session, setSession] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session)
      setLoading(false)
    })

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session)
    })

    return () => subscription.unsubscribe()
  }, [])

  if (loading) {
    return <div className="h-screen w-screen bg-[#0a0a0a] flex items-center justify-center text-white">Loading HQ Studio...</div>
  }

  if (!session) {
    return <Auth />
  }

  return (
    <BrowserRouter basename="/studio">
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/documents" element={<Documents />} />
        </Route>
        {/* Editor runs outside the sidebar layout for maximum screen space */}
        <Route path="/editor/:id" element={<Editor />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}
