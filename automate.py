import login
import time
import navigate
import modal

def automate_tags(username, password, delay, tag):
	driver = login.login(username, password)
	navigate.tag(driver, tag)
	modal.open_tags(driver)
	while True:
		try:
			modal.follow(driver)
			modal.next(driver)
		except Exception as e:
			print(e.__doc__)
			print(e.message)
			navigate.tag(driver, tag)
			modal.open(driver)
		time.sleep(delay)

def automate_explore(username, password, delay):
	driver = login.login(username, password)
	navigate.explore(driver)
	modal.open_explore(driver)
	while True:
		try:
			modal.follow(driver)
			modal.like(driver)
		except Exception as e:
			print(e.__doc__)
			print(e.message)
			nagivate.explore(driver)
			modal.open(driver)
		time.sleep(delay)
