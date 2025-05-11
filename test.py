import requests

url = "http://127.0.0.1:1337/v1/embeddings"
headers = {"Content-Type": "application/json",
           "Authorization": "Bearer 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"}
data = {
    # "model": "gpt-3.5-turbo",
    # "config": {
    #     "messages": [{"role": "user", "content": "Hello"}],
    #
    # },
    "model": "gpt-3.5-turbo",
    "input": "Hello"

}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)  # Check if the API returns a 200 OK
print(response.text)  # Inspect raw response before trying to parse JSON

try:
    print(response.json())  # Convert response to JSON if valid
except requests.exceptions.JSONDecodeError:
    print("Invalid JSON response received.")
