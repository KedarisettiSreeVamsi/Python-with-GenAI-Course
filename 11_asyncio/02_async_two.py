import asyncio
import time
async def brew(name):
    print(f"Brewing {name} chai...")
    await asyncio.sleep(2)
    print(f"{name} chai is ready...")

async def main():
    await asyncio.gather(brew("Masala"),brew("Ginger"))

asyncio.run(main())