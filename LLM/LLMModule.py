"""
First AI Agent using grok API
https://console.groq.com/docs/
"""
import os
import httpx
from groq import Groq

# Create HTTP client with SSL verification disabled
http_client = httpx.Client(verify=False)

# Initialize Groq client
client = Groq(
    api_key=os.getenv("RONISH_GROQ_KEY"),
    http_client=http_client
)

# Use a CURRENT supported model
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",   # ✅ supported model
    messages=[
        {"role": "user", "content": "Hello! Explain AI in one sentence."}
    ]
)

print(response.choices[0].message.content)