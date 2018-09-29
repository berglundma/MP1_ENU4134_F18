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

####### Part 1 #######

### HEM Correlation ###
n = 0
for row_test in test_data:
    if tdv_data[n,0] != 0:
        print('.')
        print('.')
        print('.')
        print('HEM Correlation')
        D = row_test[0]/1000
        print('D: %s   m_dot_g: %s   m_dot_f: %s' % (row_test[0], row_test[4], row_test[5]))
        t_mdotg = row_test[4]/1000
        t_mdotf = row_test[5]/1000
        gm = G_m(t_mdotg, t_mdotf, D)
        print('P_test: %s   P_data: %s' % (row_test[3], tdv_data[n,0]))
        if row_test[3] == tdv_data[n,0]:
            dp_dz = dp_dz_HEM(gm, tdv_data[n,3], t_mdotg, t_mdotf, tdv_data[n,1], tdv_data[n,2], D)
            print('mu_f: %s   rho_f: %s   rho_g: %s' % (tdv_data[n,3], row_test[1], tdv_data[n,2]))
            dp_dz = dp_dz/1000
            print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test[7]))
    n=n+1
    if n == 130:
        break
### Lockhard-Martinelli Correlation ###
n = 0
for row_test in test_data:
    if tdv_data[n,0] != 0:
        print('.')
        print('.')
        print('.')
        print('Lockhart-Martinelli Correlation')
        D = row_test[0]/1000
        print('D: %s   m_dot_g: %s   m_dot_f: %s' % (row_test[0], row_test[4], row_test[5]))
        t_mdotg = row_test[4]/1000
        t_mdotf = row_test[5]/1000
        gm = G_m(t_mdotg, t_mdotf, D)
        print('P_test: %s   P_data: %s' % (row_test[3], tdv_data[n,0]))
        if row_test[3] == tdv_data[n,0]:
            dp_dz = dp_dz_LM(tdv_data[n,3], tdv_data[n,4], t_mdotg, t_mdotf, tdv_data[n,2], tdv_data[n,1], gm, D)
            print('mu_f: %s   rho_f: %s   rho_g: %s' % (tdv_data[n,3], row_test[1], tdv_data[n,2]))
            dp_dz = dp_dz/1000
            print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test[7]))
    n=n+1
    if n == 130:
        break
### Friedel Correlation ###
n = 0
for row_test in test_data:
    if tdv_data[n,0] != 0:
        print('.')
        print('.')
        print('.')
        print('Friedel Correlation')
        D = row_test[0]/1000
        print('D: %s   m_dot_g: %s   m_dot_f: %s' % (row_test[0], row_test[4], row_test[5]))
        t_mdotg = row_test[4]/1000
        t_mdotf = row_test[5]/1000
        gm = G_m(t_mdotg, t_mdotf, D)
        print('P_test: %s   P_data: %s' % (row_test[3], tdv_data[n,0]))
        if row_test[3] == tdv_data[n,0]:
            dp_dz = dp_dz_fri(t_mdotg, t_mdotf, tdv_data[n,1], gm, tdv_data[n,3], tdv_data[n,2], tdv_data[n,4], sigma, D)
            print('mu_f: %s   rho_f: %s   rho_g: %s' % (tdv_data[n,3], row_test[1], tdv_data[n,2]))
            dp_dz = dp_dz/1000
            print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test[7]))
    n=n+1
    if n == 130:
        break

####### Part 2 #######

####### Part 3 #######
