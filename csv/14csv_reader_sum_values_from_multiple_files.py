#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import glob
import os
import string
import sys

input_path = sys.argv[1]
#output_file = sys.argv[2]

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	with open(input_file, 'rU') as csv_in_file:
		#with open(output_file, 'ab') as csv_out_file:
			filereader = csv.reader(csv_in_file, delimiter=',')
			#filewriter = csv.writer(csv_out_file, delimiter=',')
			output_list = [ ]
			output_list.append(os.path.basename(input_file))
			header = next(filereader, None)
			total_cost = 0
			for row in filereader:
				total_cost += float(row[3].strip('$').replace(',',''))
			output_list.append(total_cost)
			print output_list
			#filewriter.writerow(output_list)