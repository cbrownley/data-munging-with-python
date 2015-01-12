#!/usr/bin/python
import pandas as pd
import string
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame[(data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0)]

print data_frame_value_meets_condition
#data_frame_value_meets_condition.to_csv(output_file, index=False)
