from pydantic import BaseModel

class EC2InstanceStatusRequest(BaseModel):
    instance_id:str


class EC2StatusResponse(BaseModel):
    instance_id:str
    instance_state:str
    instacne_type:str
    availability_zone:str
    public_ip_address:str |None=None
    private_ip_address:str |None=None

    
