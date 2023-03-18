import smtplib
import ssl
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv()

email_sender = os.environ.get('gmailUser')
email_password = os.environ.get('gmailPass')
email_receiver = "email@gmail.com"

subject = "Testing!"
body = """
    Hello World :)
"""
pdf = "pdf.pdf"

def send_email(to, subject, body, pdf):
    """
    Sends an email

    Parameters:
    to (str): email receiver
    subject (str): email subject
    body (str): email body
    pdf (str): email attachment
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = to
    em['Subject'] = subject
    em.set_content(body)
    with open(pdf, 'rb') as content_file:
        content = content_file.read()
        em.add_attachment(content, maintype='application', subtype='pdf', filename=pdf)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print(f"Email sent to: {to}")
    
    return

send_email(email_receiver, subject, body, pdf)