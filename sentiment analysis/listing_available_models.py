import requests

OPENAI_API_KEY= "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDQ5MjJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.CfwJHvL6a0adtb7_Xu9in2i4Kg7BLXJTP6h3Qr_96D4"
r = requests.get('https://aiproxy.sanand.workers.dev/openai/v1/models', headers={"Authorization": f"Bearer {OPENAI_API_KEY}"})
r.json()