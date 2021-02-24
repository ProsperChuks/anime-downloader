from selenium.webdriver.common.by import By

class homepage():

    search = (By.NAME, "keyword")
    GO = (By.CLASS_NAME, "btngui")

class searchresults():

    result = (By.LINK_TEXT, "One Piece")

class animepage():

    episode = (By.XPATH, "//ul[@id='episode_related']/li/a/div[@class='name']")

class downloadPage():

    DOWNLOAD = (By.XPATH, "//ul/li[@class='dowloads']/a")

class confirmDownload():

    quality = (By.XPATH, ".//div[@class='mirror_link']/div[1]")
