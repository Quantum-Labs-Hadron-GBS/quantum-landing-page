import { createClient } from '@supabase/supabase-js'
import dotenv from 'dotenv'

dotenv.config()

const supabase = createClient(
  process.env.VITE_SUPABASE_URL,
  process.env.VITE_SUPABASE_ANON_KEY
)

const users = [
  { email: 'quantum.lab@hadrongbs.com', password: 'QLab@2026' },
  { email: 'info@hadrongbs.com', password: 'MktgHGBS@2026' },
  { email: 'saurav@hadrongbs.com', password: 'Saurav@HGBS123' }
]

async function seedUsers() {
  console.log('Registering users with Supabase Auth...')
  
  for (const user of users) {
    const { data, error } = await supabase.auth.signUp({
      email: user.email,
      password: user.password,
    })

    if (error) {
      console.error(`Failed to register ${user.email}:`, error.message)
    } else {
      console.log(`Successfully registered ${user.email}.`)
    }
  }
  console.log('\nNOTE: If email confirmations are enabled in your Supabase project (default), these users will receive an email to verify their accounts before they can log in.')
}

seedUsers()
