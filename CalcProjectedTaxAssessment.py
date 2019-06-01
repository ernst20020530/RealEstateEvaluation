#!/usr/bin/python3


from CalcBase import CalcBase


class CalcProjectedTaxAssessment(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedTaxAssessment, self).__init__('CalcProjectedTaxAssessment', dumpCF)

	def _enumrate_inputcf(self):  
		return ['projected_HomeValue'] 

	def _enumrate_outputcf(self):
		return ['tax_assessment_ratio', 'projected_tax_assessment']


	def calculate(self, assumption):

		for m in range(len(self.cfdic['tax_assessment_ratio'])):
			self.cfdic['tax_assessment_ratio'][m] = assumption['ap_tax_assessments'] / assumption['ap_home_value']
			self.cfdic['projected_tax_assessment'][m] = self.cfdic['projected_HomeValue'][m] * self.cfdic['tax_assessment_ratio'][m]







