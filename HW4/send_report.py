import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import load_config

data = load_config.load_config()

from_email = data['from_email']
to_email = data['to_email']
pass_email = data['email_password']
filename = 'tests_log.txt'
subject = f"report {filename}"
message_body = 'Here is the text with test report'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.attach(MIMEText(message_body, _subtype='plain'))

with open(filename, 'rb') as f:
    attach = MIMEBase('application', 'octet-stream')
    attach.set_payload(f.read())
    encoders.encode_base64(attach)
    attach.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(attach)

smtp_server = 'smtp.mail.ru'
smtp_port = 587

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(from_email, pass_email)

    server.sendmail(from_email, to_email, msg.as_string())

    print('The message was sent')
except Exception as e:
    print(f'Error {str(e)}')

finally:
    server.quit()
