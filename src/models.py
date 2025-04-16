from pydantic import BaseModel, Field
from typing import Optional #,Literal

class Summary(BaseModel):
    Headline : str
    Topic : str
    Summary : str
    Readability : float = Field(..., ge=1.0, le=5.0)
    Star : str





# Topic : Literal["Politics", "Science", "Technology", "Health"] can be used