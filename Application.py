#!/usr/bin/python3


import requests
import csv
import xml.etree.ElementTree as ET
import ScaleSearch as ScaleSearch

from Address import Address


class APIConnector:
	
	def __init__(self, addr):
		self.ZILLOW_token 	= ''
		self.addr			= addr

		with open(APIConnector.ZILLOW_token_path) as f:
			IEX_token_list = f.readlines()
			if len(IEX_token_list) != 0:
				self.ZILLOW_token = IEX_token_list[0].rstrip()
		


	def Get(self):

		url = self.__FormURL('GetDeepSearchResults.htm')
		if url == '':
			return {}
		print(url)

		res = requests.get(url)
		root = ET.fromstring(res.content)
		return {elem.tag: elem.text for elem in root.iter()}


	def __FormURL(self, endpoint):
		if addr.IsValid() == False:
			return ''

		tokens = [APIConnector.baseURL,endpoint]
		url_encoding = '/'.join(tokens)

		print(url_encoding)

		param = [	'zws-id='+self.ZILLOW_token,
					'address='+self.addr.encodeAddress(),
					'citystatezip='+addr.encodeCity()]
		param_encoding = '&'.join(param)
		print(param_encoding)

		url_encoding = '?'.join([url_encoding,param_encoding])
		return url_encoding

	baseURL				= 'http://www.zillow.com/webservice'
	ZILLOW_token_path	= '/home/ernst/.ssh/ZILLOW'



def write_data(output_filename,data_list):

	if data_list == None or len(data_list) == 0 or output_filename == None:
		return

	print('='*100)
	print('WRITE DATA')

	fieldlist = []
	for d in data_list:
		fieldlist = fieldlist[:] + list(d.keys())

	s = set(fieldlist)
	print('R'*100)
	print(s)
		

	with open(output_filename, 'w') as f:
		fieldnames = data_list[0].keys()
		print(fieldnames)
		spamwriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
		spamwriter.writeheader()
		for d in data_list:
			print(d)
			spamwriter.writerow(d)



if __name__=='__main__':


	ss = ScaleSearch.ScaleSearch('33543')
	searchList = ss.do()
	if len(searchList) == 0:
		print('failed to search')

	
	data_pool = []
	for target in searchList:
		addr = Address(target)
		data = APIConnector(addr).Get()
		if len(data) == 0:
			continue
		data_pool.append(data)

	for d in data_pool:
		print('-'*100)
		#print('NUM keys {0}: {1}'.format(d['zpid'],len(d)))
		print('NUM keys {0}'.format(len(d)))

	write_data('zipcode_33615.csv', data_pool)
















