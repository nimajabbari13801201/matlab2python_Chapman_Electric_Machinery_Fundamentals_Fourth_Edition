import numpy as np
import matplotlib.pyplot as plt

# مقادیر این ژنراتور
flux_ratio = np.arange(0.90, 1.01, 0.01)  # نسبت شار مغناطیسی
Ear = 695  # Ea در حالت شار کامل (V)
dr = 38.4 * np.pi / 180  # زاویه گشتاور در حالت شار کامل (رادیان)
Vp = 277  # ولتاژ فازی (V)
Xs = 0.899  # reactance (Ω)

# محاسبه Ea برای هر flux
Ea = flux_ratio * Ear

# محاسبه delta برای هر flux
d = np.arcsin(Ear / Ea * np.sin(dr))

# محاسبه Ia برای هر flux
Ea_complex = Ea * (np.cos(d) + 1j * np.sin(d))
Ia = (Ea_complex - Vp) / (1j * Xs)

# محاسبه توان واکنشی برای هر flux
theta = -np.arctan2(np.imag(Ia), np.real(Ia))
Q = 3 * Vp * np.abs(Ia) * np.sin(theta)

# رسم توان واکنشی در مقابل flux
plt.plot(flux_ratio, Q / 1000, 'b-', linewidth=2.0)
plt.title(r'$\bf{Reactive\ Power\ Versus\ Flux}$', fontsize=14, weight='bold')
plt.xlabel(r'$\bf{Flux\ ( \% \ of\ Full-Load\ Flux)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{Q\ (kVAR)}$', fontsize=12, weight='bold')
plt.grid(True)
plt.show()
