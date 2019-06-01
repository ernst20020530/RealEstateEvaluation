#!/usr/bin/python3


import numpy as np
from CalcBase import CalcBase
from CalcMortgage import CalcMortgage
from CalcProjectedRent import CalcProjectedRent
from CalcCPI_monthly import CalcCPI_monthly
from CalcProjectedHomeValue import CalcProjectedHomeValue
from CalcProjectedHOA import CalcProjectedHOA
from CalcProjectInsurance import CalcProjectInsurance
from CalcProjectedTaxAssessment import CalcProjectedTaxAssessment
from CalcProjectedTax import CalcProjectedTax
from CalcProjectedMgtfee import CalcProjectedMgtfee
from CalcProjectedOccupiedMonth import CalcProjectedOccupiedMonth
from CalcProjectedNetCF import CalcProjectedNetCF
from CalcIRR import CalcIRR



class CoreModel:

	def __init__(self, assumption):

		self.total_term = assumption['total_term']
		#self.cfdic = { name: [0]*(self.total_term+1) for name in CoreModel.cf_names}
		self.cfdic = {}
		self.assumption = assumption

		self.calc_list = [	CalcCPI_monthly(),
							CalcMortgage(),
							CalcProjectedOccupiedMonth(),
							CalcProjectedRent(),
							CalcProjectedHomeValue(),
							CalcProjectedHOA(),
							CalcProjectInsurance(),
							CalcProjectedTaxAssessment(),
							CalcProjectedTax(),
							CalcProjectedMgtfee(),
							CalcProjectedNetCF(True),
							CalcIRR(True)]

	def run(self):

		for c in self.calc_list:
			c.inputcf(self.cfdic, self.assumption)
			c.calculate(self.assumption)
			c.outputcf(self.cfdic)
			c.dump(self.assumption)


	def dumpcf(self, filename, cfname = []):

		fields = list(self.cfdic.keys())
		if len(cfname) != 0:
			fields = list(filter(lambda x: x in cfname, fields))
			
		allcf = [self.cfdic[n] for n in fields]
		allcf = np.array(allcf)

		with open(filename, 'w') as f:
			fields = ['month'] + fields[:]
			f.write(','.join(fields))
			f.write('\n')

			for m in range(self.total_term + 1):
				tmp = [str(e) for e in allcf[:,m]]
				strmonth = ','.join(tmp)
				strmonth = '{0},{1}\n'.format(str(m),strmonth)
				f.write(strmonth)



	cf_names = ['down_pay',
				'init_cost',
				'upb',
				'note_rate_bymonth',
				'pmt',
				'int',
				'principal',
				'rent',
				'projected_rent',
				'vacant_ratio',
				'cpi_bymonth',
				'home_value',
				'hoa',
				'insurance_ratio',
				'insurance',
				'tax_assessment_ratio',
				'tax_assessment',
				'tax_ratio',
				'tax',
				'mgt_fee']

if __name__=='__main__':

	assumption = {	'ap_note_rate'				: 0.04375,
					'total_term'				: 360,
					'ap_init_cost'				: -4000,
					'ap_home_price'				: 90000,
					'ap_downpay_ratio' 			: 0.2,
					'ap_CPI' 					: 0.02,
					'ap_insurance' 				: -33,
					'ap_rent' 					: 1300,
					'ap_home_value' 			: 92767,
					'ap_hoa' 					: -387,
					'ap_tax_assessments' 		: 55830,
					'ap_tax' 					: -1119,
					'ap_monthly_mgt_fee_ratio' 	: 0.05,
					'ap_tenant_searchfee_ratio'	: 0.5,
					'ap_vacancy_ratio' 			: 0.083333}

	cm = CoreModel(assumption)
	cm.run()
	#cm.dumpcf('cf.csv',['projected_HomeValue','tax_assessment_ratio','projected_tax_assessment','projected_HOA','projected_Insurance','tax_ratio','projected_tax','projected_mgtfee','projected_tenant_searchfee'])
	#cm.dumpcf('cf.csv',['projected_OccupiedMonth','projected_OccupiedMonth_ratio','projected_tenant_search_month','projected_tenant_search_month_ratio','projected_rent','projected_mgtfee','projected_tenant_searchfee'])
	cm.dumpcf('cf.csv',['projected_OccupiedMonth_ratio','projected_tenant_search_month_ratio','projected_rent','projected_mgtfee','projected_tenant_searchfee'])
	#cm.dumpcf('cf.csv')


