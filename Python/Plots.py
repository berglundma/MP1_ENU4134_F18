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
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured $(\frac{kPa}{m})$')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs HEM Calculated')
    plt.xlim(-60, 0)
    plt.ylim(-60, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_HEM_mdot(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_HEM_mdot.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\dot m_g (\frac{g}{S})$')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\dot m_g$ vs HEM Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_HEM_rho(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_HEM_rho.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\rho_g (\frac{kg}{m^3})$')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\rho_g$ vs HEM Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_HEM_D(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_HEM_D.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel('Diameter (mm)')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title('Pipe Diameter vs HEM Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()


def scatter_plot_LM(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_LM_dpdz.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred) 
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured $(\frac{kPa}{m})$')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs Lockhart-Martinelli Calculated')
    plt.xlim(-60, 0)
    plt.ylim(-60, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_LM_mdot(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_LM_mdot.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\dot m_g (\frac{g}{S})$')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\dot m_g$ vs Lockhart-Martinelli Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_LM_rho(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_LM_rho.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\rho_g (\frac{kg}{m^3})$')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\rho_g$ vs Lockhart-Martinelli Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_LM_D(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_LM_D.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel('Diameter (mm)')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title('Pipe Diameter vs Lockhart-Martinelli Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_FE(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_FE_dpdz.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred) 
    plt.xlabel(r'$\frac{\delta P}{\delta z}$ Measured $(\frac{kPa}{m})$')
    plt.ylabel(r'$\frac{\delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\frac{\delta P}{\delta z}$ Measured vs Friedel Calculated')
    plt.xlim(-60, 0)
    plt.ylim(-60, 0)

    # Generate Plot
    plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_FE_mdot(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_FE_mdot.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\dot m_g (\frac{g}{S})$')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\dot m_g$ vs Friedel Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_FE_rho(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_FE_rho.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel(r'$\rho_g (\frac{kg}{m^3})$')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title(r'$\rho_g$ vs Friedel Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()

def scatter_plot_FE_D(Y_test, Y_pred):
    data_root='../Latex/figures'
    image_file='scatter_plot_FE_D.png'

    # Define Plot
    my_dpi=300
    plt.figure(figsize=(2100/my_dpi, 2100/my_dpi), dpi=my_dpi)
    plt.scatter(Y_test,Y_pred)
    plt.xlabel('Diameter (mm)')
    plt.ylabel(r'$\frac{delta P}{\delta z}$ Calculated $(\frac{kPa}{m})$')
    plt.title('Pipe Diameter vs Friedel Calculated')

    # Generate Plot
    #plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)), color='red')

    # Add R-squared label and show/print plot
    #plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
    plt.savefig(os.path.join(data_root, image_file))
    #plt.show()
