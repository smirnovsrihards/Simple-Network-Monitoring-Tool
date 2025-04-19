import smtplib, ssl
from email.message import EmailMessage

class SendMail:
    def __init__(self, host):
        self.host = host
    
    def send(self):
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "Add your sender mail"
        receiver_email = "Add your receiver mail"
        app_password = 'App password from Google'
        
        messg = EmailMessage()
        messg.set_content(f"Alert: Host {self.host} is DOWN!!!")
        messg['Subject'] = f"[ALERT] Host Down: {self.host}"
        messg['From'] = sender_email
        messg['To'] = receiver_email
        
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, app_password)
            server.send_message(messg)
