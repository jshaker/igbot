import sys
import login
import feed
import time
import getpass
import navigate
import modal

username = raw_input('Username: ')
password = getpass.getpass('Password: ')
driver = login.login(username, password)
tag = raw_input('What tag would you like to navigate to?')
navigate.tag(driver, tag)
modal.open(driver)
while True:
	try:
		modal.like(driver)
	except Exception as e:
		print e.__doc__
		print e.message
		navigate.tag(driver, tag)
		modal.open(driver)		
	time.sleep(3)
