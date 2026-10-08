import os
import requests

apikey= os.environ["ANTHROPIC_API_KEY"]
url = "https://api.anthropic.com/v1/messages"
h = {"x-api-key":apikey, "anthropic-version": "2023-06-01", "content-type": "application/json" }
b = {
    "model": "claude-haiku-5-5",
    "max_tokens": 300,
    "messages": [
      {"role": "user", "content": "Name three things printed on a typical Australian receipt."}
    ]
  }

response = requests.post(url, headers=h, json=b)
data = response.json()
print(data)



print(f"claude's answer text: {data['content'][0]['text']}")
print(f"stop reason: {data['stop_reason']}")
print(f"input tokens: {data['usage']['input_tokens']}")
print(f"output tokens: {data['usage']['output_tokens']}")
print(type(response.text))
print(type(data))







# print(f"status code: {response.status_code}")
# print(f"text: {response.text}")