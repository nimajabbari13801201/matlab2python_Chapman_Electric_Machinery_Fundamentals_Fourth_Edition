import numpy as np
import matplotlib.pyplot as plt

# مقادیر اولیه
r1 = 0.105   # مقاومت استاتور
x1 = 0.211   # واکنش استاتور
r2 = 0.071   # مقاومت روتور
x2 = 0.317   # واکنش روتور
xm = 5.244   # واکنش شاخه مغناطیسی
v_phase = 208 / np.sqrt(3)  # ولتاژ فازی
n_sync = 1200  # سرعت سنکرون (ر.دقیقه)
w_sync = 125.7  # سرعت سنکرون (راد/ثانیه)

# محاسبه ولتاژ و امپدانس تهونن
v_th = v_phase * (xm / np.sqrt(r1**2 + (x1 + xm)**2))
z_th = ((1j*xm) * (r1 + 1j*x1)) / (r1 + 1j*(x1 + xm))
r_th = np.real(z_th)
x_th = np.imag(z_th)

# محاسبه ویژگی گشتاور-سرعت برای مقادیر مختلف لغزش
s = np.arange(0, 1.01, 0.02)  # لغزش (از 0.001 تا 1 با گام 0.02)
s[0] = 0.001  # برای جلوگیری از تقسیم بر صفر
nm = (1 - s) * n_sync  # سرعت مکانیکی (ر.دقیقه)

# محاسبه گشتاور در مقابل سرعت
t_ind = np.zeros(len(s))

for ii in range(len(s)):
    t_ind[ii] = (3 * v_th**2 * r2 / s[ii]) / \
                (w_sync * ((r_th + r2/s[ii])**2 + (x_th + x2)**2))

# رسم منحنی گشتاور-سرعت
plt.figure(1)
plt.plot(nm, t_ind, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{\tau_{ind}}$' + ' (N-m)', fontsize=12, weight='bold')
plt.title(r'$\bf{Induction\ Motor\ Torque-Speed\ Characteristic}$', fontsize=14, weight='bold')
plt.grid(True)

plt.show()
