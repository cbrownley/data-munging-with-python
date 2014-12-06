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

important_dates = ['1/20/14', '1/30/14']
header_row = True
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for row in filereader:
			if not header_row:
				if row[4] in important_dates:
					print row
					#filewriter.writerow(row)
				else:
					pass
			else:
				print row
				#filewriter.writerow(row)
				header_row = False