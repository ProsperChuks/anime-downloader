from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *
import time

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://gogoanime.so")
driver.implicitly_wait(5)
PARENT_TAB = driver.current_window_handle

search = driver.find_element(*homepage.search)
search.clear()
for char in "One Piece":
    search.send_keys(char)
    time.sleep(0.15)
submit = driver.find_element(*homepage.GO)
submit.click()

anime_search_result = driver.find_element(*searchresults.result)
anime_search_result.click()

