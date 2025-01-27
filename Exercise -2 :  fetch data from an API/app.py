import requests

# Make a GET request to a public API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check if the request was successful
if response.status_code == 200:
    post = response.json()
    print("Post fetched from API:")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
else:
    print("Failed to fetch post from API")
