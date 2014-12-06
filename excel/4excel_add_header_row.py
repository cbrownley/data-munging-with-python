#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import sys
from string import strip
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

input_file = sys.argv[1]
#output_file = sys.argv[2]

with open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		header_list = ['Customer ID','Customer Name','Invoice Number','Sale Amount','Purchase Date']
		print header_list
		#filewriter.writerow(header_list)
		worksheet = workbook.sheet_by_name('january_2013')
		for row_index in range(worksheet.nrows):
			row_of_output = []
			for column_index in range(worksheet.ncols):
				if column_index < 4:
					cell_value = str(worksheet.cell_value(row_index,column_index)).strip()
					row_of_output.append(cell_value)
				else:
					cell_value = xldate_as_tuple(worksheet.cell(row_index, column_index).value,workbook.datemode)
					cell_value = str(date(*cell_value[0:3]).strftime('%m/%d/%Y')).strip()
					row_of_output.append(cell_value)
			print row_of_output
			#filewriter.writerow(row_of_output)