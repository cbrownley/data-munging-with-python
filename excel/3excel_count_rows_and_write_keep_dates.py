#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

input_file = sys.argv[1]
#output_file = sys.argv[2]

with open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		worksheet = workbook.sheet_by_name('january_2013')
		header = worksheet.row_values(0)
		print header
		#filewriter.writerow(header)
		for row_index in range(1, worksheet.nrows):
			row_list_output = []
			for col_index in range(worksheet.ncols):
				if col_index < 4:
					cell = worksheet.cell_value(row_index,col_index)
					row_list_output.append(cell)
				else:
					cell = xldate_as_tuple(worksheet.cell(row_index, col_index).value,workbook.datemode)
					cell = date(*cell[0:3]).strftime('%m/%d/%Y')
					row_list_output.append(cell)
			print row_list_output
			#filewriter.writerow(row_list_output)
		print 'Number of rows: %d' % (worksheet.nrows)
