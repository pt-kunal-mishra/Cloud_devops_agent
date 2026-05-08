from mcp.server.fastmcp import FastMCP
from backend.mcp_server.tools.ec2 import tools
from backend.mcp_server.tools.cloudwatch import tools
from backend.mcp_server.tools.ecs import tools
from backend.mcp_server.tools.s3 import tools

mcp = FastMCP("Cloud-DevOps-Agent", "0.1.0")


if __name__=="__main__":
    mcp.run()
    


