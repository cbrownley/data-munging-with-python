#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

row_counter = 0
with open(input_file, 'rU') as filereader:
	#with open(output_file, 'wb') as filewriter:
		header = filereader.readline()
		header = header.strip()
		header_list = header.split(',')
		print header_list
		#filewriter.write(string.join(map(str,header_list),',')+'\n')
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print row_list
			#filewriter.write(string.join(map(str,row_list),',')+'\n')
			row_counter += 1
print 'Number of rows: %d' % (row_counter+1)
