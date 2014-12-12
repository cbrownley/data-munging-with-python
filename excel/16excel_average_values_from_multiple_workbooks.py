#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import glob
import os
import sys
import xlrd

input_directory = sys.argv[1]
#output_file = sys.argv[2]

for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
	with xlrd.open_workbook(input_file) as workbook:
		#with open(output_file, 'ab') as csv_out_file:
			#filewriter = csv.writer(csv_out_file, delimiter=',')
			for worksheet in workbook.sheets():
				total_sales = 0
				number_of_values = 0
				output_list = [ ]
				output_list.append(os.path.basename(input_file))
				output_list.append(worksheet.name)
				for row_index in range(1,worksheet.nrows):
					try:
						total_sales += worksheet.cell_value(row_index,3)
						number_of_values += 1
					except:
						total_sales += 0
						number_of_values += 0
				average_sales = '%.2f' % (total_sales / float(number_of_values))
				output_list.append(average_sales)
				print output_list
				#filewriter.writerow(output_list)