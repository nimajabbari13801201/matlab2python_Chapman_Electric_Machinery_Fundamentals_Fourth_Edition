import numpy as np
import matplotlib.pyplot as plt

# محاسبه زاویه گشتاور و توان خروجی
delta = np.arange(0, 91, 1)  # زاویه گشتاور از 0 تا 90 درجه
Pout = 561 * np.sin(delta * np.pi / 180)  # توان خروجی

# رسم نمودار توان خروجی بر حسب زاویه گشتاور
plt.plot(delta, Pout, linewidth=2.0)
plt.title(r'$\bf{Output\ power\ vs\ torque\ angle\ \delta}$', fontsize=14, weight='bold')
plt.xlabel(r'$\bf{Torque\ angle\ \delta\ (deg)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{P_{OUT}\ (kW)}$', fontsize=12, weight='bold')
plt.grid(True)
plt.show()
