import numpy as np

def R2(corr, exp):
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      corr_mean = np.mean(corr)
      corr_std  = np.std(corr)
      exp_mean  = np.mean(exp)
      exp_std   = np.std(exp)
    
      for x in range(0, n_corr)
        sum_corr = (corr[x]-corr_mean)/corr_std
        sum_exp  = (exp[x] -exp_mean)/exp_std
        sum_total += sum_corr*sum_exp

      r = (1/(1-n))(sum_total))
      return r;

    else:
      print "error calculating R2, length of arrays not equal"

# Mean Absolute Error - must be fed 1-D arrays
def MAE(corr, exp):
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      for x in range(0, n_corr)
        sum_total += np.absolute(((corr[n]-exp[n])/exp[n])*100)

      mae = (1/n)(sum_total))
      return mae;

    else:
      print "error calculating MAE, length of arrays not equal"

# Root Mean Square error must be fed 1-D arrays
def RMS(corr, exp):
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      n = n_corr
      for x in range(0, n)
        sum_total += (((corr[n]-exp[n])/exp[n])*100)**2

      rms = np.sqrt((1/n)(sum_total)))
      return rms;

    else:
      print "error calculating RMS, length of arrays not equal"

# Mean error must be fed 1-D arrays
def MEANError(corr, exp):
    n_corr = len(corr)
    n_exp  = len(exp)

    if n_corr == n_exp:
      n = n_corr
      for x in range(0, n)
        sum_total += ((corr[n]-exp[n])/exp[n])*100

      mean_error = (1/n)(sum_total))
      return mean_error;

    else:
      print "error calculating Mean Error, length of arrays not equal"
