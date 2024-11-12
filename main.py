import requests
from dotenv import load_dotenv
from send_email import send_email
import os

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
