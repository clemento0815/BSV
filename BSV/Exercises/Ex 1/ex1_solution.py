# Autor: Clemens Loher
# Date: 24.09.2026

# import packages
import numpy as np
import matplotlib.pyplot as plt


# compulsory

# Part 1
# variables
amp=3
duration=10
freq=0.5
n=500 #counted values
angle=30

# 500 steps to provide the wave shape
t = np.linspace(0, duration, n)

# calculate Sine-Wave
y=amp*np.sin(2*np.pi*freq*t)

# plotting the Sine-Wave
plt.plot(t,y,label="Sinuswave")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.title("Sinuswave")
plt.grid(True)
plt.savefig("sinus_plot.png", dpi=600) #save as Pic
plt.legend()
plt.show()
print('Plot 1 has been saved.')

# Part 2
# stacking t,y
data = np.column_stack((t,y))

# changing degree to rad
phi = np.radians(angle)

# rotationmatrix
R = np.array([[np.cos(phi),-np.sin(phi)],[np.sin(phi),np.cos(phi)]])

# transpose data
rotated_data = data @ R.T

# separating rotated matrix
t_rot=rotated_data[:,0]
y_rot=rotated_data[:,1]

# superposed Sinewaves plot
plt.plot(t, y, label="Sinewave", color="blue",linestyle="-")
plt.plot(t_rot, y_rot, label="Sinwave rotated (30°)", color="red", linestyle="-")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.title("Superposed Sinuswaves")
plt.axis("equal") 
plt.legend()
plt.grid(True)

# save plot as pic
plt.savefig("superposed_plot.png", dpi=600)
plt.show()
print('Plot 2 has been saved.')

