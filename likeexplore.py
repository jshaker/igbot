from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
import time
import login
import sys

if (len(sys.argv) <= 2):
	raise SystemExit
driver = login.login(sys.argv[1], sys.argv[2])
exploreBtn = driver.find_element_by_css_selector(".coreSpriteDesktopNavExplore")
exploreBtn.click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("h2")
article = driver.find_element_by_css_selector("div")
time.sleep(3)
links = article.find_elements_by_css_selector("a")
for _link in links:
	href = _link.get_attribute("href")
	if("explore" in href and "people" not in href):
		link = _link
		break
link.click()
time.sleep(5)
while True:
	likeButton = driver.find_element_by_css_selector(".coreSpriteHeartOpen")
	likeButton.click()
	nextButton = driver.find_element_by_css_selector(".coreSpriteRightPaginationArrow")
	nextButton.click()
	time.sleep(1)
