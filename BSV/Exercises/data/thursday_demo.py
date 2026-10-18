""" Demo, zum Einlesen von Daten """


# authors: Thomas Haslwanter
# date:    Feb-2024

# Standard Python packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def read_data(in_dir):
    """ Reads in the data """

    os.chdir(in_dir)

    # Read in the first file
    first_file = 'ecg_hfn.dat'
    df = pd.read_csv(first_file, header=None)
    print(df.head())

    # Read in the second file
    in_file = 'ecg_hfn.txt'
    df2 = pd.read_csv(in_file)
    print(df2.head())


if __name__ == '__main__':
    data_dir = r'C:\Users\p20529\CloudStation\Teaching\BSV\exercises\Assignment_3\data'

    read_data(data_dir)
