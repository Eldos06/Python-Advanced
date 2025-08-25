
import logging
from typing import Protocol


# my_package/email_backend_protocol.py
class BaseEmailBackend(Protocol):
   def send(
         self,
         recipient: str,
         subject: str,
         body: str
   ) -> None: ...






class loggingEmailBackend(BaseEmailBackend):
  def __init__(self, name: str) -> None:
     self.log = logging.getLogger(name)

  def send(
      self,
      recipient: str,
      subject: str,
      body: str
  ) -> None:
    self.log.info(
    "Sending email to %r with subject %r. and body %r",
    recipient,
    subject,
    body
    )


class EmailSender:
  def __init__(self, backend: BaseEmailBackend) -> None:
     self.backend = backend

  def send(
      self,
      recipient: str,
      subject: str,
      body: str
  ) -> None:
    self.backend.send(
        recipient=recipient,
        subject=subject,
        body=body
    )

  def send_with_template(
      self,
      recipient: str,
      subject: str,
      template: str,
      **params,
      ) -> None:
      body = template.format(**params)
      return self.send(
          recipient=recipient,
          subject=subject,
          body=body
      )


