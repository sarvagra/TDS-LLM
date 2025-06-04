"""
PROBLEM STATEMENT:
Project: DataSentinel Inc. - Sentiment Analysis Test Harness
------------------------------------------------------------

Overview:
---------
DataSentinel Inc. is a tech company specializing in advanced Natural Language Processing (NLP) solutions. 
As part of their latest project, they are integrating an AI-powered sentiment analysis module into an internal 
monitoring dashboard. The purpose of this module is to automatically classify large volumes of unstructured 
feedback and text data into one of three categories: GOOD, BAD, or NEUTRAL.

Quality Assurance Objective:
----------------------------
To ensure the robustness of this system, the development team is tasked with building a test harness in Python. 
The goal is to simulate the API interaction and verify that messages are correctly formatted and processed, 
even for edge cases like meaningless or incoherent text.

Implementation Details:
------------------------
- The test harness uses the `httpx` library (dummy implementation).
- The model used for inference is `"gpt-4o-mini"`.
- A dummy API key is passed in the Authorization header.
- The test sends a POST request to OpenAI's API with two messages:
    1. A system message instructing the model to classify the sentiment as either GOOD, BAD, or NEUTRAL.
    2. A user message containing the meaningless text: 
       "Aaxd qaRyNyIZiT OeE ShJ7 4D  hNiMz  02Bvti 9TvqfYe"

Success Criteria:
-----------------
- The API should accept the request and return a valid response.
- The output should be one of the expected sentiment categories (GOOD, BAD, or NEUTRAL).
- This validates message formatting and integration before deploying the system to production environments 
  where real customer feedback will be analyzed.

Limitations:
------------
- The script uses a dummy version of the `httpx` library.
- Only the following methods are allowed:
    - `response = httpx.get(url, **kwargs)`
    - `response = httpx.post(url, json=None, **kwargs)`
    - `response.raise_for_status()`
    - `response.json()`

Note:
-----
This controlled testing environment is crucial for ensuring that the full pipeline behaves as expected 
under various input conditions, thereby supporting DataSentinel's commitment to high operational standards 
and rapid, accurate decision-making.
"""

# %%
import httpx
import json
import os
from dotenv import load_dotenv

# %% define variables and keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
text="Aaxd qaRyNyIZiT OeE ShJ7 4D  hNiMz  02Bvti 9TvqfYe"
url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
headers={
    "authorization" : f"Bearer {OPENAI_API_KEY}",
    "content-type" : "application/json"
}
payload={
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Classify the sentiment of the review ONLY as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": text
        }
    ]
}
# %% get sentiment using OpenAI API, httpx version
response = httpx.post(url=url,json=payload,headers=headers,timeout=30.0)
result=response.json()
sentiment=result['choices'][0]['message']['content']
print(sentiment)

# %%
print(result)
# %%
