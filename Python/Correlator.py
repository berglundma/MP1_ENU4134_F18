#!/usr/bin/env python2.7

# Libraries to be imported
import os.path
import pyexcel as pe
import math

# Functions to be imported
from Equations import *

# Constants
g = 9.81

# File Paths
data_root='../Data'
test_file='mp1_2018_data.ods'
steam_file='property_list_water IAPWS.ods'

# Import Datasets
test_data = pe.get_sheet(file_name=os.path.join(data_root, test_file), start_column=0, column_limit=7)
print(test_data.content)

# Import Steam Data
steam_data = pe.get_sheet(file_name=os.path.join(data_root, steam_file), start_column=0, column_limit=15)
print(steam_data.content)

# Test Calculations from the equations file
#print("Area: %s" % (A(197)))

# Part 1
# HEM Correlation
for row in test_data:
    print("D mm: %s" % (row[0]))
    D = row[0]/1000
    t_mdotg = row[4]/1000
    t_mdotf = row[5]/1000
    gm = G_m(t_mdotg, t_mdotf, D)
    print("%s %s %s %s %s %s %s" % (gm, steam_data[1,4], t_mdotg, t_mdotf, steam_data[1,2], steam_data[1,11], D)) 
    dp_dz = dp_dz_HEM(gm, steam_data[1,4], t_mdotg, t_mdotf, steam_data[1,2], steam_data[1,11], D)
    print("dp_dz: %s" % (dp_dz))
# Part 2

# Part 3

