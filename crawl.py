import urllib3
from bs4 import BeautifulSoup

url = "https://news.naver.com"

http = urllib3.PoolManager()
resp = http.request("GET", url)
print(resp.status)
soup = BeautifulSoup(resp.data, "html.parser")

for link in soup.find_all("a"):
    print(link.text.strip(), link.get("href"))

for link in soup.find_all("img"):
    print(link.text.strip(), link.get("src"))
