import requests, sendemail

api_key = "0d817cf9e8d04c40b77782c0f27dc607"
topic = "amazon"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}"
       "&from=2023-08-25"
       "&sortBy=publishedAt"
       "&apiKey=0d817cf9e8d04c40b77782c0f27dc607"
       "&language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news" + "\n"
for article in content['articles'][:20]:
    body = (body + article['title'] + "\n"
            + article['description'] + "\n"
            + article['url'] + "\n\n")

body = body.encode("utf-8")
sendemail.send_email(body)