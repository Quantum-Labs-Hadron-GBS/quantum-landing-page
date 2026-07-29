const nodemailer = require('nodemailer');

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const { name, organization, email, service, description } = req.body;

  if (!name || !email) {
    return res.status(400).json({ message: 'Name and Email are required' });
  }

  // Use environment variables for SMTP configuration
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST || 'smtp.gmail.com',
    port: process.env.SMTP_PORT || 465,
    secure: true,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });

  const mailOptions = {
    from: process.env.SMTP_USER || '"Hadron Quantum Contact" <no-reply@hadrongbs.com>',
    to: 'quantum.labs@hadrongbs.com, info@hadrongbs.com',
    subject: `New Contact Request from ${name} (${organization})`,
    text: `
      You have a new contact request from the Hadron Quantum Landing Page:

      Name: ${name}
      Organization: ${organization || 'N/A'}
      Email: ${email}
      Interested Service: ${service || 'N/A'}
      
      Message:
      ${description || 'N/A'}
    `,
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
  };

  try {
    // We only try to send if SMTP_USER is configured to avoid crashes in unconfigured deployments
    if (process.env.SMTP_USER) {
      await transporter.sendMail(mailOptions);
    } else {
      console.warn("SMTP_USER not configured. Simulating email sending for lead:", req.body);
    }
    
    return res.status(200).json({ success: true, message: 'Message sent successfully!' });
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ success: false, message: 'Failed to send message. Please try again later.' });
  }
}
