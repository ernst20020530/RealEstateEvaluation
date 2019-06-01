#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectedHOA(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedHOA, self).__init__('CalcProjectedHOA', dumpCF)

	def _enumrate_inputcf(self):
		return ['CPI_monthly']

	def _enumrate_outputcf(self):
		return ['projected_HOA']


	def calculate(self, assumption):

		for m in range(len(self.cfdic['projected_HOA'])):
			if m == 0:
				self.cfdic['projected_HOA'][m] = assumption['ap_hoa']
			else:
				self.cfdic['projected_HOA'][m] = self.cfdic['projected_HOA'][m - 1] * (1 + self.cfdic['CPI_monthly'][m])











