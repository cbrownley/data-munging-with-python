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

first_workbook = True
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
	print os.path.basename(input_file)
	with xlrd.open_workbook(input_file) as workbook:
		#with open(output_file, 'ab') as csv_out_file:
			#filewriter = csv.writer(csv_out_file, delimiter=',')
			if not first_workbook:
				for worksheet in workbook.sheets():
					for row_index in range(1,worksheet.nrows):
						print worksheet.row_values(row_index)
						#filewriter.writerow(worksheet.row_values(row_index))
			else:
				first_worksheet = True
				for worksheet in workbook.sheets():
					if not first_worksheet:
						for row_index in range(1,worksheet.nrows):
							print worksheet.row_values(row_index)
							#filewriter.writerow(worksheet.row_values(row_index))
					else:
						for row_index in range(worksheet.nrows):
							print worksheet.row_values(row_index)
							#filewriter.writerow(worksheet.row_values(row_index))
						first_worksheet = False
				first_workbook = False