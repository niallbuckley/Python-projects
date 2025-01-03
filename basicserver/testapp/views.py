from django.http import JsonResponse
import een_web.common.meazure.meazure as meazure
import requests

meazure.shim_request()

def make_request():
    """A simple function to make an HTTP request."""
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API
    response = requests.get(url)
    return dict(response.request.headers)

def test_view(request):
    """View that triggers the `make_request` function."""
    try:
        data = make_request()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
