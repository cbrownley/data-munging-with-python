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
my_sheets = [0,1]
with xlrd.open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for sheet_index in range(workbook.nsheets):
			if sheet_index in my_sheets:
				if not first_worksheet:
					for row_index in range(1,workbook.sheet_by_index(sheet_index).nrows):
						amount = workbook.sheet_by_index(sheet_index).cell_value(row_index,3)
						if amount > 1900.0:
							print workbook.sheet_by_index(sheet_index).row_values(row_index)
							#filewriter.writerow(workbook.sheet_by_index(sheet_index).row_values(row_index))
						else:
							pass
				else:
					for row_index in range(workbook.sheet_by_index(sheet_index).nrows):
						if row_index > 0:
							amount = workbook.sheet_by_index(sheet_index).cell_value(row_index,3)
							if amount > 1900.0:
								print workbook.sheet_by_index(sheet_index).row_values(row_index)
								#filewriter.writerow(workbook.sheet_by_index(sheet_index).row_values(row_index))
							else:
								pass
						else:
							print workbook.sheet_by_index(sheet_index).row_values(row_index)
							#filewriter.writerow(workbook.sheet_by_index(sheet_index).row_values(row_index))
					first_worksheet = False