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
navigate.tag(driver)
modal.open(driver)
while True:
	modal.like(driver)
	time.sleep(3)
