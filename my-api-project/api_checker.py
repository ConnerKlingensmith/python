#!/home/ec2-user/Downloads/Python/my-api-project/venv/bin/python

import requests
import sys

def check_api(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"✓ {url} - Status: {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"✗ {url} - Error: {e}")
        return none

if __name__ == "__main__":
    urls = [
            "https://api.github.com",
        "https://httpbin.org/get",
    ]

    for url in urls:
        check_api(url)

import sys
print(f"\nPython interpreter: {sys.executable}")
