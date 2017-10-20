from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
import time
import login

driver = login.login()
while True:
        likeButtons = driver.find_elements_by_css_selector('.coreSpriteHeartOpen')
        for likeButton in likeButtons:
                try:
                        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", likeButton)
                        likeButton.click()
                except StaleElementReferenceException:
                        pass
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
driver.close()

