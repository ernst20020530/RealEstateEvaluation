#!/usr/bin/python3


from CalcBase import CalcBase
import numpy as np


class CalcIRR(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcIRR, self).__init__('CalcIRR', dumpCF)

	
	def _enumrate_inputcf(self):
		return ['upb','projected_HomeValue','projected_NetCF']


	def _enumrate_outputcf(self):
		return ['irr','pay_off','sales_price','down_pay','init_cost','irr_cf']

	
	def calculate(self, assumption):
		
		term_max = assumption['total_term']+1
		netcf_mask = np.full((term_max,term_max),0)
		for m in range(term_max):
			for n in range(term_max):
				if m >= n:
					netcf_mask[m,n] = 1
		
		identityM = np.identity(term_max)
		upb		= np.array([self.cfdic['upb'] for m in range(term_max)])
		pay_off	= np.negative(np.multiply(upb, identityM))

		projected_HomeValue		= np.array([self.cfdic['projected_HomeValue'] for m in range(term_max)])
		sales_price				= np.multiply(projected_HomeValue, identityM)

		projected_NetCF = np.array([self.cfdic['projected_NetCF'] for x in range(term_max)])
		projected_NetCF = np.multiply(np.array(netcf_mask),projected_NetCF)

		down_pay_s 		= [0 for x in range(term_max)]
		down_pay_s[0] 	= -assumption['ap_home_price'] * assumption['ap_downpay_ratio']
		down_pay 		= np.array([down_pay_s for x in range(term_max)])


		init_cost_s 	= [0 for x in range(term_max)]
		init_cost_s[0] 	= assumption['ap_init_cost']
		init_cost 		= np.array([init_cost_s for x in range(term_max)])
		
		irr_cf	= init_cost
		irr_cf	= np.add(irr_cf, down_pay)
		irr_cf	= np.add(irr_cf, pay_off)
		irr_cf	= np.add(irr_cf, sales_price)
		irr_cf	= np.add(irr_cf, projected_NetCF)

		irr_monthly = np.array([np.irr(irr_cf[m]) for m in range(term_max)])
		irr = np.multiply(12,irr_monthly)

		m = 180
		self.cfdic['pay_off'] 				= pay_off[m,:].tolist()
		self.cfdic['sales_price'] 			= sales_price[m,:].tolist()
		self.cfdic['down_pay'] 				= down_pay[m,:].tolist()
		self.cfdic['init_cost'] 			= init_cost[m,:].tolist()
		self.cfdic['irr_cf'] 				= irr_cf[m,:].tolist()
		self.cfdic['projected_NetCF'] 		= projected_NetCF[m,:].tolist()
		self.cfdic['irr'] 					= irr.tolist()












