#!/usr/bin/python3


from CalcBase import CalcBase
import numpy as np


class CalcProjectedNetCF(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedNetCF, self).__init__('CalcProjectedNetCF', dumpCF)

	def _enumrate_inputcf(self):
		return ['pmt',
				'projected_rent',
				'projected_HOA',
				'projected_Insurance',
				'projected_tax',
				'projected_mgtfee',
				'projected_tenant_searchfee']

	def _enumrate_outputcf(self):
		return ['projected_NetCF']

	def calculate(self, assumption):
		
		pmt 						= np.array(self.cfdic['pmt'])
		projected_rent 				= np.array(self.cfdic['projected_rent'])
		projected_HOA 				= np.array(self.cfdic['projected_HOA'])
		projected_Insurance 		= np.array(self.cfdic['projected_Insurance'])
		projected_tax 				= np.array(self.cfdic['projected_tax'])
		projected_mgtfee 			= np.array(self.cfdic['projected_mgtfee'])
		projected_tenant_searchfee 	= np.array(self.cfdic['projected_tenant_searchfee'])

		projected_NetCF = pmt
		projected_NetCF = np.add(projected_NetCF, projected_rent)
		projected_NetCF = np.add(projected_NetCF, projected_HOA)
		projected_NetCF = np.add(projected_NetCF, projected_Insurance)
		projected_NetCF = np.add(projected_NetCF, projected_tax)
		projected_NetCF = np.add(projected_NetCF, projected_mgtfee)
		projected_NetCF = np.add(projected_NetCF, projected_tenant_searchfee)
		self.cfdic['projected_NetCF'] = projected_NetCF.tolist()














