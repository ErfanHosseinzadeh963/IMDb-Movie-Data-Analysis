import requests
from bs4 import BeautifulSoup

url = "https://arxiv.org/list/cs.AI/recent?utm_source=chatgpt.com"
page = requests.get(url)
suop = BeautifulSoup(page.text, 'html.parser')
print(suop)