import numpy as np
import matplotlib.pyplot as plt

# Set up the basic conditions
bmax = 1  # Normalize bmax to 1
freq = 60  # Frequency (Hz)
w = 2 * np.pi * freq  # Angular velocity (rad/s)

# Time vector
t = np.arange(0, 1/60, 1/6000)  # Time from 0 to 1/60 with step size 1/6000

# Generate the three component magnetic fields
Baa = np.sin(w * t) * (np.cos(0) + 1j * np.sin(0))
Bbb = np.sin(w * t + 2 * np.pi / 3) * (np.cos(2 * np.pi / 3) + 1j * np.sin(2 * np.pi / 3))
Bcc = np.sin(w * t - 2 * np.pi / 3) * (np.cos(-2 * np.pi / 3) + 1j * np.sin(-2 * np.pi / 3))

# Calculate Bnet
Bnet = Baa + Bbb + Bcc

# Calculate a circle representing the expected maximum value of Bnet
circle = 1.5 * (np.cos(w * t) + 1j * np.sin(w * t))

# Plot the magnitude and direction of the resulting magnetic fields
plt.figure()
for ii in range(len(t)):
    # Plot the reference circle
    plt.plot([0, np.real(circle[ii])], [0, np.imag(circle[ii])], 'k')

    # Plot the four magnetic fields
    plt.plot([0, np.real(Baa[ii])], [0, np.imag(Baa[ii])], 'k', linewidth=2)
    plt.plot([0, np.real(Bbb[ii])], [0, np.imag(Bbb[ii])], 'b', linewidth=2)
    plt.plot([0, np.real(Bcc[ii])], [0, np.imag(Bcc[ii])], 'm', linewidth=2)
    plt.plot([0, np.real(Bnet[ii])], [0, np.imag(Bnet[ii])], 'r', linewidth=3)

    plt.axis('square')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.draw()
    plt.pause(0.0001)  # Allow the plot to update
    plt.clf()  # Clear the plot for the next frame

plt.show()
