#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import glob
import os
import sys
import xlrd

input_directory = sys.argv[1]

workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
	workbook = xlrd.open_workbook(input_file)
	print 'Workbook:',os.path.basename(input_file)
	print 'Number of worksheets:',workbook.nsheets
	for worksheet in workbook.sheets():
		print "Worksheet name:",worksheet.name, "Rows:",worksheet.nrows, "Columns:",worksheet.ncols
		#print worksheet.row_values(0)
	print ""
	workbook_counter += 1
print 'Number of Excel workbooks: %d' % (workbook_counter)
