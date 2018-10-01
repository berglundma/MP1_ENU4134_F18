# Where all the plotting functions live
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def scatter_plot(Y_test, Y_pred):
    # Define Plot
    #r_squared = 0.59
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\delta P/\delta z$ Measured')
    plt.ylabel(r'$\delta P/\delta z$ Calculated')

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.show()
