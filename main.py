from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://gogoanime.so")
PARENT_TAB = driver.current_window_handle

def homepage(self):
    self.locator = "keyword"

def searchresults(self):
    self.locator = "One Piece"

def animepage(self):
    self.locator = "//ul[@id='episode_related']/li/a/div[@class='name']"

def downloadPage1(self):
    self.locator = "//ul/li[@class='downloads']/a"

def downloadPage2(self):
    self.locator = "Download(360P - mp4)"

driver.quit()
