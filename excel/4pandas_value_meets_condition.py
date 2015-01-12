#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import pandas as pd
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame['Sale Amount'] = data_frame['Sale Amount'].astype(float)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'] > 1400.0]

print data_frame_value_meets_condition
#data_frame_value_meets_condition.to_csv(output_file, index=False)
