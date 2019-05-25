#!/usr/bin/python3


import numpy as np
from CalcBase import CalcBase
from MortgageCalc import MortgageCalc


class CoreModel:

	def __init__(self, assumption):

		self.total_term = assumption['total_term']
		self.cfdic = { name: [0]*(self.total_term+1) for name in CoreModel.cf_names}
		self.assumption = assumption

		self.calc_list = [MortgageCalc()]

	def run(self):

		for c in self.calc_list:
			c.inputcf(self.cfdic, self.assumption)
			c.calculate(self.assumption)
			c.outputcf(self.cfdic)


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
				'effective_rent',
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

	assumption = {	'ap_note_rate'				: 0.05375,
					'total_term'				: 360,
					'ap_home_price'				: 77900,
					'ap_downpay_ratio' 			: 0.2,
					'ap_CPI' 					: 0.02,
					'ap_insurance' 				: -28,
					'ap_rent' 					: 1100,
					'ap_home_value' 			: 77125,
					'ap_hoa' 					: -297,
					'ap_tax_assessments' 		: 46117,
					'ap_tax' 					: -994,
					'ap_monthly_mgt_fee_ratio' 	: 0.05,
					'ap_vacancy_ratio' 			: 0.083333}

	cm = CoreModel(assumption)
	cm.run()
	cm.dumpcf('cf.csv',['upb','int','principal','pmt'])
	#cm.dumpcf('cf.csv')


