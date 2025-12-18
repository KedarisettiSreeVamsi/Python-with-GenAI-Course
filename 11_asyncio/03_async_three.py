import aiohttp
import asyncio

async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = [f"https://httpbin.org/delay/{i}" for i in range(1,4)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
