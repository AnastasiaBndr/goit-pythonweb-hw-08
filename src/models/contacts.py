from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, relationship, mapped_column
from datetime import date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    second_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False)

    phone_number: Mapped[str] = mapped_column(
        String(13), unique=True, nullable=False)
    birthday: Mapped[date] = mapped_column(Date)
    additional_data: Mapped[str] = mapped_column(String(200), nullable=True)

    def __str__(self):
        return (
            f"Contact: ({self.id}, {self.first_name} "
            f"{self.second_name} {self.email} "
            f"{self.phone_number} {self.birthday} {self.additional_data})"
        )
