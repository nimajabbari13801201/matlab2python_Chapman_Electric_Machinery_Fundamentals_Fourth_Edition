import numpy as np
import matplotlib.pyplot as plt

# مقادیر اولیه
r1 = 0.200  # مقاومت استاتور
x1 = 0.410  # واکنش استاتور
r2 = 0.120  # مقاومت روتور
x2 = 0.410  # واکنش روتور
xm = 15.0   # واکنش شاخه مغناطیسی
v_phase = 208 / np.sqrt(3)  # ولتاژ فازی
n_sync = 3600  # سرعت سنکرون (ر.دقیقه)
w_sync = 377    # سرعت سنکرون (راد/ثانیه)

# محاسبه ولتاژ و امپدانس تهونن
v_th = v_phase * (xm / np.sqrt(r1**2 + (x1 + xm)**2))
z_th = ((1j*xm) * (r1 + 1j*x1)) / (r1 + 1j*(x1 + xm))
r_th = np.real(z_th)
x_th = np.imag(z_th)

# محاسبه ویژگی گشتاور-سرعت برای مقادیر مختلف لغزش
s = np.arange(0, 51) / 50  # لغزش
s[0] = 0.001  # برای جلوگیری از تقسیم بر صفر
nm = (1 - s) * n_sync  # سرعت مکانیکی (ر.دقیقه)
wm = (1 - s) * w_sync  # سرعت مکانیکی (راد/ثانیه)

# محاسبه گشتاور و توان خروجی
p_out = np.zeros(51)
for ii in range(51):
    t_ind = (3 * v_th**2 * r2 / s[ii]) / \
            (w_sync * ((r_th + r2/s[ii])**2 + (x_th + x2)**2))
    p_out[ii] = t_ind * wm[ii]

# رسم منحنی گشتاور-سرعت
plt.plot(nm, p_out / 1000, 'k-', linewidth=2.0)  # توان خروجی بر حسب کیلووات
plt.xlabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{P_{OUT}}$' + ' (kW)', fontsize=12, weight='bold')
plt.title(r'$\bf{Induction\ Motor\ Output\ Power\ versus\ Speed}$', fontsize=14, weight='bold')
plt.grid(True)
plt.show()
