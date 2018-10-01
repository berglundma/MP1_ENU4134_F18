# Where all the plotting functions live
import os.path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def scatter_plot_HEM(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_HEM_dpdz.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred) 
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs HEM Calculated')
    plt.xlim(-60, 0)
    plt.ylim(-60, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    plt.show()

def scatter_plot_HEM_mdot(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_HEM_mdot.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs HEM Calculated')
    plt.xlim(-60, 0)
    plt.ylim(-60, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    plt.show()

def scatter_plot_LM(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_LM_dpdz.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs L-M Calculated')
    plt.xlim(-50, 0)
    plt.ylim(-50, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    plt.show()

def scatter_plot_Fe(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_Fe_dpdz.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs Friedel Calculated')
    plt.xlim(-50, 0)
    plt.ylim(-50, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    plt.show()
