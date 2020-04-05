from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get("https://www.google.com")
#chrome_browser.maximize_window()
# search = chrome_browser.find_element_by_class_name()
# search.send_keys("Hello")


chrome_browser.close()

