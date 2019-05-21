#!/usr/bin/python3

import re

class Address:

	def __init__(self, num, street, type, city, state):
		self.num	= num
		self.street	= street
		self.type	= type
		self.city	= city
		self.state	= state

	def __init__(self, addrStr):
		self.addrStr	= addrStr
		self.num		= ''
		self.street		= ''
		self.type		= ''
		self.city		= ''
		self.state		= ''

		strTokens = addrStr.split(',')
		strTokens = [t.strip() for t in strTokens]
		if len(strTokens) != 3:
			print('Address {0} does not match expectation'.format(addrStr))
			return

		print(strTokens)

		searchObj = re.search(Address.num_regex, strTokens[0])
		if searchObj == None:
			print('failed to search num')
			return
		self.num	= searchObj.group()
		print(self.num)
		
		searchObj = re.search(Address.street_regex, strTokens[0])
		if searchObj == None:
			print('failed to search street')
			return
		self.street	= searchObj.group()
		print(self.street)

		searchObj = re.search(Address.type_regex, strTokens[0])
		if searchObj == None:
			print('failed to search type')
			return
		self.type =	searchObj.group()
		print(self.type)

		self.city	= strTokens[1]
		self.state	= strTokens[2]

	def IsValid(self):
		if 	len(self.num) 		== 0 or len(self.street) 	== 0 or len(self.type) 		== 0 or len(self.city) 		== 0 or len(self.state) 	== 0:
			print('Property Address Error: {0}'.format(self.addrStr))
			return False
		return True

				


	def encodeAddress(self):
		return '+'.join([self.num, self.street, self.type])

	def encodeCity(self):
		return '+'.join([self.city, self.state])



	num_regex 		= '^\d+'
	street_regex	= '([A-Za-z]+\s)+'
	type_regex		= '\w+$'


if __name__=='__main__':

	a = Address('3024 Piney Bark Dr, Zephyrhills, FL 33543')
	print(a.encodeAddress())
	print(a.encodeCity())

