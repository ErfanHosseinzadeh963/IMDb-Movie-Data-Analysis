import requests

#url = "https://www.imdb.com/chart/top/"
#url = "https://pfxa.ir/blog/"
url = "https://maktabkhooneh.org/lms/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D9%BE%D8%B1%D9%88%DA%98%D9%87-%D9%85%D8%AD%D9%88%D8%B1-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-mk6104/unit/125537/"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers, timeout=20)

print("HTTP status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response preview:")
print(response.text[:1500])