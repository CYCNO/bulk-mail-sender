import json
from email.message import EmailMessage
from email.mime.text import MIMEText
import ssl
import smtplib


def send_email(sender, password, reciever, subject, message, name):
    em = EmailMessage()

    em['From'] = sender
    em['To'] = reciever
    em['Subject'] = subject

    em.set_content(MIMEText(message, 'html'))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())

    print(f'mail is sended to {name}')


# Load the email data from emails.json
with open('data/recipient_data.json') as file:
    email_data = json.load(file)
    print('All Email Loaded')
    print()

# Read The Credential 
with open('data/credential.json', 'r') as json_file:
    cred= json.load(json_file)    

# Read the content of the text file
with open('data/email_template.txt', 'r') as file:
    file_lines = file.readlines()

# Extract subject and body from file_lines
subject = ''
body_data = ''
for line in file_lines:
    if line.strip().startswith("Subject:"):
        subject = line.strip().replace('Subject:', '').strip()
    else:
        body_data += line.strip() + '<br>'

# Iterate over each email in the data
for email in email_data['emails']:
    recipient_email = email['email']
    name = email['name']

    # Set the modified body of the email
    body = body_data.replace("{name}", str(name))
    # Call the function to send the email
    send_email(cred['email'], cred['appPassword'],
               recipient_email, subject, body, name)
    print()
print('All Mail Sended Successfully')
