import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="mcp",
    args=["run", "server.py"],
    env=None
)

def extract_content(payload):
    if hasattr(payload, "contents"):
        contents = payload.contents
        if contents:
            first = contents[0]
            if hasattr(first, "text"):
                return first.text

    if hasattr(payload, "content"):
        content = payload.content
        if content and hasattr(content[0], "text"):
            return content[0].text
        return str(content)

    return str(payload)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            resources = await session.list_resources()
            print("Resources:")
            for res in resources.resources:
                print(f"- {res.uri}")

            tools = await session.list_tools()
            print("\nTools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            cities = await session.read_resource("cities://list")
            print("\ncities://list ->")
            print(extract_content(cities))

            weather = await session.call_tool("get_weather", {"city": "Paris"})
            print("\nget_weather(Paris) ->")
            print(extract_content(weather))

if __name__ == "__main__":
    asyncio.run(run())