#!/usr/bin/python3


import numpy as np


class CoreModel:

	def __init__(self, total_term):

		#self.cfdic = { name: np.zeros(total_term) for name in CoreModel.cf_names}
		self.cfdic = { name: [0]*total_term for name in CoreModel.cf_names}
		self.total_term = total_term


#	def dumpcf(self, filename, cfname = []):
#
#		with open(filename, 'w') as f:
#
#			fields = list(self.cfdic.keys())
#			fields = ['month'] + fields[:]
#			f.write(','.join(fields))
#			f.write('\n')
#
#
#			allcf = [v for v in self.cfdic.values()]
#			allcf = np.array(allcf)
#
#			for m in range(self.total_term):
#				tmp = [str(e) for e in allcf[:,m]]
#				strmonth = ','.join(tmp)
#				strmonth = '{0},{1}\n'.format(str(m),strmonth)
#				f.write(strmonth)

	def dumpcf(self, filename, cfname = []):

		fields = list(self.cfdic.keys())
		if len(cfname) != 0:
			fields = list(filter(l))
			

		with open(filename, 'w') as f:

			fields = list(self.cfdic.keys())
			fields = ['month'] + fields[:]
			f.write(','.join(fields))
			f.write('\n')


			allcf = [v for v in self.cfdic.values()]
			allcf = np.array(allcf)

			for m in range(self.total_term):
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

	cm = CoreModel(360)
	cm.dumpcf('cf.csv')


