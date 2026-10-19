import time
from datetime import date
import requests
from bs4 import BeautifulSoup


base_url = "https://www.plaisio.gr/list/anavathmisi-diktia/anavathmisi-pc/kartes-grafikon"
headers = {"User-Agent": "gpu-price-tracker (personal learning project; github.com/odysmpasias)"}

products = []
today = date.today().isoformat()
for page in range(1,21):
    url = f"{base_url}?page={page}"
    response = requests.get(url, headers=headers, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all(attrs={"data-test": "ProductPortrait"})

    if len(cards) == 0:
        break

    print(f"Page {page}: {len(cards)} cards")
    for card in cards:
        products.append({"id" :card["data-cnstrc-item-id"],"name" : card["data-cnstrc-item-name"],"price" : card["data-cnstrc-item-price"], "date" : today})
    time.sleep(2)
    print(len(products))