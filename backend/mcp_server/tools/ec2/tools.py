from backend.mcp_server.tools.ec2 import ec2_client
from backend.mcp_server.clients.aws_client import ec2_client

from backend.mcp_server.tools.ec2.schema import(
    EC2StatusResponse, EC2InstanceStatusRequest
)

@mcp.tool()
def get_ec2_status(instance_id:str):
    """"
    Get Ec2 instance status and metadata information
    """
    try:
        response=ec2_client.describe_instance(
            InstanceIds=[instance_id]
        )
        reservations=response.get("Reservations")

        if not reservations:
            return{
                "error":"Instance not found"
            }
        instance=reservations[0].get("Instances")[0]

        result=EC2StatusResponse(
            instance_id=instance_id,
            instance_state=instance["State"]["Name"],
            instance_type=instance["InstanceType"],
            availability_zone=instance["Placement"]["AvailabilityZone"],
            public_ip_address=instance.get("PublicIpAddress"),
            private_ip_address=instance.get("PrivateIpAddress")
        )
        return result.model_dump()
    except Exception as e:
        return{
            "error":str(e)
        }

