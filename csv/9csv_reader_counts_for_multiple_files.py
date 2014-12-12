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

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 0
	with open(input_file, 'rU') as csv_in_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		header = next(filereader, None)
		#print header
		for row in filereader:
			#print row
			row_counter += 1
	print '%s: %d rows %d columns' % (os.path.basename(input_file), row_counter+1, len(header))
	file_counter += 1
print 'Number of files: %d' % (file_counter)