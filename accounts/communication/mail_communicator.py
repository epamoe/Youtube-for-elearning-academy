
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
   
class MailCommunicator: 
    
        
    port = 465
    smtp_server_domain_name = "smtp.gmail.com"
    sender_mail = "ytbdev10@gmail.com"
    password = "Ycono19@2222"
    
    
    @classmethod
    def send_activation_mail(self, recipient: str, subject: str, templates: dict) -> None:
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        mail = MIMEMultipart('alternative')
        mail['Subject'] = subject
        mail['From'] = self.sender_mail
        mail['To'] = recipient
        
        html_content = MIMEText(templates["html_template"], 'html')
        text_content = MIMEText(templates["text_template"], 'plain')
        
        mail.attach(text_content)
        mail.attach(html_content)
        
        service.sendmail(self.sender_mail, recipient, mail.as_string())
        print(mail.as_string())

        service.quit()

