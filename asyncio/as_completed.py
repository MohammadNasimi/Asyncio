import aiohttp
import asyncio
import random

async def show_status(session,url,delay):
        await asyncio.sleep(delay)
        async with session.get(url) as response:
            return f'status for {url} ---> {response.status}'

async def main():
    urls =['http://pytefhon.org','http://python.org','http://python.org','http://python.org']
    async with aiohttp.ClientSession() as session:
        list_requasts = [asyncio.create_task(show_status(session,url,random.randint(2,5))) for url in urls]
        done,pending = await asyncio.wait(list_requasts,return_when=asyncio.FIRST_EXCEPTION)
        for i in done:
            if i.exception() is None:
                print(i.result())
            else:
                print("Error .....")
        print("Done",done)
        print("Pending",pending)
        for p in pending:
             p.cancel()
        
asyncio.run(main())