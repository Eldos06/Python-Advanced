
import config
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column




# 2. Base and models
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str]
    motto: Mapped[str | None]


def main() -> None:
    engine = create_engine(
        url=config.DB_URL,
        echo=config.DB_ECHO,
    )
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
