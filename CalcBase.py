#!/usr/bin/python3


class CalcBase:


	def __init__(self):

		self.cfdic = {}
		

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


