import json, os

# Simulated social media API response
response_text = '''
{
    "user": "Amerix",
    "followers": 1200000,
    "last_post": {
        "title": "Cold shower protocol",
        "likes": 4800
    }
}'''

data = json.loads(response_text)

user = data["user"]
followers = data["followers"]
likes = data["last_post"]["likes"]

print("X Social Media Post")
print("-" * 40)
print(f"Followers: {followers}")
print(f"Last post likes: {likes}")