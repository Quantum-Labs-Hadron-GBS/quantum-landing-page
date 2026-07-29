import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const { name, organization, email, service, description } = req.body;

  if (!name || !email) {
    return res.status(400).json({ success: false, message: 'Name and Email are required' });
  }

  if (!process.env.RESEND_API_KEY) {
    console.warn("RESEND_API_KEY not configured. Simulating email sending for lead:", req.body);
    return res.status(200).json({ success: true, message: 'Simulated email send.' });
  }

  try {
    const { data, error } = await resend.emails.send({
      from: 'Hadron Quantum <contact@hadrongbs.com>', // Must be a verified domain in Resend
      to: ['quantum.labs@hadrongbs.com', 'info@hadrongbs.com'],
      subject: `New Contact Request from ${name} (${organization || 'N/A'})`,
      html: `
        <h2>New Contact Request</h2>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Organization:</strong> ${organization || 'N/A'}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Interested Service:</strong> ${service || 'N/A'}</p>
        <br />
        <p><strong>Message:</strong></p>
        <p>${description ? description.replace(/\n/g, '<br />') : 'N/A'}</p>
      `,
    });

    if (error) {
      console.error('Resend Error:', error);
      return res.status(500).json({ success: false, message: 'Failed to send message via Resend.', error });
    }

    return res.status(200).json({ success: true, message: 'Message sent successfully!', data });
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ success: false, message: 'Internal Server Error while sending message.' });
  }
}
