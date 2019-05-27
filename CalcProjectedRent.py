#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectedRent(CalcBase):

	def _enumrate_inputcf(self):
		return ['CPI_monthly']

	def _enumrate_outputcf(self):
		return ['projected_rent']


	def calculate(self, assumption):

		for m in range(len(self.cfdic['projected_rent'])):
			if m == 0:
				self.cfdic['projected_rent'][m] = assumption['ap_rent'] * (1 - assumption['ap_vacancy_ratio'])
			else:
				self.cfdic['projected_rent'][m] = self.cfdic['projected_rent'][m - 1] * (1 + self.cfdic['CPI_monthly'][m])




