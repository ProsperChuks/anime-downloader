from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://gogoanime.so")
driver.implicitly_wait(10)
PARENT_TAB = driver.current_window_handle

driver.quit()
