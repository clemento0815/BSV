""" Dicom File einlesen """

# author: Clemens Loher
# date: 2026-10-22

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
import pydicom

if __name__ == '__main__':
  main part of your code


%history
dir
ls
in_file = 'SER00002/2A1A1ADC'
pydicom.dcmread(in_file)
data = pydicom.dcmread(in_file)
type(data)
data
dir(data)
img_data = data.pixel_array
type(img_data)
img_data.shape
plt.imshow(img_data)
plt.imshow(img_data, cmap = 'gray')
img_data
plt.imshow(img_data, cmap = 'jet')
plt.imshow(img_data, cmap = 'jet'); colormap()
plt.imshow(img_data, cmap = 'jet'); colorbar()
plt.imshow(img_data, cmap = 'jet')
plt.colorbar()
plt.imshow(img_data, cmap = 'jet'); plt.colorbar()