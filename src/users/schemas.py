from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreateUserInput(BaseModel):
    email: str
    name: str
    password: str


class CreateUserOutput(CreateUserInput):
    id: UUID
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
