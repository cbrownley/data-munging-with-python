#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
#output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
for file in all_files:
	# Parse the first worksheet, with index value 0, in each workbook
	data_frame = pd.read_excel(file, 0, index_col=None)
	data_frames.append(data_frame)
data_frame_concat = pd.concat(data_frames, ignore_index=True)

print data_frame_concat
#data_frame_concat.to_csv(output_file, index = False)