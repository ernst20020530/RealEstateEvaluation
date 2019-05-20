#!/usr/bin/python3

import re

if __name__=='__main__':

	#abc = 'gu ru 99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
	abc = '8722 Thornwood Ln, TAMPA, FL 33615'
	#emails = re.findall(r'[\w\s*]+@[\w\.-]+', abc)
	emails = re.findall(r'\d+[\s+\w+]+,\s*\w+,\s*\w+\s*\d{5}', abc)
	for email in emails:
		print(email)

