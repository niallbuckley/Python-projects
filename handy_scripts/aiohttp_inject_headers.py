import aiohttp
import asyncio
import asyncio.exceptions

url="https://google.com"

def shim_aiohttp_request():
    old_fn = aiohttp.ClientSession._request

    async def shim_requests(self, method, url, *args, **kwargs):
        headers = kwargs.get('headers', {})

        # Inject the custom b3 header
        headers['b3'] = 'asdfasdfasdf'
        # Update the kwargs with the modified headers
        kwargs['headers'] = headers

        return await old_fn(self, method, url, *args, **kwargs)

    aiohttp.ClientSession._request = shim_requests

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
    shim_aiohttp_request()

    async with aiohttp.ClientSession() as session:
        await make_req(session)


asyncio.run(main())   
