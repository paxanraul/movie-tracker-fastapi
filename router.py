from fastapi import APIRouter, Depends

from typing import Annotated

router = APIRouter(
    prefix="/movies",
    tags=["Raul movie tracker swag"],
)

