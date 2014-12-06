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

row_counter = 0
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for row in filereader:
			print row
			#filewriter.writerow(row)
			row_counter += 1
print 'Number of rows: %d' % (row_counter)
