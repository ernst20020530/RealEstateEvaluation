#!/usr/bin/python3


from CalcBase import CalcBase
import numpy as np


class CalcProjectedRent(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedRent, self).__init__('CalcProjectedRent', dumpCF)

	def _enumrate_inputcf(self):
		return ['CPI_monthly','projected_OccupiedMonth', 'projected_tenant_search_month']

	def _enumrate_outputcf(self):
		return ['projected_rent']


	def calculate(self, assumption):

		for m in range(len(self.cfdic['projected_rent'])):
			if m == 0:
				self.cfdic['projected_rent'][m] = assumption['ap_rent']
			else:
				self.cfdic['projected_rent'][m] = self.cfdic['projected_rent'][m - 1] * (1 + self.cfdic['CPI_monthly'][m])

		projected_OccupiedMonth 		= np.array(self.cfdic['projected_OccupiedMonth'])
		projected_tenant_search_month 	= np.array(self.cfdic['projected_tenant_search_month'])
		projected_rent					= np.array(self.cfdic['projected_rent'])

		projected_mergeMonth 	= np.add(projected_OccupiedMonth,projected_tenant_search_month)
		projected_rent			= np.multiply(projected_rent,projected_mergeMonth)
		print(projected_mergeMonth)

		self.cfdic['projected_rent'] = projected_rent.tolist()





