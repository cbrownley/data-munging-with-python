#!/usr/bin/python
import pandas as pd
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

important_dates = ['01/24/2013','01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]

print data_frame_value_in_set
#data_frame_value_in_set.to_csv(output_file, index=False)
