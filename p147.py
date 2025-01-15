import numpy as np
import matplotlib.pyplot as plt

# مقادیر این ژنراتور
Ea = np.arange(0.65, 1.01, 0.01) * 13230  # Ea (V)
Vp = 7044  # ولتاژ فازی (V)
d1 = 27.9 * np.pi / 180  # زاویه گشتاور در حالت شار کامل (رادیان)
Xs = 8.18  # reactance (Ω)

# محاسبه delta برای هر Ea
d = np.arcsin(13230 / Ea * np.sin(d1))

# محاسبه Ea به صورت مختلط
Ea_complex = Ea * (np.cos(d) + 1j * np.sin(d))

# محاسبه Ia برای هر Ea
Ia = (Ea_complex - Vp) / (1j * Xs)

# رسم جریان آرمایچر در مقابل Ea
plt.plot(Ea / 1000, np.abs(Ia), 'b-', linewidth=2.0)
plt.title(r'$\bf{Armature\ Current\ Versus\ E_A}$', fontsize=14, weight='bold')
plt.xlabel(r'$\bf{E_A\ (kV)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{I_A\ (A)}$', fontsize=12, weight='bold')
plt.grid(True)
plt.show()
