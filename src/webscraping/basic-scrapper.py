import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=hm_nv_menu"
page = requests.get(url)
suop = BeautifulSoup(page.text, 'html.parser')
print(suop)