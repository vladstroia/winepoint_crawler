 





# import pandas as pd

# tables = pd.read_html("https://www.winepoint.ro/tari/vin-rosu/franta/bordeaux/saint-emilion/chateau-de-grand-mayne/saint-emilion-grand-cru-classe-2016")
# print(tables)

import unidecode
# unaccented_string = unidecode.unidecode(accented_string)
import requests
# from lxml import etree
from bs4 import BeautifulSoup
from links import links

import re
for link in links:
    URL = link
    resp = requests.get(URL)
    if "search&search" not in link:
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            imageTag = re.findall('src=".*"',str(soup.find('div', {"id": "productMainImage"})))[0][5:-1]
            # img_url = "https://www.winepoint.ro/" + re.findall('src=".*"', imageTag)[0][5:-1]
            img_url = "https://www.winepoint.ro/" + imageTag

            soup.find('div', {"class": "manuf_title"}).decompose()
            vin = soup.find("h1", {"class": "productsTitle"}).get_text().strip()
            

            imageTag = re.findall('src=".*"',str(soup.find('div', {"id": "productMainImage"})))[0][5:-1]
            numePoza = unidecode.unidecode(vin.replace(" ","-")) + imageTag[-4:]

            with open(f"images/{numePoza}", 'wb') as handle:
                response = requests.get(img_url, stream=True)
                print(numePoza)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)


