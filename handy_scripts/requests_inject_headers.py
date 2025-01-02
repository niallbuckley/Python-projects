import requests

# Shim the requests.get method to inject the custom b3 header
def shim_request():
    old_fn = requests.get  # Save the original requests.get method

    def shim_requests_get(*args, **kwargs):
        # Get the 'headers' from kwargs, defaulting to an empty dictionary if not provided
        headers = kwargs.get('headers', {})
        # Inject the custom b3 header
        headers['b3'] = 'asdfasdfasdf'
        # Update the kwargs with the modified headers
        kwargs['headers'] = headers
        # Call the original requests.get with the updated arguments
        return old_fn(*args, **kwargs)

    # Replace requests.get with the shimmed version
    requests.get = shim_requests_get

# Apply the shim
shim_request()

# Make a request to test it
response = requests.get('http://google.com', headers={"User-Agent": "CustomAgent"})
#print(response.json())
for header, value in response.request.headers.items():
    print(f"{header}: {value}")
