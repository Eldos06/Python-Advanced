__all__ = (
    "BASE_DIR",
)

from pathlib import Path


BASE_DIR = Path(__file__).parent

SQLite_DB_PATH = BASE_DIR / "db.sqlite3"

DB_URL = f"sqlite:///{BASE_DIR}/db.sqlite3"

DB_ECHO = True





