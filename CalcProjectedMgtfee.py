#!/usr/bin/python3


from CalcBase import CalcBase
import numpy as np


class CalcProjectedMgtfee(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedMgtfee, self).__init__('CalcProjectedMgtfee', dumpCF)

	def _enumrate_inputcf(self):
		return ['projected_rent','projected_OccupiedMonth_ratio','projected_tenant_search_month_ratio']

	def _enumrate_outputcf(self):
		return ['projected_mgtfee','projected_tenant_searchfee']


	def calculate(self, assumption):

		projected_rent = np.array(self.cfdic['projected_rent'])	
		projected_tenant_search_month_ratio = np.array(self.cfdic['projected_tenant_search_month_ratio'])	
		projected_tenant_searchfee = np.negative(np.multiply(projected_rent, projected_tenant_search_month_ratio))
		self.cfdic['projected_tenant_searchfee'] = projected_tenant_searchfee.tolist()
		
		projected_OccupiedMonth_ratio = np.array(self.cfdic['projected_OccupiedMonth_ratio'])
		projected_mgtfee = np.negative(np.multiply(projected_rent, projected_OccupiedMonth_ratio))
		self.cfdic['projected_mgtfee'] = projected_mgtfee.tolist()


