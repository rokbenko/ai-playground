import vertexai
from vertexai.preview.generative_models import GenerativeModel

project_id = 'xxxxxxxxxxxxxxxxxxx'
location = 'us-central1'

vertexai.init(project=project_id, location=location)

model = GenerativeModel('gemini-pro')
response = model.generate_content('Say hi')

print(response.text)