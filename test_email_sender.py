import unittest
from unittest.mock import patch, MagicMock
from email_sender import EmailSender


class TestEmailSender(unittest.TestCase):


    @patch('smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        # Mock the SMTP object and its methods
        smtp_instance = MagicMock()
        mock_smtp.return_value = smtp_instance


        email_sender = EmailSender('smtp.gmail.com', 587, 'mhizxeryl@gmail.com', 'btlr uiqh urzd yneh')
        to_addresses = ['iniememudosen@gmail.com']
        subject = 'Test Subject'
        body = 'Test Body'


        # Call the send_email method
        result = email_sender.send_email(subject, body, to_addresses)


        # Assertions
        self.assertTrue(result)
        smtp_instance.starttls.assert_called_once()
        smtp_instance.login.assert_called_once_with('mhizxeryl@gmail.com', 'btlr uiqh urzd yneh')
        smtp_instance.sendmail.assert_called_once()


    @patch('smtplib.SMTP')
    def test_send_email_failure(self, mock_smtp):
        # Mock the SMTP object to raise an exception
        smtp_instance = MagicMock()
        smtp_instance.sendmail.side_effect = Exception("SMTP Error")
        mock_smtp.return_value = smtp_instance


        email_sender = EmailSender('smtp.gmail.com', 587, 'mhizxeryl@gmail.com', 'btlr uiqh urzd yneh')
        to_addresses = ['iniememudosen@gmail.com']
        subject = 'Test Subject'
        body = 'Test Body'


        # Call the send_email method
        result = email_sender.send_email(subject, body, to_addresses)


        # Assertions
        self.assertFalse(result)
   
    @patch.object(EmailSender, 'send_email', return_value=True)
    def test_send_daily_email_success(self, mock_send_email):
        email_sender = EmailSender('smtp.gmail.com', 587, 'mhizxeryl@gmail.com', 'btlr uiqh urzd yneh')
        to_addresses = ['iniememudosen@gmail.com']


        # Call the send_daily_email function
        send_daily_email(email_sender, to_addresses)


        # Assert that send_email was called with the correct parameters
        mock_send_email.assert_called_once_with(
            "A Lover's Note",
            "This is your daily email update from chaos test project.",
            to_addresses
        )


if __name__ == '__main__':
    unittest.main()