import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    full_name: str
    username: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str | None = Field(default_factory=None)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class UserFullName(SQLModel):
    full_name: str


class UserUsername(SQLModel):
    username: str


class UserEmail(SQLModel):
    email: EmailStr


class UserPassword(SQLModel):
    password: str
