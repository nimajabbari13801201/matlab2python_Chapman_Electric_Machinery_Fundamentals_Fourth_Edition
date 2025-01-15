import numpy as np
import matplotlib.pyplot as plt

# مقادیر اولیه
Ea = np.arange(1, 1.71, 0.01) * 384  # اندازه ولتاژ داخلی Ea (V)
Ear = 384  # Ea مرجع
deltar = -36.4 * np.pi / 180  # زاویه گشتاور مرجع (رادیان)
Xs = 1.1  # reactance همزمان
Vp = 480  # ولتاژ فازی در 0 درجه (V)

# محاسبه Ea مرجع به صورت مختلط
Ear_complex = Ear * (np.cos(deltar) + 1j * np.sin(deltar))

# محاسبه delta2
delta2 = np.arcsin(np.abs(Ear_complex) / np.abs(Ea) * np.sin(deltar))

# محاسبه phasor Ea برای هر مقدار از Ea
Ea_complex = Ea * (np.cos(delta2) + 1j * np.sin(delta2))

# محاسبه Ia
Ia = (Vp - Ea_complex) / (1j * Xs)

# رسم منحنی v-curve
plt.plot(np.abs(Ea_complex), np.abs(Ia), 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{E_A\ (V)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{I_A\ (A)}$', fontsize=12, weight='bold')
plt.title(r'$\bf{Synchronous\ Motor\ V-Curve}$', fontsize=14, weight='bold')
plt.grid(True)
plt.show()
