from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException, WebDriverException
import time
import login
import sys

if (len(sys.argv) <= 2):
	raise SystemExit
driver = login.login(sys.argv[1], sys.argv[2])
while True:
        likeButtons = driver.find_elements_by_css_selector('.coreSpriteHeartOpen')
        for likeButton in likeButtons:
                try:
                        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", likeButton)
                        likeButton.click()
                except (StaleElementReferenceException, WebDriverException):
                        pass
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
driver.close()

