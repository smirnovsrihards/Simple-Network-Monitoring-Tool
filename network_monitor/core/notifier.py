from core.configer import ConfManager
import smtplib, ssl
from email.message import EmailMessage

class SendMail:
    def __init__(self, host):
        self.host = host
    
    def send(self):
        read = ConfManager
        config_data = read.read_config()
        
        port = config_data['port']
        smtp_server = config_data['smtp_server']
        sender_email = config_data['sender_email']
        receiver_email = config_data['receiver_email']
        app_password = config_data['app_password']
        
        messg = EmailMessage()
        messg.set_content(f"Alert: Host {self.host} is DOWN!!!")
        messg['Subject'] = f"[ALERT] Host Down: {self.host}"
        messg['From'] = sender_email
        messg['To'] = receiver_email
        
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, app_password)
            server.send_message(messg)
