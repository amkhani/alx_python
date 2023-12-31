import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

print(response.text)

if response.status_code >= 400:
    print("Error code:", response.status_code)
