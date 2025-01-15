import numpy as np
import matplotlib.pyplot as plt

# Given values
Q = -4810
DE = 5567
S = 1000

# Get points for stator current limit
theta = np.arange(-95, 96, 1)  # Angle in degrees
rad = np.deg2rad(theta)  # Angle in radians
s_curve = S * (np.cos(rad) + 1j * np.sin(rad))

# Get points for rotor current limit
orig = 1j * Q
theta = np.arange(75, 106, 1)  # Angle in degrees
rad = np.deg2rad(theta)  # Angle in radians
r_curve = orig + DE * (np.cos(rad) + 1j * np.sin(rad))

# Plot the capability diagram
plt.figure(1)
plt.plot(np.real(s_curve), np.imag(s_curve), 'b', linewidth=2.0, label='Stator Current Limit')
plt.plot(np.real(r_curve), np.imag(r_curve), 'r--', linewidth=2.0, label='Rotor Current Limit')

# Add x and y axes
plt.plot([-1500, 1500], [0, 0], 'k')
plt.plot([0, 0], [-1500, 1500], 'k')

# Set titles and axes
plt.title('Synchronous Generator Capability Diagram', fontsize=14, weight='bold')
plt.xlabel('Power (kW)', fontsize=12, weight='bold')
plt.ylabel('Reactive Power (kVAR)', fontsize=12, weight='bold')
plt.axis([-1500, 1500, -1500, 1500])
plt.axis('square')
plt.legend()

# Show the plot
plt.show()
