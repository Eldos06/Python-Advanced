import logging
from email_sender import EmailSender, loggingEmailBackend
from common import configure_logging, BASE_DIR

from my_package.file_email_backend import FileEmailBackend

WelcomeTemplate = """
Dear {name},

Welcome to our website!

Best regards,
The Team.

"""

def send_mails(sender: EmailSender) -> None:
    name = "Bob"
    recipient = "bob@ya.ru"
    subject = "Hello Bob"
    body = "This is a test email"
    sender.send(
        recipient=recipient,
        subject=subject,
        body=body,
    )



    sender.send_with_template(
        recipient=recipient,
        subject=subject,
        template=f'{WelcomeTemplate}',
        name=name,
    )


def main() -> None:
    configure_logging()
    logging.info("Starting the main function.")  # Added log message

    logging_backend = loggingEmailBackend('sender')
    sender = EmailSender(backend = logging_backend)

    send_mails(sender)
    emails_directory =  BASE_DIR / 'emails'
    file_backend = FileEmailBackend(directory=emails_directory)
    send_mails(sender)

if __name__ == "__main__":
    main()


