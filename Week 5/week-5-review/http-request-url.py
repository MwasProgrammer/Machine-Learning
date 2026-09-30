import urllib.request, json # urllib.request is used for opening and fetching data from URLs (making HTTP requests).
# Fetch a public API and print the response
url = "https://httpbin.org/json"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())
print(json.dumps(data, indent=2))