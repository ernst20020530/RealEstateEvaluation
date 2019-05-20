#!/usr/bin/python3

import requests
import re


class ScaleSearch:

	def __init__(self, zipcode):
		self.url = ScaleSearch.URLTemplate.format(zipcode)
		print(self.url)

	def do(self):
		res = ''
		for i in range(5):
			response = requests.get(self.url, headers=ScaleSearch.get_headers())
			if response.status_code != 200:
				print('URL response failed\n code:{0}\t URL:{1}'.format(response.status_code, self.url))
			else:
				res = response.text
				break
		else:
			print('Fail to get data from Web {0}'.format(self.url))
			return []

		s = set()
		for regex in ScaleSearch.AddressRegex:
			s= s.union(set(re.findall(regex,res)))

		return list(s)


	def get_headers():
		# Creating headers.
		headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'accept-encoding': 'gzip, deflate, sdch, br',
					'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
					'cache-control': 'max-age=0',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
		return headers


	URLTemplate	= 'https://www.redfin.com/zipcode/{0}/filter/max-price=100k'

	AddressRegex = ['\d+[\s+\w+]+,[\s*\w+]+,\s*[a-zA-Z]+\s*\d{5}',
					'\d+[\s+\w+]+\s\#\d+,[\s*\w+]+,\s*[a-zA-Z]+\s*\d{5}']

