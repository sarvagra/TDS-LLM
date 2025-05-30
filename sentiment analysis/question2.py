# ---------------------------------------------------------------
# QUESTION 2: LLM TOKEN COST CALCULATION
# ---------------------------------------------------------------

# PROBLEM STATEMENT:

# LexiSolve Inc. is a startup that provides conversational AI solutions.
# Since OpenAI's pricing is based on token usage, tracking the number of
# tokens processed in API requests is essential.

# TASK:
# - Make a request to OpenAI's GPT-4o-Mini.
# - Send the following **user message** for token analysis:
#   "List only the valid English words from these: 
#    iUHHUCD, yqpw, r, Bob0Fj, N4wMu02RWE, g, q, fQJLG4Iy, ZFPGAy79f, e, 
#    u3ZIyl9ZN, BU9zsp, 0gniO, eXOOdC, t1L6BLvp, eU, Ri, 6MHrnS5a6, EXzB, 8, 
#    SBw, R48WPQ0X, tPC6fV, 9SbhS, iz, zLiSLWdVQL, eVM, x4m, Zltg8CshbI, 
#    I877KFK5zv, 7cjhPk70, 3Z, WF, S8TKK, oS150mB4b, urz, S6, Bx, aY, 
#    892gHr38w7, OQzCFOi6Q, d9tq6bfX ..."

# OBJECTIVE:
# - Determine the **number of input tokens** used in processing this request.
# - Extract the **token count** from the response JSON under `"usage"`.

# IMPORTANT NOTE:
# - The model counts the words and system prompts as tokens.
# - You **must actually make the request** to get the token count.

# ---------------------------------------------------------------


# %% import libraries
import httpx
import json
import os
from dotenv import load_dotenv

# %% define variables and keys
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
text="List only the valid English words from these: iUHHUCD, yqpw, r, Bob0Fj, N4wMu02RWE, g, q, fQJLG4Iy, ZFPGAy79f, e, u3ZIyl9ZN, BU9zsp, 0gniO, eXOOdC, t1L6BLvp, eU, Ri, 6MHrnS5a6, EXzB, 8, SBw, R48WPQ0X, tPC6fV, 9SbhS, iz, zLiSLWdVQL, eVM, x4m, Zltg8CshbI, I877KFK5zv, 7cjhPk70, 3Z, WF, S8TKK, oS150mB4b, urz, S6, Bx, aY, 892gHr38w7, OQzCFOi6Q, d9tq6bfX"
url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
headers={
    "authorization" : f"Bearer {OPENAI_API_KEY}",
    "content-type" : "application/json"
}
payload={
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": text
        }
    ]
}
# %% get number of tokens using OpenAI API, httpx version
response = httpx.post(url=url,json=payload,headers=headers,timeout=30.0)
result=response.json()
tokens=result['usage']['prompt_tokens']
print(tokens)

