from pydantic import Basemodel
from typing import Optional

class item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str