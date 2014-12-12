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

with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		header_list = [ ]
		for number in range(1, 6):
			header_list.append('Var'+str(number))
		print header_list
		#filewriter.writerow(header_list)
		for row in filereader:
			print row
			#filewriter.writerow(row)