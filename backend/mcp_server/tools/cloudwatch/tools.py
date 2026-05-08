from backend.mcp_server.tools.cloudwatch import cloudwatch_logs_client
from backend.mcp_server.tools.cloudwatch.schema import LogEvent,CloudWatchlogsResponse
from backend.mcp_server.server import mcp

@mcp.tool()
def get_recent_logs(log_group_name:str,limit:int=10):
    """
    Fetch recent CloudWatch logs from a log group.
    """
    try:
        response=(cloudwatch_logs_client.filter_log_events(
            logGroupName=log_group_name,
            limit=limit
        )
        events=response.get("events",[])
        logs=[]
        for event in events:
        logs.append(
                LogEvent(
                    timestamp=event["timestamp"],
                    message=event["message"]
                )
            )
        result=CloudWatchlogsResponse(
            logs=logs
        )
        return result.model_dump()
    except Exception as e:
        return {"error":str(e)}

