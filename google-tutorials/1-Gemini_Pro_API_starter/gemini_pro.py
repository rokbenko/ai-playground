import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GOOGLE_CLOUD_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Say hi')

print(response.text)
