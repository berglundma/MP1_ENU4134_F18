#!/usr/bin/env python2.7

# Libraries to be imported
import os.path
import math
import pyexcel as pe
import numpy as np
import matplotlib.pyplot as plt

# Functions to be imported
from Equations import *

# Constants
g = 9.81

# File Paths
data_root='../Data'
test_file='mp1_2018_data.ods'
tdv_file='Table_densities_viscosities.ods'

# Import Datasets
test_data = pe.get_sheet(file_name=os.path.join(data_root, test_file), start_column=0, column_limit=7)
print(test_data.content)

# Import Steam Data
tdv_data = pe.get_sheet(file_name=os.path.join(data_root, tdv_file), start_column=0, column_limit=15)
print(tdv_data.content)

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
    print("%s %s %s %s %s %s %s" % (gm, tdv_data[1,3], t_mdotg, t_mdotf, tdv_data[1,1], tdv_data[1,2], D))
    dp_dz = dp_dz_HEM(gm, tdv_data[1,3], t_mdotg, t_mdotf, tdv_data[1,1], tdv_data[1,2], D)
    print("dp_dz: %s" % (dp_dz))

# Part 2

# Part 3

