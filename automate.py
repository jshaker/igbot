import login
import time
import navigate
import modal

def automate(username, password, tag):
	driver = login.login(username, password)
	navigate.tag(driver, tag)
	modal.open(driver)
	while True:
		try:
			modal.follow(driver)
			modal.next(driver)
		except Exception as e:
			print(e.__doc__)
			print(e.message)
			navigate.tag(driver, tag)
			modal.open(driver)
		time.sleep(30)
