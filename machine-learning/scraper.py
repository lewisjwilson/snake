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


def snakePos():
    # recursive function in case not fully loaded in DOM
    # gets snek head position (0th element of snek array)
    try:
        element = driver.find_elements(By.CLASS_NAME, 'snake')[0]
        return [styleFormatter(element.get_attribute('style'))[0],
                styleFormatter(element.get_attribute('style'))[1]]
    except:
        # print("Food Element Not Found, trying again")
        return [None, None]


def foodPos():
    # gets food position
    try:
        element = driver.find_elements(By.CLASS_NAME, 'food')[0]
        return [styleFormatter(element.get_attribute('style'))[0],
                styleFormatter(element.get_attribute('style'))[1]]
    except:
        # print("Food Element Not Found, trying again")
        return [None, None]


def styleFormatter(style_string):
    # parses attribute string to get row and col VALUES only
    vals = re.findall("\d+", style_string)
    return vals if len(vals) > 1 else driver.close()


def getRowsAndCols(snek_food_row_col):
    func_switch = {
        "sr": "snakepos",
        "sc": "snakepos",
        "fr": "foodpos",
        "fc": "foodpos",
    }

    row_col_switch = {
        "sr": 0,
        "sc": 1,
        "fr": 0,
        "fc": 1,
    }

    func = func_switch.get(snek_food_row_col)
    row_col = row_col_switch.get(snek_food_row_col)

    count = 0
    recursion_limit = 20

    out = None

    while(out is None):
        if(count < recursion_limit):
            count += 1
            if(func == "snakepos"):
                out = snakePos()[row_col]
            elif (func == "foodpos"):
                out = foodPos()[row_col]
            if(out != None):
                return out
        else:
            sys.exit("Recursion Limit Reached")


# chromedriver in /usr/bin (if incompatible,
# download from https://chromedriver.chromium.org/home)
# for your current version of Chrome
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/game/index.html')

# .5s delay to allow for web page to load elements
time.sleep(1)

# setup actions for sending key presses
# TODO: implement key presses in new file!!
action = ActionChains(driver)
action.send_keys(Keys.UP)
action.perform()

for i in range(50):

    snek_row = getRowsAndCols("sr")
    snek_col = getRowsAndCols("sc")
    food_row = getRowsAndCols("fr")
    food_col = getRowsAndCols("fc")

    print("snek_row: " + snek_row + ", snek_col: " + snek_col +
          "\n food_row: " + food_row + ", food_col: " + food_col)
    time.sleep(0.001)

# used to close the session
driver.close()
