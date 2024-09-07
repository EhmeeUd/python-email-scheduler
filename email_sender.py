import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

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
smtp_server = 'smtp.gmail.com'
smtp_port = 587
login = 'mhizxeryl@gmail.com'
password = 'btlr uiqh urzd yneh'

to_addresses = ['verychaoticpodcast@gmail.com', 'iniememudosen@gmail.com']
email_sender = EmailSender(smtp_server, smtp_port, login, password)

# Schedule daily email at 16:40 AM
schedule.every().day.at("16:40").do(send_daily_email, email_sender, to_addresses)

# Keep the script running to trigger the daily task
while True:
    schedule.run_pending()
    time.sleep(60)
