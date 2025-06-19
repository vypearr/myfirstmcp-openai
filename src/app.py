from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import PlainTextResponse

# MCP with token
mcp = FastMCP("Demo")

# Visible homepage
async def homepage(request):
    return PlainTextResponse("✅ MCP Server is running!")

# Final app with streamable HTTP mount
app = Starlette(
    routes=[
        Route("/", endpoint=homepage),
        Mount("/stream", app=mcp.http_app()),  # ✅ new streamable HTTP route
    ]
)

# Tools and resources
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
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
