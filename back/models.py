from sqlalchemy.orm import Mapped, mapped_column

from db import Base

# Создает таблицу с фильмами
class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column()