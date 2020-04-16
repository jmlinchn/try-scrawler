import requests
import re

from bs4 import BeautifulSoup

link = 'http://www.santostang.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

for tag in soup.find_all(re.compile("^h")):
    print(tag.name)