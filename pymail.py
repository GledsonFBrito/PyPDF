import smtplib
import imghdr
from email.message import EmailMessage

email_pass = ''  # senha que será fornecida pelo gmail
email_id = 'SEUEMAIL@GMAIL.COM'
receiving_email = 'EMAILRECEPTOR@GMAIL.COM'

smtp = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
smtp.login(email_id, email_pass)  # login no e-mail

msg = EmailMessage()

with open('IMAGEM.JPG', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

with open('IMAGEM2.JPG', 'rb') as f:
    file_data1 = f.read()
    file_type2 = imghdr.what(f.name)
    file_name3 = f.name

msg['Subject'] = 'Cabeçalho do email'
msg['From'] = email_id
msg['To'] = receiving_email
msg.set_content('CONTEÚDO DO EMAIL')
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
smtp.send_message(msg)

"""
se você usa o " smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) " 
não será necessário dar "hello" ou "starttls".
caso use smtp = smtplib.SMTP(host='smtp.gmail.com', port=587), 
daí será necessário usar as seguintes linhas:
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
"""