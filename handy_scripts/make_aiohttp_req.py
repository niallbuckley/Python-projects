import aiohttp_inject_header
import aiohttp
import asyncio
import asyncio.exceptions

url="https://google.com"

aiohttp_inject_header.shim_aiohttp_request()

async def make_req(session):
    try:
        timeout = aiohttp.ClientTimeout(total=200)
        resp = await session.request(
            method="GET",
            url=url,
            timeout=timeout,
        )
        if resp.status == 200:
            print("success!!")
            print(resp.request_info.headers)
            return
        else:
            print("resp: ", resp.status)
    except asyncio.exceptions.TimeoutError:
        print(f"Timeout while sending settings to archiver for url: {url}")
    except Exception:
        print(f"Unable to send settings to archiver using url: {url}")

async def main():
    async with aiohttp.ClientSession() as session:
        await make_req(session)

asyncio.run(main())
