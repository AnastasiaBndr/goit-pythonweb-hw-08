from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from src.configuration import get_db

app = FastAPI()


@app.get("/api/contacts")
def healthcheker(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database is not configured correctly",
                                )
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error connecting to db")

@app.post("/api/contact/create")
def create_contact():
    ...

@app.post("/api/contact/delete/{id}")
def delete_contact():
    ...


@app.patch("/api/contact/update/{id}")
def update_contact():
    ...

@app.get("/api/contact/get/{id}")
def create_contact():
    ...



