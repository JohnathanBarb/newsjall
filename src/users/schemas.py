from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreateUserInput(BaseModel):
    email: str
    name: str
    password: str


# TODO: rename it to UserOutput
class CreateUserOutput(BaseModel):
    id: UUID
    email: str
    name: str
    created_at: datetime
    updated_at: datetime
