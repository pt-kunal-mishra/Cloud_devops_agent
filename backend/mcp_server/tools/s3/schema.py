from pydantic import BaseModel
from typing import List, Optional

class S3BucketResponse(BaseModel):
    buckets:List[str]
class S3ObjectResponse(BaseModel):
    objects:List[str]

class UploadResponse(BaseModel):
    bucket:str
    key:str
    status:str



