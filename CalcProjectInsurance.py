#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectInsurance(CalcBase):

	def _enumrate_inputcf(self):
		return ['CPI_monthly']

	def _enumrate_outputcf(self):
		return ['projected_Insurance']


	def calculate(self, assumption):

		for m in range(len(self.cfdic['projected_Insurance'])):
			if m == 0:
				self.cfdic['projected_Insurance'][m] = assumption['ap_insurance']
			else:
				self.cfdic['projected_Insurance'][m] = self.cfdic['projected_Insurance'][m - 1] * (1 + self.cfdic['CPI_monthly'][m])










