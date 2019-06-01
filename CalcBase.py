#!/usr/bin/python3


import numpy as np

class CalcBase:

	def __init__(self, name, dumpCF):

		self.cfdic 	= {}
		self.name	= name
		self.dumpCF = dumpCF

	def dump(self, assumption):
		if self.dumpCF == False:
			return

		fields = self._enumrate_inputcf() + self._enumrate_outputcf()
		allcf = [self.cfdic[n] for n in fields]
		allcf = np.array(allcf)

		with open('{0}.csv'.format(self.name), 'w') as f:
			fields = ['month'] + fields[:]
			f.write(','.join(fields))
			f.write('\n')
			
			for m in range(assumption['total_term'] + 1):
				tmp = [str(e) for e in allcf[:,m]]
				strmonth = ','.join(tmp)
				strmonth = '{0},{1}\n'.format(str(m),strmonth)
				f.write(strmonth)


	def inputcf(self, cfdic, assumption):
		inputcf_name = self._enumrate_inputcf()
		for n in inputcf_name:
			self.cfdic[n] = cfdic[n]
		outputcf_name = self._enumrate_outputcf()
		for n in outputcf_name:
			if n not in inputcf_name:
				self.cfdic[n] = [0]*(assumption['total_term'] + 1)


	def _enumrate_inputcf(self):
		return []


	def outputcf(self, cfdic):
		outputcf_name = self._enumrate_outputcf()
		for n in outputcf_name:
			print(n)
			cfdic[n] = self.cfdic[n]


	def _enumrate_outputcf(self):
		return []


	def calculate(self, assumption):

		pass


