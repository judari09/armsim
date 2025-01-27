from pydantic import BaseModel


class linkBase(BaseModel):
    name:str
    type:str
    range:list[2]
    
class linkCreate(linkBase):
    pass
    