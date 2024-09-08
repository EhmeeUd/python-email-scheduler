import unittest
from unittest.mock import patch, MagicMock
from email_sender import EmailSender, send_daily_email  

class TestEmailSender(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        # Set up mock SMTP server
        mock_server_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server_instance

        # Initialize EmailSender
        email_sender = EmailSender("smtp.example.com", 587, "test@example.com", "password")

        # Call the send_email method
        result = email_sender.send_email(
            subject="Test Subject",
            body="Test Body",
            to_addresses=["recipient@example.com"]
        )

        # Assert that the email was sent successfully
        self.assertTrue(result)
        mock_server_instance.sendmail.assert_called_once_with(
            "test@example.com",
            ["recipient@example.com"],
            unittest.mock.ANY  # We use ANY here since the exact message body is not important for the test
        )

    @patch('smtplib.SMTP')
    def test_send_email_failure(self, mock_smtp):
        # Set up mock SMTP server to raise an exception
        mock_server_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server_instance
        mock_server_instance.sendmail.side_effect = Exception("SMTP error")

        # Initialize EmailSender
        email_sender = EmailSender("smtp.example.com", 587, "test@example.com", "password")

        # Call the send_email method
        result = email_sender.send_email(
            subject="Test Subject",
            body="Test Body",
            to_addresses=["recipient@example.com"]
        )

        # Assert that the email sending failed
        self.assertFalse(result)

    @patch('smtplib.SMTP')
    def test_send_daily_email(self, mock_smtp):
        # Set up mock SMTP server
        mock_server_instance = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server_instance

        # Initialize EmailSender
        email_sender = EmailSender("smtp.example.com", 587, "test@example.com", "password")

        # Call the send_daily_email function
        send_daily_email(email_sender, ["recipient@example.com"])

        # Assert that the send_email method was called with the expected parameters
        mock_server_instance.sendmail.assert_called_once_with(
            "test@example.com",
            ["recipient@example.com"],
            unittest.mock.ANY  # We use ANY here since the exact message body is not important for the test
        )


if __name__ == '__main__':
    unittest.main()
