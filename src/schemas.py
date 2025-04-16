from pydantic import BaseModel



class Prompt(BaseModel):
    news : str

    