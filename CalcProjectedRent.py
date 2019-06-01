#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectedRent(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedRent, self).__init__('CalcProjectedRent', dumpCF)

	def _enumrate_inputcf(self):
		return ['CPI_monthly','projected_OccupiedMonth']

	def _enumrate_outputcf(self):
		return ['projected_rent']


	def calculate(self, assumption):

		for m in range(len(self.cfdic['projected_rent'])):
			if m == 0:
				self.cfdic['projected_rent'][m] = assumption['ap_rent']
			else:
				self.cfdic['projected_rent'][m] = self.cfdic['projected_rent'][m - 1] * (1 + self.cfdic['CPI_monthly'][m])
		#for m in range(len(self.cfdic['projected_rent'])):
		#	self.cfdic['projected_rent'][m] *= self.cfdic['projected_OccupiedMonth'][m]





