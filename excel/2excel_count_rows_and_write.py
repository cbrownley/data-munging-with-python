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

row_counter = 0
with xlrd.open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		worksheet = workbook.sheet_by_name('january_2013')
		for row_index in range(worksheet.nrows):
			print worksheet.row_values(row_index)
			#filewriter.writerow(worksheet.row_values(row_index))
			row_counter += 1
print 'Number of rows: %d' % (row_counter)
