from backend.mcp_server.server import mcp
from backend.mcp_server.clients.aws_client import s3_client

from backend.mcp_server.tools.s3.schema import (
    S3BucketResponse,
    S3ObjectResponse,
    UploadResponse
)

@mcp.tool()
def list_s3_buckets():
    """"List All s3 buckets"""
    
    try:
        response=s3_client.list_buckets()
        buckets=[
            bucket["Name"]
            for bucket in response["Buckets"]
        ]
        result=S3BucketResponse(buckets=buckets)
        return result.model_dump()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def list_s3_objects(bucket_name: str):
    """List objects in an S3 bucket"""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        contents=response.get("Contents", [])
        objects = [
            obj["Key"]
            for obj in response.get("Contents", [])
        ]
        result = S3ObjectResponse(objects=objects)
        return result.model_dump()
    except Exception as e:
        return {"error": str(e)}

from backend.mcp_server.server import mcp

from backend.mcp_server.clients.aws_clients import (
    s3_client
)

from backend.mcp_server.tools.s3.schema import (
    S3BucketsResponse,
    S3ObjectsResponse,
    UploadResponse
)


@mcp.tool()
def list_s3_buckets():

    """
    List all S3 buckets.
    """

    try:

        response = s3_client.list_buckets()

        buckets = [
            bucket["Name"]
            for bucket in response["Buckets"]
        ]

        result = S3BucketsResponse(
            buckets=buckets
        )

        return result.model_dump()

    except Exception as e:

        return {
            "error": str(e)
        }


@mcp.tool()
def list_s3_objects(
    bucket_name: str
):

    """
    List objects in an S3 bucket.
    """

    try:

        response = s3_client.list_objects_v2(
            Bucket=bucket_name
        )

        contents = response.get("Contents", [])

        objects = [
            obj["Key"]
            for obj in contents
        ]

        result = S3ObjectsResponse(
            objects=objects
        )

        return result.model_dump()

    except Exception as e:

        return {
            "error": str(e)
        }


@mcp.tool()
def upload_incident_report(
    bucket_name: str,
    object_key: str,
    content: str
):

    """
    Upload incident report to S3.
    """

    try:

        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=content
        )

        result = UploadResponse(
            bucket=bucket_name,
            key=object_key,
            status="uploaded"
        )

        return result.model_dump()

    except Exception as e:

        return {
            "error": str(e)
        }