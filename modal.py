from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
import sys

def open(driver):
	anchor = driver.find_element_by_css_selector("a")
	anchor.click()

def like(driver):
	try:
		likeButton = driver.find_element_by_css_selector(".coreSpriteHeartOpen")
		likeButton.click()
	except:
		next(driver)

def next(driver):
	nextButton = driver.find_element_by_css_selector(".coreSpriteRightPaginationArrow")
	nextButton.click()

def follow(driver):
	try:
		followButton = driver.find_element_by_css_selector("button")
		if (followButton.text == 'Follow'):
			followButton.click()
	except:
		next(driver)
