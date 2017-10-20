from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
import time
import init

def login(username, password):
	driver = init.init()
	loginBtn = driver.find_element_by_link_text("Log in")
	loginBtn.click()
	usernameInput = driver.find_element_by_name("username")
	usernameInput.clear()
	usernameInput.send_keys(username)
	passwordInput = driver.find_element_by_name("password")
	passwordInput.clear()
	passwordInput.send_keys(password)
	passwordInput.send_keys(Keys.RETURN)
	driver.implicitly_wait(10)
	driver.find_element_by_css_selector("#mainFeed")
	return driver
