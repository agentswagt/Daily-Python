import requests
import sys

base_url = "http://cpbook.subeen.com/p/download"

info_dt = {"name": "Subeen", "email": "book@subeen.com", "country": "Bangladesh"}

url = base_url + "process.php"

response = requests.post(url, data=info_dt)



with open("cpbook.pdf", "wb") as fp:
    fp.write(response.content)
print("Book Download Completed!")

