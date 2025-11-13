from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException, status
from datetime import date


class ErrorResponse(BaseModel):
    message: str


class ContactModel(BaseModel):
    first_name: str
    second_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str | None = None

    @model_validator(mode="before")
    def validate_items(cls, values):
        first_name = values.get("name")

        if not first_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Name is required."
            )

        return values


class ResponseContactModel(BaseModel):
    id: int = Field(default=1, ge=1)
    first_name: str
    second_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str | None = None
