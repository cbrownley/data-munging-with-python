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

data_frame = pd.read_csv(input_file)

data_frame_value_matches_pattern = data_frame[data_frame['Invoice Number'].str.startswith("001-")]

print data_frame_value_matches_pattern
#data_frame_value_matches_pattern.to_csv(output_file, index=False)
