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

my_columns = ['Customer ID', 'Purchase Date']
with open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		worksheet = workbook.sheet_by_name('january_2013')
		header = worksheet.row_values(0)
		header_list_output = [ ]
		for column_index in range(len(header)):	
			if header[column_index] in my_columns:
				header_list_output.append(header[column_index])
		print header_list_output
		#filewriter.writerow(header_list_output)
		for row_index in range(1,worksheet.nrows):
			row_list_output = [ ]
			for column_index in range(len(header)):
				if header[column_index] in my_columns:
					if column_index == 4:
						cell = xldate_as_tuple(worksheet.cell_value(row_index, column_index),workbook.datemode)
						cell = date(*cell[0:3]).strftime('%m/%d/%Y')
						row_list_output.append(cell)
					else:
						row_list_output.append(worksheet.cell_value(row_index, column_index))
			print row_list_output
			#filewriter.writerow(row_list_output)