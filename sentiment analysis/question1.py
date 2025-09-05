import httpx

def main():
    # API endpoint (dummy OpenAI endpoint)
    url = "https://aipipe.org/openrouter/v1/chat/completions"

    # Headers with dummy API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDQ5MjJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.AxrDGrgj0BrU6THvuENDgLLbbG9rXil_eGKqHb1ZvA0"
    }

    # Request body with required model and messages
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Analyze the sentiment of the given text and classify it as GOOD, BAD, or NEUTRAL ONLY."
            },
            {
                "role": "user",
                "content": "Aaxd qaRyNyIZiT OeE ShJ7 4D  hNiMz  02Bvti 9TvqfYe"
            }
        ]
    }

    # Send POST request (dummy)
    response = httpx.post(url=url,json=payload,headers=headers,timeout=30.0)
    result=response.json()
    sentiment=result['choices'][0]['message']['content']
    print(sentiment)

if __name__ == "__main__":
    main()
