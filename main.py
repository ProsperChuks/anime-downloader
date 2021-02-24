from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locator import *
import time

def main():

    episode_no = 900
    ep = f"EP {episode_no}"
    animeurl = "one-piece"
    
    PATH = 'chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get("https://gogoanime.so")
    driver.implicitly_wait(5)
    PARENT_TAB = driver.current_window_handle

    def download_tab():
        driver.implicitly_wait(5)
        DOWNLOAD_TAB = driver.current_window_handle
        go = driver.find_element(*confirmDownload.quality)
        go.click()
        driver.switch_to.window(DOWNLOAD_TAB)
        go.click()

    search = driver.find_element(*homepage.search)
    search.clear()
    for char in "one piece":
        search.send_keys(char)
        time.sleep(0.15)
    submit = driver.find_element(*homepage.GO)
    submit.click()

    anime_search_result = driver.find_element(*searchresults.result)
    anime_search_result.click()

    for episode in driver.find_elements_by_class_name('name'):
        
        if ep == episode.text:
            driver.get(f'https://gogoanime.so/{animeurl}-episode-{episode_no}')
            break
    
    download = driver.find_element(*downloadPage.DOWNLOAD)
    download.click()

    download_tab()

    time.sleep(5)

if __name__=="__main__":
    main()
