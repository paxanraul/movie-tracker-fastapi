from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    title: str = Field(..., json_schema_extra="Batman")
    year: int = Field(..., json_schema_extra=2008)


class MovieUpdate(BaseModel):
    title: str | None = Field(None, json_schema_extra="Batman")
    year: int | None = Field(None, json_schema_extra=2008)