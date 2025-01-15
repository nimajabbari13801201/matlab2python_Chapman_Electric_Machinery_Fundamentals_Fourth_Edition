import numpy as np
import matplotlib.pyplot as plt

# Define values for this generator
fnlA = 61.0  # No-load freq of Gen A
fnlB = 61.5  # No-load freq of Gen B
fnlC = 60.5  # No-load freq of Gen C
spA = 1.5    # Slope of Gen A (MW/Hz)
spB = 1.676  # Slope of Gen B (MW/Hz)
spC = 1.961  # Slope of Gen C (MW/Hz)
Pload = np.arange(0, 10.05, 0.05)  # Load in MW

# Calculate the system frequency
fsys = (313.2 - Pload) / 5.137

# Calculate the power of each generator
PA = spA * (fnlA - fsys)
PB = spB * (fnlB - fsys)
PC = spC * (fnlC - fsys)

# Plot the power sharing versus load
plt.plot(Pload, PA, 'b-', linewidth=2.0, label='Generator A')
plt.plot(Pload, PB, 'k--', linewidth=2.0, label='Generator B')
plt.plot(Pload, PC, 'r-.', linewidth=2.0, label='Generator C')

# Plot power limit lines
plt.plot([0, 10], [3, 3], 'k', linewidth=1.0)  # Power limit
plt.plot([0, 10], [0, 0], 'k:')  # Zero power line

# Set titles and labels
plt.title('Power Sharing Versus Total Load', fontsize=14, weight='bold')
plt.xlabel('Total Load (MW)', fontsize=12, weight='bold')
plt.ylabel('Generator Power (MW)', fontsize=12, weight='bold')

# Add legend
plt.legend()

# Enable grid
plt.grid(True)

# Show the plot
plt.show()
