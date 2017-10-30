from multiprocessing.dummy import Pool as ThreadPool
import sys
import getpass
import automate
import itertools

def strip(str):
        return str.strip()

username = input('Username: ')
password = getpass.getpass('Password: ')
tagsString = input('What tag(s) would you like to navigate to?')
tags = list(map(strip, tagsString.split(',')))
count = len(tags)
pool = ThreadPool(count)
pool.starmap(automate.automate, zip(itertools.repeat(username),itertools.repeat(password), tags))
