"""
    lock
"""
import asyncio

counter = 0


async def increment(lock):
    global counter
    await lock.acquire()
    temp_counter = counter
    temp_counter+=1
    await asyncio.sleep(0.1)
    counter = temp_counter
    lock.release()


async def main():
    global counter
    lock = asyncio.Lock()
    T = [asyncio.create_task(increment(lock)) for _ in range(100)]
    await asyncio.gather(*T)
    print("result:",counter)


asyncio.run(main())