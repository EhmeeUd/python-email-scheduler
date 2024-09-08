import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv


load_dotenv()


class EmailSender:
    def __init__(self, smtp_server, smtp_port, login, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.login = login
        self.password = password


    def send_email(self, subject, body, to_addresses):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = ', '.join(to_addresses)
            msg['Subject'] = subject


            msg.attach(MIMEText(body, 'plain'))


            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.login, self.password)
                text = msg.as_string()
                server.sendmail(self.login, to_addresses, text)
            print(f"Email successfully sent to {to_addresses}")
            return True
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False


def send_daily_email(email_sender, to_addresses):
    subject = "A Lover's Note"
    body = "This is your daily email update from chaos test project."
    email_sender.send_email(subject, body, to_addresses)


# Configuration
smtp_server = getenv("SMTP_SERVER", "smtp.example.com")
smtp_port = getenv("SMTP_PORT", "587")
login = getenv("LOGIN", "test@example.com")
password = getenv("PASSWORD", "password")


to_addresses = getenv("TO", "default@example.com").split(',')

print(to_addresses)
email_sender = EmailSender(smtp_server, smtp_port, login, password)


send_daily_email(email_sender, to_addresses)