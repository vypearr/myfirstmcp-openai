from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import PlainTextResponse

# Create an MCP server with a token.
mcp = FastMCP("Demo", auth_token="ttambi7")

# Visible homepage route
async def homepage(request):
    return PlainTextResponse("✅ MCP Server is running!")

# ASGI app with homepage and SSE
app = Starlette(
    routes=[
        Route("/", endpoint=homepage),         # Visible root route
        Mount("/sse", app=mcp.sse_app()),      # SSE for MCP Inspector
    ]
)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

"""
# Uncomment this section for local testing (optional)
if __name__ == "__main__":   
    import uvicorn
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.INFO)

    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
