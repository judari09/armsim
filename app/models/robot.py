from pydantic import BaseModel

class robotBase(BaseModel):
    name:str
    number_links: int
    type_robot:str

class robotCreate(robotBase):
    pass