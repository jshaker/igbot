from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
def init():
	driver = webdriver.Chrome()
        driver.get("http://www.instagram.com")
	return driver
