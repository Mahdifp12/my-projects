import requests
from requests.api import get

def get_title(url):
    req = requests.get(url)
    rt = req.text
    print(rt[rt.find("<title>") + 7 : rt.find("</title>")])

get_title("https://aparat.com")