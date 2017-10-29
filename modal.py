from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
import sys

def open(driver):
	anchor = driver.find_element_by_css_selector("a")
	anchor.click()

def like(driver):
        likeButton = driver.find_element_by_css_selector(".coreSpriteHeartOpen")
	likeButton.click()
	nextButton = driver.find_element_by_css_selector(".coreSpriteRightPaginationArrow")
	nextButton.click()
