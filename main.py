 
# // use selenium to download website "https://www.winepoint.ro/tari/vin-rosu/franta/bordeaux/saint-emilion/chateau-de-grand-mayne/saint-emilion-grand-cru-classe-2016"
# // and save it as "saint-emilion-grand-cru-classe-2016.html"    

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
# #chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# # chrome_options.headless = True # also works
# driver = webdriver.Chrome(options=chrome_options)



# driver.get("https://www.winepoint.ro/tari/vin-rosu/franta/bordeaux/saint-emilion/chateau-de-grand-mayne/saint-emilion-grand-cru-classe-2016")
# # driver.find_element_by_id("nav-search").send_keys("Selenium")
# # save the page as html
# # html = driver.page_source
# # with open("saint-emilion-grand-cru-classe-2016.html", "w") as file:
# #     file.write(html)
# # driver.close()
# # print the span iwth id "description"
# print(driver.find_element(By.ID, "description"))





# import pandas as pd

# tables = pd.read_html("https://www.winepoint.ro/tari/vin-rosu/franta/bordeaux/saint-emilion/chateau-de-grand-mayne/saint-emilion-grand-cru-classe-2016")
# print(tables)


import requests
# from lxml import etree
from bs4 import BeautifulSoup

# Reading temperature of New York
URL = "https://www.winepoint.ro/tari/vin-rosu/franta/bordeaux/saint-emilion/chateau-de-grand-mayne/saint-emilion-grand-cru-classe-2016"
resp = requests.get(URL)

if resp.status_code == 200:

    # Using BeautifulSoup
    soup = BeautifulSoup(resp.text, "lxml")
    # print(soup.find(id="description"))
    # print(soup.get_text())  
    # for span in soup.find(id="productDescription").get_text():
    #     print(span)
    print(soup.find(id="productDescription").get_text())
    # elements = soup.select('span[data-testid="TemperatureValue"][class^="CurrentConditions"]')
    # print(elements[0].text)