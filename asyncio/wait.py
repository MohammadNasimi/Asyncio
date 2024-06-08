import aiohttp
import asyncio
import random

async def show_status(session,url,delay):
        await asyncio.sleep(delay)
        async with session.get(url) as response:
            print( f'status for {url} ---> {response.status}')
            return f'status for {url} ---> {response.status}'

async def main():
    urls =['http://python.org','http://python.org','http://python.org','http://python.org']
    async with aiohttp.ClientSession() as session:
        list_requasts = [show_status(session,url,random.randint(2,5)) for url in urls]
        for req in asyncio.as_completed(list_requasts):
             await req

asyncio.run(main())