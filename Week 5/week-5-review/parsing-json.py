import json
# Parse this nested JSON and print the author and title
response = '{"book": {"title": "Clean Code", "author": "Robert Martin", "year": 2008}}'
data = json.loads(response)
book = data["book"]
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")