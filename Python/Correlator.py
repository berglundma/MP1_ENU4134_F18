#!/usr/bin/env python2.7

# Libraries to be imported
import os.path
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Functions to be imported
from Equations import *

# Constants
g = 9.81
sigma = 0.07407

# File Paths
data_root='../Data'
test_file='mp1_2018_data.csv'
tdv_file='Table_densities_viscosities.csv'
test_file_full_path=os.path.join(data_root, test_file)
tdv_file_full_path=os.path.join(data_root, tdv_file)

# Import Datasets
test_data = pd.read_csv(test_file_full_path, names=['D', 'Air_Meter', 'Water_Meter', 'PressureE', 'm_dot_g', 'm_dot_f', 'delta', 'dP_dz'], skiprows=2)
print(test_data)

# Import TDV Data
tdv_data = pd.read_csv(tdv_file_full_path, names=['PressureC', 'rho_f', 'rho_g', 'mu_f', 'mu_g'], skiprows=1)
print(tdv_data)

data = pd.concat([test_data, tdv_data], axis=1, sort=False)
#data.to_csv('example.csv')
print(data)

####### Part 1 #######

### HEM Correlation ###
n = 0
for row_test in data.itertuples():
   D = row_test.D/1000
   t_mdotg = row_test.m_dot_g/1000
   t_mdotf = row_test.m_dot_f/1000
   gm = G_m(t_mdotg, t_mdotf, D)
   dp_dz = dp_dz_HEM(gm, row_test.mu_f, t_mdotg, t_mdotf, row_test.rho_f, row_test.rho_g, D)
   dp_dz = dp_dz/1000

   print('.')
   print('.')
   print('.')
   print('HEM Correlation')
   print('D: %s   m_dot_g: %s   m_dot_f: %s' % (row_test.D, row_test.m_dot_g, row_test.m_dot_f))
   print('GM: %s' % (gm))
   print('P_test: %s P_data: %s' % (row_test.PressureE, row_test.PressureC))
   print('mu_f: %s   rho_f: %s   rho_g: %s' % (row_test.mu_f, row_test.rho_f, row_test.rho_g))
   print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test.dP_dz))
   n+=1

### Lockhard-Martinelli Correlation ###
n = 0
for row_test in data.itertuples():
   D = row_test.D/1000
   t_mdotg = row_test.m_dot_g/1000
   t_mdotf = row_test.m_dot_f/1000
   gm = G_m(t_mdotg, t_mdotf, D)
   dp_dz = dp_dz_LM(row_test.mu_f, row_test.mu_g, t_mdotg, t_mdotf, row_test.rho_g, row_test.rho_f, gm, D)
   dp_dz = dp_dz/1000

   print('.')
   print('.')
   print('.')
   print('Lockhart-Martinelli Correlation')
   print('D: %s   m_dot_g: %s   m_dot_f: %s' % (row_test.D, row_test.m_dot_g, row_test.m_dot_f))
   print('GM: %s' % (gm))
   print('P_test: %s P_data: %s' % (row_test.PressureE, row_test.PressureC))
   print('mu_f: %s   rho_f: %s   rho_g: %s' % (row_test.mu_f, row_test.rho_f, row_test.rho_g))
   print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test.dP_dz))
   n+=1

### Friedel Correlation ###
n = 0
for row_test in data.itertuples():
   D = row_test.D/1000
   t_mdotg = row_test.m_dot_g/1000
   t_mdotf = row_test.m_dot_f/1000
   gm = G_m(t_mdotg, t_mdotf, D)
   dp_dz = dp_dz_fri(t_mdotg, t_mdotf, row_test.rho_f, gm, row_test.mu_f, row_test.rho_g, row_test.mu_g, sigma, D)
   dp_dz = dp_dz/1000

   print('.')
   print('.')
   print('.')
   print('Friedel Correlation')
   print('D: %s   m_dot_g: %s   m_dot_f: %s' % (row_test.D, row_test.m_dot_g, row_test.m_dot_f))
   print('GM: %s' % (gm))
   print('P_test: %s P_data: %s' % (row_test.PressureE, row_test.PressureC))
   print('mu_f: %s   rho_f: %s   rho_g: %s' % (row_test.mu_f, row_test.rho_f, row_test.rho_g))
   print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test.dP_dz))
   n+=1

####### Part 2 #######

####### Part 3 #######
