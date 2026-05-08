from pydantic import BaseModel
from typing import List

class ECSServiceResponse(BaseModel):
    service_arns:List[str]

class ECSUpdateResponse(BaseModel):
    service:str
    desired_count:int
    status:str
