# Code from geeksforgeeks.org
# https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
import re

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def check(Ip):

	if(re.search(regex, Ip)):
		return True

	else:
		return False
