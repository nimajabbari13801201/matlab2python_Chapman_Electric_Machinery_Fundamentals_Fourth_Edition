import numpy as np
import matplotlib.pyplot as plt

# Define values for this generator
EA = 1328  # Internal gen voltage
I = np.arange(0, 251, 2.51)  # Current values (A)
R = 0.15  # Resistance (ohms)
X = 1.10  # Reactance (ohms)

# Calculate the voltage for the lagging PF case
VP_lag = np.sqrt(EA**2 - (X * I * 0.8 - R * I * 0.6)**2) - R * I * 0.8 - X * I * 0.6
VT_lag = VP_lag * np.sqrt(3)

# Calculate the voltage for the leading PF case
VP_lead = np.sqrt(EA**2 - (X * I * 0.8 + R * I * 0.6)**2) - R * I * 0.8 + X * I * 0.6
VT_lead = VP_lead * np.sqrt(3)

# Calculate the voltage for the unity PF case
VP_unity = np.sqrt(EA**2 - (X * I)**2)
VT_unity = VP_unity * np.sqrt(3)

# Plot the terminal voltage versus load
plt.plot(I, np.abs(VT_lag), 'b-', linewidth=2.0, label='0.8 PF lagging')
plt.plot(I, np.abs(VT_unity), 'k--', linewidth=2.0, label='1.0 PF')
plt.plot(I, np.abs(VT_lead), 'r-.', linewidth=2.0, label='0.8 PF leading')

# Set titles and labels
plt.title('Terminal Voltage Versus Load', fontsize=14, weight='bold')
plt.xlabel('Load (A)', fontsize=12, weight='bold')
plt.ylabel('Terminal Voltage (V)', fontsize=12, weight='bold')

# Set the axis limits and grid
plt.axis([0, 260, 1500, 2500])
plt.grid(True)

# Add the legend
plt.legend()

# Show the plot
plt.show()
