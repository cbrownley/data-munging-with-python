#!/usr/bin/python
import pandas as pd
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame_column_by_name = data_frame.ix[:, ['Invoice Number', 'Purchase Date']]

print data_frame_column_by_name
#data_frame_column_by_name.to_csv(output_file, index=False)
