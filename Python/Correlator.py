#!/usr/bin/env python2.7

# Libraries
import os.path
import pyexcel as pe

# File Paths
data_root='../Data'
test_file='mp1_2018_data.ods'
steam_file='property_list_water IAPWS.ods'

# Import Datasets
test_data = pe.get_sheet(file_name=os.path.join(data_root, test_file), start_column=0, column_limit=7)
for row in test_data:
    print("%s: %s: %s: %s: %s: %s:" % (row[0], row[1], row[2], row[3], row[4], row[5]))

# Import Steam Data
steam_data = pe.get_sheet(file_name=os.path.join(data_root, steam_file), start_column=0, column_limit=7)
for row in steam_data:
    print("%s: %s: %s: %s: %s: %s:" % (row[0], row[1], row[2], row[3], row[4], row[5]))
