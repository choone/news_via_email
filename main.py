import requests, sendemail

api_key = "0d817cf9e8d04c40b77782c0f27dc607"
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-08-23\
&sortBy=publishedAt&apiKey=0d817cf9e8d04c40b77782c0f27dc607'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    body = (body + article['title'] + "\n"
            + article['description'] + "\n\n")

body = body.encode("utf-8")
sendemail.send_email(body)