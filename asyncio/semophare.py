"""
    semaphore
"""
import asyncio


async def increment(smp):
    async with smp:
        print("hello task  ........")
        await asyncio.sleep(1)


async def main():
    smp = asyncio.Semaphore(2)
    T = [asyncio.create_task(increment(smp)) for _ in range(10)]
    await asyncio.gather(*T)


asyncio.run(main())