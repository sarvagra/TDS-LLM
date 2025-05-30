# %%
import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv


# %%# Listing available models from OpenAI API
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
r = requests.get('https://aiproxy.sanand.workers.dev/openai/v1/models', headers={"Authorization": f"Bearer {OPENAI_API_KEY}"})
r.json()
# %% listing top 3 models
r.json()['data'][:3]

# %% read the movie review file
reviews=pd.read_csv('../resources/movie-reviews.csv')
reviews.review.iloc[0] # extract reviews


# %% get sentiment of the first review using OpenAI API
model="gpt-4o-mini"
message = [
    {
        "role" : "system",
        "content" :"identify the sentiment of the review as positive or negative.Just say positive or negative"
    },
    {
        "role": "user",
        "content": reviews.review.iloc[0]
    }
]

data ={
    "model": model,
    "messages": message
}
headers = {
    "content-type"  : "application/json",
    "authorization" : f"Bearer {OPENAI_API_KEY}"

} 
response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",headers=headers,data=json.dumps(data))
result = response.json()
ans = result['choices'][0]['message']['content']

# %%
print(ans)
# %% define a function to get sentiment of a review
def sentiment(review):
    message = [
        {
            "role": "system",
            "content": "Identify the sentiment of the review as positive or negative. Just say positive or negative"
        },
        {
            "role": "user",
            "content": review
        }
    ]

    data = {
        "model": "gpt-4o-mini",
        "messages": message
    }

    response = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )
    
    result = response.json()
    try:
        return result['choices'][0]['message']['content'].strip().lower()
    except Exception as e:
        print(f"Error: {e}")
        return "error"
# %% apply function to all reviews
reviews['sentiment'] = reviews.review.apply(sentiment)

# %%
#print(reviews['sentiment'])
old_reviews=pd.read_csv('../resources/movie-reviews.csv')
merged=old_reviews.merge(reviews, on='review')
print(merged)
# %% compare the sentiments, produce the score 
sum=0
for i in range(len(merged)):
    if merged['sentiment_x'][i] == merged['sentiment_y'][i]:
        sum=sum+1
print(f"Accuracy: {sum/len(merged)* 100} %") # print accuracy

