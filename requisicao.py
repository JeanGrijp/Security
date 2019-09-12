
import requests

url = 'https://www.youtube.com/'
req = requests.get(url)
print(req.text)
res = requests.post(url)