#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import re
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

input_file = sys.argv[1]
#output_file = sys.argv[2]

regexp = re.compile(r'(?P<my_pattern>^J.*)', re.I)
with open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		worksheet = workbook.sheet_by_name('january_2013')
		for row_index in range(worksheet.nrows):
			output = []
			if row_index > 0:
				result = regexp.search(worksheet.cell_value(row_index,1))
				if result == None:
					pass
				else:
					for col_index in range(worksheet.ncols):
						if col_index < 4:
							cell = worksheet.cell_value(row_index,col_index)
							output.append(cell)
						else:
							cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index),workbook.datemode)
							cell = date(*cell[0:3]).strftime('%m/%d/%Y')
							output.append(cell)
					print output
					#filewriter.writerow(output)
			else:
				print worksheet.row_values(row_index)
				#filewriter.writerow(worksheet.row_values(row_index))
