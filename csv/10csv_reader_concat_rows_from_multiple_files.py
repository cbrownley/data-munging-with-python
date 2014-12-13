#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	print os.path.basename(input_file)
	with open(input_file, 'rU') as csv_in_file:
		with open(output_file, 'ab') as csv_out_file:
			filereader = csv.reader(csv_in_file, delimiter=',')
			filewriter = csv.writer(csv_out_file, delimiter=',')
			if not first_file:
				header = next(filereader, None)
				for row in filereader:
					print row
					filewriter.writerow(row)
			else:
				for row in filereader:
					print row
					filewriter.writerow(row)
				first_file = False