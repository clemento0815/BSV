"""header"""

# author: Clemens Loher
# date: 2026-11-03

# Import standard packages
import matplotlib.pyplot as plt
import numpy as np
from mat4py import loadmat

data = loadmat("S1_A1_E1.mat")
list = data["emg"]
emg = np.array(list)

print(emg.shape)

emg1 = emg[:, 0]
emg2 = emg[:, 1]
emg3 = emg[:, 2]
emg4 = emg[:, 3]
emg5 = emg[:, 4]
emg6 = emg[:, 5]
emg7 = emg[:, 6]
emg8 = emg[:, 7]
emg9 = emg[:, 8]
emg10 = emg[:, 9]

plt.figure(figsize=(12, 8))
plt.subplot(2, 5, 1)
plt.plot(emg1)
plt.title("EMG 1")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 5, 2)
plt.plot(emg2)
plt.title("EMG 2")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 5, 3)
plt.plot(emg3)
plt.title("EMG 3")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 5, 4)
plt.plot(emg4)
plt.title("EMG 4")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 5, 5)
plt.plot(emg5)
plt.title("EMG 5")
plt.xlabel("Time") 
plt.ylabel("Amplitude")

plt.subplot(2, 5, 6)
plt.plot(emg6)
plt.title("EMG 6")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 5, 7)
plt.plot(emg7)
plt.title("EMG 7")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2, 5, 8)
plt.plot(emg8)
plt.title("EMG 8")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.subplot(2, 5, 9)
plt.plot(emg9)
plt.title("EMG 9")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.subplot(2, 5, 10)
plt.plot(emg10)
plt.title("EMG 10")
plt.xlabel("Time")
plt.ylabel("Amplitude")
