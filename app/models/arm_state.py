from pydantic import BaseModel
from robot import *

class armStateBase(BaseModel):
    name_robot: str
    is_used: bool
    ef_pos_x:float
    ef_pos_y:float
    ef_pos_z:float
    
class armStateCreate(armStateBase):
    pass 


    