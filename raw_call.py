import os
import requests
from parse import get_text, is_complete, total_tokens

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


print(f"Answer: {get_text(data)}")
print(f"Complete: {is_complete(data)}")
print(f"Total tokens: {total_tokens(data)}")


