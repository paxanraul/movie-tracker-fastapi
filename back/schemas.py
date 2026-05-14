from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    title: str = Field(..., json_schema_extra="Batman")
    year: int = Field(..., json_schema_extra=2008)


class MovieUpdate(BaseModel):
    title: str | None = Field(None, json_schema_extra="Batman")
    year: int | None = Field(None, json_schema_extra=2008)


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"