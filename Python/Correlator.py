#!/usr/bin/env python2.7

# Libraries to be imported
import os.path
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Functions to be imported
from Equations import *
from Error import *

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

### HEM Cororelation ###
for row_test in data.itertuples():
   D = row_test.D/1000
   t_mdotg = row_test.m_dot_g/1000
   t_mdotf = row_test.m_dot_f/1000
   gm = G_m(t_mdotg, t_mdotf, D)
   dp_dz = dp_dz_HEM(gm, row_test.mu_f, t_mdotg, t_mdotf, row_test.rho_f, row_test.rho_g, D)
   dp_dz = dp_dz/1000
   data.at[row_test.Index, 'HEM_dp_dz'] = dp_dz

   #scatter_plot(arrayoftest, arrayofcorr)
   print('.')
   print('.')
   print('.')
   print('HEM Correlation')
   print(row_test)
   print('D: %s   m_dot_g: %s   m_dot_f: %s ' % (row_test.D, row_test.m_dot_g, row_test.m_dot_f))
   print('GM: %s' % (gm))
   print('P_test: %s P_data: %s' % (row_test.PressureE, row_test.PressureC))
   print('mu_f: %s   rho_f: %s   rho_g: %s' % (row_test.mu_f, row_test.rho_f, row_test.rho_g))
<<<<<<< HEAD
   print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test.dP_dz))
=======
   print('Correlated: %s kPa/m  Experimental: %s kPa/m' % (dp_dz, row_test.dP_dz)

>>>>>>> temp-branch
print(data)

# MAE
mae=MAE(data.HEM_dp_dz, data.dP_dz)
data.HEM_mae = mae

print(data)

# ME
merror=MError(data.HEM_dp_dz, data.dP_dz)
data.HEM_merror = merror

# RMS 
rms=RMS(data.HEM_dp_dz, data.dP_dz)
data.HEM_rms = rms

# R2
r2=R2(data.HEM_dp_dz, data.dP_dz)
data.HEM_R2 = r2
<<<<<<< HEAD


=======
>>>>>>> temp-branch

### Lockhard-Martinelli Correlation ###
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

### Friedel Correlation ###
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

####### Part 2 #######
AE_LM_Min = 100 # arbitrary starting value
C_min = 0 # arbitrary starting value
C = 0 # starting value
while C < 100.01: # ending value
    LM_corr = []
    exp = []
    for row_test in data.itertuples():
       D = row_test.D/1000
       t_mdotg = row_test.m_dot_g/1000
       t_mdotf = row_test.m_dot_f/1000
       gm = G_m(t_mdotg, t_mdotf, D)
       dp_dz = dp_dz_LM_2(row_test.mu_f, row_test.mu_g, t_mdotf, t_mdotg, row_test.rho_f, row_test.rho_g, gm, D, C)
       dp_dz = dp_dz/1000
       LM_corr = LM_corr + [dp_dz]
       exp = exp + [row_test.dP_dz]
    MAE_LM = MAE(LM_corr, exp)
    print(MAE_LM)
    if MAE_LM < MAE_LM_Min:
        MAE_LM_Min = MAE_LM
        C_min = C
    C = C + 0.01
print('.')
print('MAE_LM_Min: %s' % (MAE_LM_Min))
print('MAE_LM_Final_Min: %s' % (MAE_LM_Min))
print('C_min: %s' % (C_min))

####### Part 3 #######
MAE_Re_lo_Min = 100 # arbitrary starting value
C1_Re_lo_min = 0 # arbitrary starting value
C2_Re_lo_min = 0 # arbitrary starting value
C1 = -1 # starting value
while C1 < 0.01: # ending value
    C2 = -1 # starting value
    while C2 < 0.01: # ending value
        corr = []
        for row_test in data.itertuples():
           D = row_test.D/1000
           t_mdotg = row_test.m_dot_g/1000
           t_mdotf = row_test.m_dot_f/1000
           gm = G_m(t_mdotg, t_mdotf, D)
           dp_dz = dp_dz_fric_lo_3(gm, row_test.mu_f, t_mdotg, row_test.rho_g, D, C1, C2)
           dp_dz = dp_dz/1000
           corr = corr + [dp_dz]
        MAE_Re_lo = MAE(corr, exp)
        if MAE_Re_lo < MAE_Re_lo_Min:
            MAE_Re_lo_Min = MAE_Re_lo
            C1_Re_lo_min = C1
            C2_Re_lo_min = C2
        print(MAE_Re_lo_Min)
        C2 = C2 + 0.01
    C1 = C1 + 0.001
print('.')
print('MAE_Re_lo_Min_Final: %s' % (MAE_Re_lo_Min))
print('C1_Re_lo_min: %s' % (C1_Re_lo_min))
print('C2_Re_lo_min: %s' % (C2_Re_lo_min))
