# from email_sender import BaseEmailBackend
from typing import Protocol
import logging

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
