import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'alex.erling@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # tls is encryption mechanism
    smtp.login('username', 'password') # 2FA enabled so wont work
    smtp.send_message(email)
    print("All good boss")
t