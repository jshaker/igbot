def explore(driver):
	url = "https://www.instagram.com/explore/"
	driver.get(url)
	driver.implicitly_wait(10)
	driver.find_element_by_css_selector("h2")
	return url

def tag(driver, tag):
	url = "https://www.instagram.com/explore/tags/" + tag
	driver.get(url)
	driver.implicitly_wait(10)
	driver.find_element_by_css_selector("h2")
	return url
