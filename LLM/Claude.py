"""
https://platform.claude.com/docs/en/build-with-claude/working-with-messages
"""
import os

import anthropic
import httpx

# Basic request and response
API = os.getenv("CLAUDE_API_KEY")
HTTP_CLIENT = httpx.Client(
    verify=True,
    timeout=60.0,
    proxy="http://135.245.192.7:8000"
)
message = anthropic.Anthropic(api_key=API, http_client=HTTP_CLIENT).messages.create(
    model="claude-sonnet-4",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message)