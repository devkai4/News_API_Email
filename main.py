import requests
import os
from dotenv import load_dotenv
from send_email import send_email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Set header for email's title
msg = MIMEMultipart()
msg['Subject'] = "Today's news"

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
              + article["description"] + "\n" \
              + article["url"] + 2*"\n"

msg.attach(MIMEText(body, 'plain'))
send_email(message=msg.as_string())
