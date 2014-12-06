#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

row_counter = 0
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		for row in filereader:
			if row_counter < 3:
				pass
			elif row_counter > 15:
				pass
			else:
				print map(string.strip,row)
				#filewriter.writerow(map(string.strip,row))
			row_counter += 1