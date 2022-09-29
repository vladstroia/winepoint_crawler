
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
# import lines from lines
from lines import lines

for line in lines:
    searchTerm = line
    print(line)
    searchPhrase = "https://www.winepoint.ro/index.php?main_page=advanced_search_result&search_in_description=1&keyword=" +searchTerm.replace(" ", "+")
    driver.get(searchPhrase)
    input("Press Enter to continue...")
    print(driver.current_url)
    f = open("links.txt", "a")
    f.write(f"'{driver.current_url}',\n")
    f.close()

