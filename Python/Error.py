import numpy

# Mean Absolute Error - Best for correlation evaluation
def MAE(corr, exp):
    mae = np.sum(np.absolute((corr - exp)))
    return mae;

# Root Mean Square error must be fed 1-D arrays
def RMSE(corr, exp):
    return np.sqrt(((corr - exp) ** 2).mean())

