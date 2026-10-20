import time
from datetime import date
import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://www.plaisio.gr/list/anavathmisi-diktia/anavathmisi-pc/kartes-grafikon"
headers = {"User-Agent": "gpu-price-tracker (personal learning project; github.com/odysmpasias)"}

products = []
today = date.today().isoformat()
for page in range(1,21):
    url = f"{base_url}?page={page}"
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all(attrs={"data-test": "ProductPortrait"})

    if len(cards) == 0:
        break

    container = soup.find(attrs={"data-test":"Products" })
    expected_total = int(container["data-cnstrc-num-results"])

    print(f"Page {page}: {len(cards)} cards")
    for card in cards:
        products.append({"id" :card["data-cnstrc-item-id"],"name" : card["data-cnstrc-item-name"],"price" : card["data-cnstrc-item-price"], "date" : today})
    time.sleep(2)

print(len(products))

if len(products) == 0:
    raise RuntimeError("No products found. The page layout may have changed.")

if len(products) != expected_total:
    raise RuntimeError(f"Expected {expected_total} products but collected {len(products)}.")

df = pd.DataFrame(products)
print(df.head())
df.to_csv(f"data/raw/{today}.csv", index = False)