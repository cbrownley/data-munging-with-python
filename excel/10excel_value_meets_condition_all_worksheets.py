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

first_worksheet = True
with xlrd.open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for worksheet in workbook.sheets():
			if not first_worksheet:
				for row_index in range(1,worksheet.nrows):
					amount = worksheet.cell_value(row_index,3)
					if amount > 1700.0:
						print worksheet.row_values(row_index)
						#filewriter.writerow(worksheet.row_values(row_index))
					else:
						pass
			else:	
				for row_index in range(worksheet.nrows):
					if row_index > 0:
						amount = worksheet.cell_value(row_index,3)
						if amount > 1700.0:
							print worksheet.row_values(row_index)
							#filewriter.writerow(worksheet.row_values(row_index))
						else:
							pass
					else:
						print worksheet.row_values(row_index)
						#filewriter.writerow(worksheet.row_values(row_index))
				first_worksheet = False