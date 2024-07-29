# models.py
from pydantic import BaseModel
from typing import List

class ContactResponse(BaseModel):
    contacts: List[str]
