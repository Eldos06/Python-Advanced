from datetime import datetime
from random import randint
from pathlib import Path
import random
from base_email_backend import BaseEmailBackend

class FileEmailBackend(BaseEmailBackend):
  def __init__(
    self,
    directory: Path,
         ) -> None:
    self.directory = directory
    self.directory.mkdir(parents=True, exist_ok=True)

  @classmethod
  def get_filename(
    cls,
    recipient: str,
    subject: str,
    ) -> str:
        ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        rnd = random.randint(1_000_000, 9_999_999)
        rec = recipient.replace('@', '_at_')
        subj = subject.replace(' ', '_')
        return f"{ts}.{rnd}._{rec}_{subj}.txt"


  def send(
    self,
    recipient: str,
    subject: str,
    body: str
  ) -> None:
    filename = ''
    filepath = self.directory / filename

    with filepath.open('w') as f:
      f.write(f"To: {recipient}\n")
      f.write(f"Subject: {subject}\n")
      f.write(f"Body: {body}\n")