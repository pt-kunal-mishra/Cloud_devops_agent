import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


client = MultiServerMCPClient(
  {
      "cloudops":{
          "command":"python",
          "args":[
              "-m",
              "backend.mcp_server.server",
          ],
          "transport":"stdio",
          }
  }  
)

async def get_mcp_tools():
    """Load tools from the MCP server.
    into lanchain-compatible tools."""
    tools = await client.get_tools()
    for tool in tools:
        print(tool.name)
    
    return tools
