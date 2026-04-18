from enum import StrEnum

from pydantic import BaseModel


class StatusEnum(StrEnum):
    OK = "OK"
    NOTOK = "NOTOK"


class HealthOut(BaseModel):
    app: StatusEnum
