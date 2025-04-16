from pydantic import BaseModel
from typing import Optional #,Literal

class Summary(BaseModel):
    Headline : str
    Topic : str
    Summary : str
    Readability : Optional[str]
    Star : str





# Topic : Literal["Politics", "Science", "Technology", "Health"] can be used