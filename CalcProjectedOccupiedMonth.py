#!/usr/bin/python3

from CalcBase import CalcBase
import numpy as np


class CalcProjectedOccupiedMonth(CalcBase):

	def __init__(self, dumpCF = False):
		super(CalcProjectedOccupiedMonth, self).__init__('CalcProjectedOccupiedMonth', dumpCF)

	def _enumrate_outputcf(self):
		return ['projected_OccupiedMonth',
				'projected_tenant_search_month',
				'projected_OccupiedMonth_ratio',
                'projected_tenant_search_month_ratio']

	def calculate(self, assumption):

		self.cfdic['projected_OccupiedMonth'] = [1 for x in range(len(self.cfdic['projected_OccupiedMonth']))]

		rent_renew_month_idx_list = [m for m in range(1,assumption['total_term']+1)]
		rent_renew_month_idx_list = rent_renew_month_idx_list[::13]
		rent_renew_month_idx_list = [0] + rent_renew_month_idx_list[:]
		for m in rent_renew_month_idx_list:
			self.cfdic['projected_OccupiedMonth'][m] = 0

		projected_OccupiedMonth = np.array(self.cfdic['projected_OccupiedMonth'])

		tenant_search_month_list = [m for m in range(2,assumption['total_term']+1)]
		tenant_search_month_list = tenant_search_month_list[::13]
		for m in tenant_search_month_list:
			#self.cfdic['projected_tenant_search_month'][m] = assumption['ap_tenant_searchfee_ratio']
			self.cfdic['projected_tenant_search_month'][m] = 1

		projected_tenant_search_month = np.array(self.cfdic['projected_tenant_search_month'])
		projected_OccupiedMonth = np.multiply(1-projected_tenant_search_month,projected_OccupiedMonth)
		self.cfdic['projected_OccupiedMonth'] = projected_OccupiedMonth.tolist()
		projected_OccupiedMonth_ratio = projected_OccupiedMonth * assumption['ap_monthly_mgt_fee_ratio']
		self.cfdic['projected_OccupiedMonth_ratio'] = projected_OccupiedMonth_ratio.tolist()

		projected_tenant_search_month_ratio = projected_tenant_search_month * assumption['ap_tenant_searchfee_ratio']
		self.cfdic['projected_tenant_search_month_ratio'] = projected_tenant_search_month_ratio.tolist()





