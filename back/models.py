from sqlalchemy.orm import Mapped, mapped_column

from db import Base

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column()
    hashed_password: Mapped[str] = mapped_column(nullable=False)

