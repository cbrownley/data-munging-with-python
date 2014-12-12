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
my_columns = ['Customer Name', 'Sale Amount']
with xlrd.open_workbook(input_file) as workbook:
	#with open(output_file, 'wb') as csv_out_file:
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for worksheet in workbook.sheets():
			if not first_worksheet:
				header = worksheet.row_values(0)
				for row_index in range(1,worksheet.nrows):
					row_list_output = [ ]
					for column_index in range(len(header)):
						if header[column_index] in my_columns:
							row_list_output.append(worksheet.cell_value(row_index, column_index))
					print row_list_output
					#filewriter.writerow(row_list_output)
			else:
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
							row_list_output.append(worksheet.cell_value(row_index, column_index))
					print row_list_output
					#filewriter.writerow(row_list_output)
				first_worksheet = False