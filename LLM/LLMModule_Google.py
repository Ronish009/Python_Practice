import os

import certifi
from google import genai

#os.environ["SSL_CERT_FILE"] = certifi.where()
#os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

client = genai.Client(api_key=os.getenv("RONISH_GOOGLE_API_KEY1"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain newWorkStealingPool in Executer in java language"
)
print(response.text)