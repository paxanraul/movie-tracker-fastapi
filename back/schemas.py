from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    title: str = Field(..., example="Batman")
    year: int = Field(..., example=2008)


class MovieUpdate(BaseModel):
    title: str | None = Field(None, example="Batman")
    year: int | None = Field(None, example=2008)