from fastapi import FastAPI, Depends, HTTPException, status, Query, Path, Request
from sqlalchemy.orm import Session
from src.configuration import get_db
from src.models.contacts import Contact
from fastapi.responses import JSONResponse
from .pydantic_models import ContactModel, ResponseContactModel, ErrorResponse

app = FastAPI()


@app.exception_handler(HTTPException)
def handle_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content={"message": str(exc.detail)}
    )


@app.get("/api/contacts", response_model=ResponseContactModel)
async def get_contacts_list(
    skip: int = 0,
    limit: int = Query(default=10, le=100, ge=10),
    db: Session = Depends(get_db),
):
    try:
        contacts = db.query(Contact).offset(skip).limit(limit).all()
        if contacts is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database is not configured correctly",
            )
        return contacts
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error connecting to db",
        )


@app.post(
    "/api/contact/create",
    response_model=ResponseContactModel,
    responses={400: {"model": ErrorResponse}},
)
async def create_contact(contact: ContactModel, db: Session = Depends(get_db)):

    new_contact = Contact(
        first_name=contact.first_name,
        second_name=contact.second_name,
        email=contact.email,
        birthday=contact.birthday,
        phone_number=contact.phone_number,
        additional_data=contact.additional_data,
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


@app.post("/api/contact/delete/{ontact_id}", response_model=ResponseContactModel)
def delete_contact(): ...


@app.patch("/api/contact/update/{contact_id}", response_model=ResponseContactModel)
def update_contact(): ...


@app.get("/api/contact/get/{contact_id}", response_model=ResponseContactModel)
async def get_contact_by_id(
    contact_id: int = Path(description="The ID of the contact to get", gt=0, le=10),
    db: Session = Depends(get_db),
):
    print(contact_id)
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return contact
