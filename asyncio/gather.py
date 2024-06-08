import aiohttp
import asyncio

async def show_status(session,url):
        async with session.get(url) as response:
            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])
            await asyncio.sleep(4)
            # html = await response.text()
            # print("Body:", html[:15], "...")
            return response.status

async def main():
    urls =['http://pythdfsfon.org','http://python.org','http://python.org','http://python.org']
    async with aiohttp.ClientSession() as session:
        list_requasts = [show_status(session,url) for url in urls]
        result_status = await asyncio.gather(*list_requasts,return_exceptions=True) # await --> run asyncio.gather(*list_requasts)
        print(result_status)

asyncio.run(main())