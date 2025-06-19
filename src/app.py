# server.py

from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

# Create an MCP server
mcp = FastMCP("Demo")

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount("/", app=mcp.sse_app()),
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


""" if __name__ == "__main__":
    # Set up logging
    import uvicorn

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.INFO)

    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000) """
