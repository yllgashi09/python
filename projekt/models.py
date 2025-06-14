from pydantic import Basemodel
from typing import List, Optional

class Developer(Basemodel):
    name : str
    experience: Optional[int]= None

    class project(Basemodel):
        title: str
        description: Optional[str] = None
        language: Optional[list[str]] = []
        lead_developer: Developer
