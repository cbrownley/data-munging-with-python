#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import xlrd
import sys

input_file = sys.argv[1]

workbook = xlrd.open_workbook(input_file)
print 'Number of worksheets:',workbook.nsheets
for worksheet in workbook.sheets():
	print "Worksheet name:",worksheet.name, "Rows:",worksheet.nrows, "Columns:",worksheet.ncols
	#print worksheet.row_values(0)
