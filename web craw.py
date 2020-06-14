import requests
url = "https://scblog.netlify.app"

response = requests.get(url)

with open("shagato.html", "w") as f:
    f.write(response.text)
