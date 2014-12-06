#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import sys
import xlrd

input_file = sys.argv[1]
#output_file = sys.argv[2]

my_columns = [1, 3]
with xlrd.open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		worksheet = workbook.sheet_by_name('january_2013')
		for row_index in range(worksheet.nrows):
			row_list_output = [ ]
			for column_index in my_columns:
				row_list_output.append(worksheet.cell_value(row_index,column_index))
			print row_list_output
			#filewriter.writerow(row_list_output)