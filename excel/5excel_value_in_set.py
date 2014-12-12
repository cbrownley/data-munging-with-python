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

important_dates = ['01/24/2013','01/31/2013']
with open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		worksheet = workbook.sheet_by_name('january_2013')
		for row_index in range(worksheet.nrows):
			output = []
			if row_index > 0:
				cell = xldate_as_tuple(worksheet.cell_value(row_index,4),workbook.datemode)
				cell = str(date(*cell[0:3]).strftime('%m/%d/%Y'))
				if cell in important_dates:
					for col_index in range(worksheet.ncols):
						if col_index < 4:
							cell = worksheet.cell_value(row_index,col_index)
							output.append(cell)
						else:
							cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index),workbook.datemode)
							cell = str(date(*cell[0:3]).strftime('%m/%d/%Y'))
							output.append(cell)
					print output
					#filewriter.writerow(output)
				else:
					pass
			else:
				print worksheet.row_values(row_index)
				#filewriter.writerow(worksheet.row_values(row_index))