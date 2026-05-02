import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    print(f"Success! Post Title: {data['title']}")
    print(f"Status Code: {response.status_code}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")