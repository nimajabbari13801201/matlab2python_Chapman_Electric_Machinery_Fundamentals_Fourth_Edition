import numpy as np
import matplotlib.pyplot as plt

# مقادیر اولیه
r1 = 1.80  # مقاومت استاتور (اهم)
x1 = 2.40  # واکنش استاتور (اهم)
r2 = 2.50  # مقاومت روتور (اهم)
x2 = 2.40  # واکنش روتور (اهم)
xm = 60  # واکنش شاخه مغناطیسی (اهم)
v = 120  # ولتاژ تک‌فاز (ولت)
n_sync = 1800  # سرعت همزمان (ر.دقیقه)
w_sync = 188.5  # سرعت همزمان (راد/ثانیه)

# تعیین محدوده‌های لغزش برای رسم نمودار
s = np.arange(0, 2.01, 0.01)
s[0] = 0.0001  # جلوگیری از تقسیم بر صفر
s[200] = 1.9999  # جلوگیری از تقسیم بر صفر

# محاسبه سرعت‌های مربوطه بر حسب rpm
nm = (1 - s) * n_sync

# محاسبه Zf و Zb به عنوان تابعی از لغزش
zf = (r2 / s + 1j * x2) * (1j * xm) / (r2 / s + 1j * x2 + 1j * xm)
zb = (r2 / (2 - s) + 1j * x2) * (1j * xm) / (r2 / (2 - s) + 1j * x2 + 1j * xm)

# محاسبه جریان‌های جاری در هر لغزش
i1 = v / (r1 + 1j * x1 + zf + zb)

# محاسبه توان شکاف هوا
p_ag_f = np.abs(i1)**2 * 0.5 * np.real(zf)
p_ag_b = np.abs(i1)**2 * 0.5 * np.real(zb)
p_ag = p_ag_f - p_ag_b

# محاسبه گشتاور در N-m
t_ind = p_ag / w_sync

# رسم نمودار گشتاور-سرعت
plt.figure(1)
plt.plot(nm, t_ind, color='b', linewidth=2.0)
plt.xlabel(r'$\it{n_{m}}$ (r/min)', fontsize=12)
plt.ylabel(r'$\tau_{ind}$ (N-m)', fontsize=12)
plt.title('Single Phase Induction motor torque-speed characteristic', fontsize=12)
plt.grid(True)
plt.show()
