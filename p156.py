import numpy as np
import matplotlib.pyplot as plt

# مقادیر اولیه
If = np.arange(2.5, 8.1, 0.1)  # مقدار جریان میدان (A)
Xs = 1.5  # واکنش همزمان
Vp = 1328  # ولتاژ فازی

# مقادیر Ea و delta برای حالت‌های مختلف بار
d_nl = -1.27 * np.pi / 180  # زاویه در حالت بدون بار
d_half = -11.2 * np.pi / 180  # زاویه در حالت نیمه‌بار
d_full = -22.7 * np.pi / 180  # زاویه در حالت بار کامل
Ea_nl = 1328.3  # Ea در حالت بدون بار
Ea_half = 1354  # Ea در حالت نیمه‌بار
Ea_full = 1439  # Ea در حالت بار کامل

# بارگذاری داده‌ها از فایل p61_occ.dat
occ_data = np.loadtxt('p61_occ.dat')
if_values = occ_data[:, 0]
vt_values = occ_data[:, 1]

# محاسبه Ea برای هر مقدار از جریان میدان
Ea = np.interp(If, if_values, vt_values) / np.sqrt(3)

# محاسبه جریان‌های آرمایچر برای حالت‌های مختلف بار

# حالت بدون بار
delta = np.arcsin(Ea_nl / Ea * np.sin(d_nl))
Ea2 = Ea * (np.cos(delta) + 1j * np.sin(delta))
Ia_nl = (Vp - Ea2) / (1j * Xs)

# حالت نیمه‌بار
delta = np.arcsin(Ea_half / Ea * np.sin(d_half))
Ea2 = Ea * (np.cos(delta) + 1j * np.sin(delta))
Ia_half = (Vp - Ea2) / (1j * Xs)

# حالت بار کامل
delta = np.arcsin(Ea_full / Ea * np.sin(d_full))
Ea2 = Ea * (np.cos(delta) + 1j * np.sin(delta))
Ia_full = (Vp - Ea2) / (1j * Xs)

# رسم منحنی v-curve
plt.plot(If, np.abs(Ia_nl), 'k-', linewidth=2.0, label='No-Load')
plt.plot(If, np.abs(Ia_half), 'b--', linewidth=2.0, label='Half-Load')
plt.plot(If, np.abs(Ia_full), 'r:', linewidth=2.0, label='Full-Load')

plt.xlabel(r'$\bf{Field\ Current\ (A)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{Armature\ Current\ (A)}$', fontsize=12, weight='bold')
plt.title(r'$\bf{Synchronous\ Motor\ V-Curve}$', fontsize=14, weight='bold')
plt.grid(True)
plt.legend()
plt.show()
