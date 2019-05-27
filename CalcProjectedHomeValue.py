#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectedHomeValue(CalcBase):

	def _enumrate_inputcf(self):
		return ['CPI_monthly']


	def _enumrate_outputcf(self):
		return ['projected_HomeValue']



	def calculate(self, assumption):

		for m in range(len(self.cfdic['projected_HomeValue'])):
			if m == 0:
				self.cfdic['projected_HomeValue'][m] = assumption['ap_home_value']
			else:
				self.cfdic['projected_HomeValue'][m] = self.cfdic['projected_HomeValue'][m - 1] * (1 + self.cfdic['CPI_monthly'][m])







