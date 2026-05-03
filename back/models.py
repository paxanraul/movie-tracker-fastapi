from pydantic import BaseModel, Field
from sqlalchemy.orm import Mapped, mapped_column

from db import Base

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column()

class MovieCreate(BaseModel):
    title: str = Field(..., example="Batman")
    year: int = Field(..., example=2008)


class MovieUpdate(BaseModel):
    title: str | None = Field(None, example="Batman")
    year: int | None = Field(None, example=2008)
