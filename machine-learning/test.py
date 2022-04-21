# basic imports
import sys
import time
import re

# selenium imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# chromedriver in /usr/bin (if incompatible,
# download from https://chromedriver.chromium.org/home)
# for your current version of Chrome

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/game/index.html')

# .5s delay to allow for web page to load elements
time.sleep(1)


def snakePos():
    # recursive function in case not fully loaded in DOM
    # gets snek head position (0th element of snek array)

    try:
        element = driver.find_elements(By.CLASS_NAME, 'snake')[0]
        return [styleFormatter(element.get_attribute('style'))[0],
                styleFormatter(element.get_attribute('style'))[1]]
    except:
        # print("Food Element Not Found, trying again")
        return None


def foodPos():
    # gets food position

    try:
        element = driver.find_elements(By.CLASS_NAME, 'food')[0]
        return [styleFormatter(element.get_attribute('style'))[0],
                styleFormatter(element.get_attribute('style'))[1]]
    except:
        # print("Food Element Not Found, trying again")
        return None


def styleFormatter(style_string):
    vals = re.findall("\d+", style_string)
    return vals if len(vals) > 1 else driver.close()

    # setup actions for sending key presses
action = ActionChains(driver)
action.send_keys(Keys.UP)
action.perform()

for i in range(50):

    count = 0
    recursion_limit = 20

    snek_row = None
    snek_col = None
    food_row = None
    food_col = None

    # ensure the element exists
    while(snek_row is None):
        if(count < recursion_limit):
            count += 1
            snek_row = snakePos()[0]
        else:
            sys.exit("Recursion Limit Reached")

    count = 0
    while(snek_col is None):
        if(count < recursion_limit):
            count += 1
            snek_col = snakePos()[1]
        else:
            sys.exit("Recursion Limit Reached")

    count = 0
    while(food_row is None):
        if(count < recursion_limit):
            count += 1
            food_row = foodPos()[0]
        else:
            sys.exit("Recursion Limit Reached")

    count = 0
    while(food_col is None):
        if(count < recursion_limit):
            count += 1
            food_col = foodPos()[1]
        else:
            sys.exit("Recursion Limit Reached")

    print("snek_row: " + snek_row +
          "\n food_row: " + food_pos)
    time.sleep(0.001)

# used to close the session
driver.close()
