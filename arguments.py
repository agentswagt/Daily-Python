import sys
import requests

img_url = sys.argv[1]
file_name = sys.argv[2]
r = requests.get(img_url)
with open(file_name, "wb") as f:
    f.write(r.content)