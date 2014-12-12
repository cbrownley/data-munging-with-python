#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import re
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

regexp = re.compile(r'(?P<my_pattern>^001-.*)', re.I)
header_row = True
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for row in filereader:
			if not header_row:
				result = regexp.search(row[1])
				if result == None:
					pass
				else:
					print row
					#filewriter.writerow(row)
			else:
				print row
				#filewriter.writerow(row)
				header_row = False