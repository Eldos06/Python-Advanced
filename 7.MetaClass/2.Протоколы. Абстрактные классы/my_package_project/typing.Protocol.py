import logging
from email_sender import EmailSender, loggingEmailBackend
from common import configure_logging

WelcomeTemplate = """
Dear {name},

Welcome to our website!

Best regards,
The Team.

"""

def main() -> None:
    configure_logging()
    logging.info("Starting the main function.")  # Added log message

    logging_backend = loggingEmailBackend('sender')
    sender = EmailSender(backend = logging_backend)
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

if __name__ == "__main__":
    main()

