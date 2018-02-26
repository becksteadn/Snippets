#
# Use Selenium to grab a screenshot of a website without a GUI.
#
# Required:
# Chromedriver: https://chromedriver.storage.googleapis.com/index.html?path=2.35/
# Selenium module: pip install selenium
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER = 'chromedriver'
WINDOW_SIZE = "1920,1080"

# Set headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size={}".format(WINDOW_SIZE))

driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)

# Specify URL
URL = "https://google.com"
OUT = "mygrab.png"

# Launch Selenium
driver.get(URL)
screenshot = driver.save_screenshot(OUT)
driver.quit()
