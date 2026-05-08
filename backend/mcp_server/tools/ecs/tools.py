from backend.mcp_server.server import mcp

from backend.mcp_server.clients.aws_client import (
    ecs_client
)
from backend.mcp_server.tools.ecs.schema import(
    ECSServiceResponse, ECSUpdateResponse
)

@mcp.tool()
def list_ecs_services(cluster_name:str):
    """
    List ECS services in a cluster.
    """
    try:
        response=ecs_client.list_services(
            cluster=cluster_name
        )
        result=ECSServiceResponse(
            service_arns=response['serviceArns']

        )
        return result.model_dump()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def update_ecs_service(
    cluster_name:str,
    service_name:str,
    desired_count:int
):
    """
    Scale ECS service to the desired count of an ECS service.
    """
    try:
        response=ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            desiredCount=desired_count
        )
        service=response['service']

        result=ECSUpdateResponse(
            service=service['serviceName'],
            desired_count=service['desiredCount'],
            status=service['status']
        )
        return result.model_dump()
    except Exception as e:
        return {"error": str(e)}
    

@mcp.tool()
def restart_ecs_service(
    cluster_name:str,
    service_name:str
):
    """
    Restart an ECS service by forcing a new deployment.
    """
    try:
        response=ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            forceNewDeployment=True
        )
        service=response['service']

        
        return {
            "service": service['serviceName'],
            "status": service['status'],
            "message":"New deployment triggered successfully."
        }
    except Exception as e:
        return {"error": str(e)}

