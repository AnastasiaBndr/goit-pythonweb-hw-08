from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, relationship, mapped_column
from datetime import date
from .contacts import Base


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
        return f"Contsct: ({self.id}, {self.first_name} 
        {self.second_name} {self.email} {self.phone_number} {self.birthday} {self.additional_data})"
