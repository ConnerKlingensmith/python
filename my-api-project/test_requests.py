import requests

response = requests.get('https://api.github.com')
print(f"Status Code: {response.status_code}")
print(f"Using requests version: {requests.__version__}")
