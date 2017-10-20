from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.instagram.com")
loginBtn = driver.find_element_by_link_text("Log in")
loginBtn.click()
usernameInput = driver.find_element_by_name("username")
usernameInput.clear()
usernameInput.send_keys("invoyage")
passwordInput = driver.find_element_by_name("password")
passwordInput.clear()
passwordInput.send_keys("1234.com")
passwordInput.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#mainFeed")
while True:
	likeButtons = driver.find_elements_by_css_selector('.coreSpriteHeartOpen')
	for likeButton in likeButtons:
		driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", likeButton)
		likeButton.click()
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(5)
driver.close()
