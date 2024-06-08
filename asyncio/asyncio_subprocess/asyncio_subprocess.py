import asyncio


async def main():
    process = await asyncio.create_subprocess_exec('python','username.py',stdin =asyncio.subprocess.PIPE,
                                                   stdout=asyncio.subprocess.PIPE)
    std_out,std_err = await process.communicate(b"mohammad")
    print(process.pid)
    print(std_out)
    print(std_err)
    status_code = await process.wait()
    print(status_code)

asyncio.run(main())