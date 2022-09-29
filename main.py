 





# import pandas as pd

# tables = pd.read_html("https://www.winepoint.ro/tari/vin-rosu/franta/bordeaux/saint-emilion/chateau-de-grand-mayne/saint-emilion-grand-cru-classe-2016")
# print(tables)


import requests
# from lxml import etree
from bs4 import BeautifulSoup
from links import links



URL = links[0]
resp = requests.get(URL)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, "lxml")
    data = soup.find(id="productDescription").get_text()
    # data = data.split(":")
    # data = data.replace("\n", "")
    data = data.replace("\xa0", "")
    data = data.strip() 
    data = data.split("\n")
    for line in data:
        line = line.split(":")
    print(data)
    # print([x for x in data if x])
    # for line in data:
    #     print(line)
    # print(soup.find(id="productDescription").get_text())
