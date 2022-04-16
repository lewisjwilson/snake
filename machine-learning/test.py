from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# chromedriver in /usr/bin (if incompatible,
# download from https://chromedriver.chromium.org/home)
# for your current version of Chrome

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/game/index.html')

gb = driver.find_element(by=By.ID, value="game-board")
food = gb.find_element(by=By.CLASS_NAME, value="food")
print(food.get_attribute("style"))
