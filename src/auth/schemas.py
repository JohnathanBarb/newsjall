from pydantic import BaseModel


class LoginRequestInput(BaseModel):
    email: str
    password: str


class TokenPairOutput(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
