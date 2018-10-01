import numpy as np

def R2(corr, exp):
    sum_total = 0
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      corr_mean = np.mean(corr)
      corr_std  = np.std(corr)
      exp_mean  = np.mean(exp)
      exp_std   = np.std(exp)

      for n in range(0, n_corr):
        sum_corr = (corr[n]-corr_mean)/corr_std
        sum_exp  = (exp[n]-exp_mean)/exp_std
        sum_total += sum_corr*sum_exp

#     Changes made:
#     1-n changed to n_corr-1
#     return r changed to return r**2
      r = (1.0/(n_corr-1.0))*(sum_total)
      R2 = r**2
      return R2;

    else:
      print('error calculating R2, length of arrays not equal')

# Mean Absolute Error - must be fed 1-D arrays
def MAE(corr, exp):
    sum_total = 0

    n_corr = len(corr)
    n_exp= len(exp)
    
    #print(corr, exp)
    if n_corr == n_exp:
      for n in range(0, n_corr):
        sum_total += np.absolute(((corr[n]-exp[n])/exp[n])*100)

#     Changes made:
#     n changed to n_corr
      mae = (1.0/n_corr)*(sum_total)
      return mae;

    else:
      print('error calculating R2, length of arrays not equal')

# Root Mean Square error must be fed 1-D arrays
def RMS(corr, exp):
    sum_total = 0
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      n = n_corr
      for n in range(0, n):
        sum_total += (((corr[n]-exp[n])/exp[n])*100)**2

      rms = np.sqrt((1.0/n)*(sum_total))
      return rms;

    else:
      print('error calculating R2, length of arrays not equal')

# Mean error must be fed 1-D arrays
def MEANError(corr, exp):
    sum_total = 0
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      n = n_corr
      for n in range(0, n):
        sum_total += ((corr[n]-exp[n])/exp[n])*100

      mean_error = (1.0/n)*(sum_total)
      return mean_error;

    else:
      print('error calculating R2, length of arrays not equal')
