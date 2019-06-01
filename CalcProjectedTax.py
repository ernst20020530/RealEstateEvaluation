#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectedTax(CalcBase):

	def _enumrate_inputcf(self):
		return ['projected_tax_assessment']

	def _enumrate_outputcf(self):
		return ['tax_ratio','projected_tax']

	
	def calculate(self, assumption):
		
		for m in range(len(self.cfdic['tax_ratio'])):
			self.cfdic['tax_ratio'][m] = abs(assumption['ap_tax'] / assumption['ap_tax_assessments'])/12
			self.cfdic['projected_tax'][m] = -self.cfdic['projected_tax_assessment'][m] * self.cfdic['tax_ratio'][m]






