import os
from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

completion = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Your response should be in JSON format."},
    {"role": "user", "content": "Hello!"}
  ],
  response_format={"type": "json_object"}
)

print(completion.choices[0].message.content)

# Check if the OpenAI API response is a valid JSON
import json

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

print(is_json(completion.choices[0].message.content))
