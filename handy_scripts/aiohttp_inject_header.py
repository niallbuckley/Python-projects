import aiohttp

url="https://google.com"

def inject_headers(kwargs):
    headers = kwargs.get('headers', {})

    # Inject the custom b3 header
    headers['b3'] = 'asdfasdfasdf'
    # Update the kwargs with the modified headers
    kwargs['headers'] = headers


def shim_aiohttp_request():
    #import aiohttp
    old_fn = aiohttp.ClientSession._request


    async def shim_requests(self, method, url, *args, **kwargs):
        inject_headers(kwargs)
        return await old_fn(self, method, url, *args, **kwargs)

    aiohttp.ClientSession._request = shim_requests