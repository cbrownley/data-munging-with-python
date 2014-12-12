#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

my_columns = ['Invoice Number', 'Purchase Date']
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		header = next(filereader, None)
		header_list_output = [ ]
		for index_value in range(len(header)):	
			if header[index_value] in my_columns:
				header_list_output.append(header[index_value])
		print header_list_output
		#filewriter.writerow(header_list_output)
		for row in filereader:
			row_list_output = [ ]
			for index_value in range(len(header)):
				if header[index_value] in my_columns:
					row_list_output.append(row[index_value])
			print row_list_output
			#filewriter.writerow(row_list_output)