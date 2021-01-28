from selenium import webdriver

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://gogoanime.so")
PARENT_TAB = driver.current_window_handle

driver.quit()
