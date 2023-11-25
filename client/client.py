import asyncio
from graphql_client import Client


async def get_all_posts():
    client = Client("http://localhost:5000/graphql")
    result = await client.all_posts()

    print(result.list_posts)

asyncio.run(get_all_posts())