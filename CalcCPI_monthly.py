#!/usr/bin/python3


from CalcBase import CalcBase


class CalcCPI_monthly(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcCPI_monthly, self).__init__('CalcCPI_monthly', dumpCF)


	def _enumrate_outputcf(self):
		return ['CPI_monthly']


	def calculate(self, assumption):
		for m in range(len(self.cfdic['CPI_monthly'])):
			self.cfdic['CPI_monthly'][m] = assumption['ap_CPI']/12








