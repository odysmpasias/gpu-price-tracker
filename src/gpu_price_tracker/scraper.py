import requests
from bs4 import BeautifulSoup

url = "https://www.plaisio.gr/list/anavathmisi-diktia/anavathmisi-pc/kartes-grafikon"
headers = {"User-Agent": "gpu-price-tracker (personal learning project; github.com/odysmpasias)"}

response = requests.get(url, headers=headers, timeout=20)
soup = BeautifulSoup(response.text, "html.parser")
cards = soup.find_all(attrs={"data-test": "ProductPortrait"})

for card in cards:
    print(card["data-cnstrc-item-id"], card["data-cnstrc-item-name"], card["data-cnstrc-item-price"])
    