""" Smoothing CO2-Data (done on VSC with Python 3.11.4, without Artificial Intelligence) """

# author: Clemens Loher
# date: 2026-10-18

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

if __name__ == '__main__':
    
    # load data
    data = np.loadtxt("co2_mm_mlo.csv", delimiter=",", skiprows=41)
    months = data[:,1]
    years = data[:,2]
    co2 = data[:,3]
    
    # savgol filter
    window_length = 15 # We choose a window length of 15 months, which is an odd number and large enough to smooth the data but not too large to lose important features
    polyorder = 6 # because polyorder 3 would cut off the spikes in the data, we choose a higher order polynomial to better fit the data
    co2_savgol = signal.savgol_filter(co2, window_length = window_length, polyorder = polyorder)
    
    # moving average
    window_size = 12 # Because we have monthly data, we take a window size of 12 months
    weights = np.ones(window_size)/window_size
    co2_moving_avg = np.convolve(co2, weights, mode='valid') # plot only the valid part of the convolution to avoid edge effects
    
    # correct the years for the moving average to match the length of the filtered data
    offset = window_size // 2
    years_valid = years[offset : len(years) - (window_size - 1 - offset)]
    
    # plot results
    plt.figure(figsize=(15, 7))
    plt.plot(years, co2, label='Original CO2 Data', color='gray', alpha=0.7)
    plt.plot(years, co2_savgol, label='Savitzky-Golay Filtered', color='blue')
    plt.plot(years_valid, co2_moving_avg, label='Moving Average', color='red') # [window_size-1:]
    plt.xlabel('Year')
    plt.ylabel('CO2 Concentration (ppm)')
    plt.legend()
    plt.show()
    