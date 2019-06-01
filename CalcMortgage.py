#!/usr/bin/python3


import numpy as np

from CalcBase import CalcBase



class CalcMortgage(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcMortgage, self).__init__('CalcMortgage', dumpCF)

	def _enumrate_inputcf(self):
		return []


	def _enumrate_outputcf(self):
		return ['int','upb','note_rate_bymonth','pmt','principal']

	def calculate(self, assumption):
		
		self.cfdic['upb'][0] = (1 - assumption['ap_downpay_ratio']) * assumption['ap_home_price']

		note_rate_permonth = assumption['ap_note_rate']/12

		#calculate payment
		for m in range(1, assumption['total_term']+1):
			self.cfdic['pmt'][m] = np.pmt(note_rate_permonth, assumption['total_term'], self.cfdic['upb'][0], 0, 0)

		#calculate interest
		int = np.ipmt(note_rate_permonth, np.arange(360) + 1, 360, self.cfdic['upb'][0], 0)
		self.cfdic['int'] = np.array([0] + int.tolist())

		#calculate principal
		prn = np.ppmt(note_rate_permonth, np.arange(360) + 1, 360, self.cfdic['upb'][0], 0)
		self.cfdic['principal'] = np.array([0] + prn.tolist())

		for m in range(1, assumption['total_term']+1):
			self.cfdic['upb'][m] = self.cfdic['upb'][m - 1] + self.cfdic['principal'][m]






