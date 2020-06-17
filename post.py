import requests
import sys
base_url = "http://subeen.com/download"

info_dt = {"name": "Subeen", "email": "book@subeen.com", "country": "Bangladesh"}

url = base_url + "process.php"

response = requests.get(url, data=info_dt)

if response.ok is False:
    sys.exit("Error Downloading File")

with open("cpbook.pdf", "wb") as fp:
    fp.write(response.content)

print("Book Downloaded Completed")