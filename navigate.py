def explore(driver):
	driver.get("https://www.instagram.com/explore/")
	driver.implicitly_wait(10)
	driver.find_element_by_css_selector("h2")

def tag(driver):
	tag = raw_input('What tag would you like to navigate to?')
	driver.get("https://www.instagram.com/explore/tags/"+tag)
	driver.implicitly_wait(10)
	driver.find_element_by_css_selector("h2")

