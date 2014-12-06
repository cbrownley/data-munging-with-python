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

important_dates = ['2/17/14','2/24/14']
header_row = True
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for row in filereader:
			if not header_row:
				cost = row[3].strip('$').replace(',','')
				if float(cost) < 200.0 or row[4] in important_dates:
					print row
					#filewriter.writerow(row)
				else:
					pass
			else:
				print row
				#filewriter.writerow(row)
				header_row = False