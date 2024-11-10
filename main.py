import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
