from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Holiday(BaseModel):
    at: datetime
    name: str
    link: HttpUrl | None
