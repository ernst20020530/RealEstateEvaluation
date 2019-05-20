#!/usr/bin/python3


import requests
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
		print(url)

		res = requests.get(url)
		root = ET.fromstring(res.content)
		print(res.content)
		print('-'*100)
		#print(root)

		print({elem.tag: elem.text for elem in root.iter()})


		#print('-'*100)

		#target = root.find('links')
		#print(target.attrib)
		#print(target)



	def __FormURL(self, endpoint):
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

if __name__=='__main__':


	ss = ScaleSearch.ScaleSearch('33543')
	searchList = ss.do()
	if len(searchList) == 0:
		print('failed to search')

	for target in searchList:
		addr = Address(target)
		print(APIConnector(addr).Get())


