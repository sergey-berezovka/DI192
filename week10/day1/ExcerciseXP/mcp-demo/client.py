import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None
)

def extract_text(result):
    if hasattr(result, "contents") and result.contents:
        return result.contents[0].text
    if hasattr(result, "content") and result.content:
        return result.content[0].text
    return str(result)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            resources = await session.list_resources()
            print("Resources:")
            for r in resources.resources:
                print("-", r.uri)

            tools = await session.list_tools()
            print("\nTools:")
            for t in tools.tools:
                print("-", t.name)

            greeting = await session.read_resource("greeting://hello")
            print("\nGreeting:")
            print(extract_text(greeting))

            result = await session.call_tool("add", {"a": 1, "b": 7})
            print("\nAdd result:")
            print(extract_text(result))

if __name__ == "__main__":
    asyncio.run(run())