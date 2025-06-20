from fastmcp import FastMCP

mcp = FastMCP("Demo", auth_token="ttambi")

# Visible homepage
async def homepage(request):
    return PlainTextResponse("✅ MCP Server is running!")
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000)

