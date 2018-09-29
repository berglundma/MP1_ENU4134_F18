#!/usr/bin/env python2.7

# Libraries to be imported
import os.path
import math
import pyexcel as pe
import numpy as np
#import matplotlib.pyplot as plt

# Functions to be imported
from Equations import *

# Constants
g = 9.81
sigma = 0.07407

# File Paths
data_root='../Data'
test_file='mp1_2018_data.ods'
tdv_file='Table_densities_viscosities.ods'

# Import Datasets
test_data = pe.get_sheet(file_name=os.path.join(data_root, test_file), start_column=0, column_limit=8)
#print(test_data.content)

# Import TDV Data
tdv_data = pe.get_sheet(file_name=os.path.join(data_root, tdv_file), start_column=0, column_limit=15)
#print(tdv_data.content)

# Test Calculations from the equations file
#print("Area: %s" % (A(197)))

# Part 1
# HEM Correlation
n = 0
for row_test in test_data:
    print('Line Number: %s' % (n))
    D = row_test[0]/1000
    print('D: %s' % (row_test[0]))
    t_mdotg = row_test[4]/1000
    print('m_dot_g: %s' % (row_test[4]))
    t_mdotf = row_test[5]/1000
    print('m_dot_f: %s' % (row_test[5]))
    gm = G_m(t_mdotg, t_mdotf, D)
    
    if row_test[3] == tdv_data[n,0]:
      print('P_test: %s P_data: %s' % (row_test[3], tdv_data[n,0]))
      dp_dz = dp_dz_HEM(gm, tdv_data[n,0], t_mdotg, t_mdotf, tdv_data[n,1], tdv_data[n,2], D)
      print('mu_f: %s   rho_f: %s rho_g: %s' % (tdv_data[n,3], row_test[1], tdv_data[n,2]))
      print('Correlated: %s   Experimental: %s' % (dp_dz, row_test[7]))

    n=n+1

# Lockhard-Martinelli Correlation

# Friedel Correlation

# Part 2

# Part 3

