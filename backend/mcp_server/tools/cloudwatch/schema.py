from pydantic import BaseModel
from typing import List,Optional

class CloudWatchLogRequest(BaseModel):
    log_group_name:str
    limit:int=10

class LogEvent(BaseModel):
    timestamp:int
    message:str

class CloudWatchlogsResponse(BaseModel):
    logs:List[LogEvent]
