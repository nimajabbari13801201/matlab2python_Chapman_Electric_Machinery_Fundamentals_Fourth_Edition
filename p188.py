import numpy as np
import matplotlib.pyplot as plt

# مقادیر اولیه
r1 = 0.075   # مقاومت استاتور
x1 = 0.170   # واکنش استاتور
r2 = 0.065   # مقاومت روتور
x2 = 0.170   # واکنش روتور
xm = 7.2     # واکنش شاخه مغناطیسی
v_phase = 440 / np.sqrt(3)  # ولتاژ فازی
n_sync = 3000  # سرعت سنکرون (ر.دقیقه)
w_sync = 314.2  # سرعت سنکرون (راد/ثانیه)
p_mech = 1000  # تلفات مکانیکی (وات)
p_core = 1100  # تلفات هسته (وات)
p_misc = 150   # تلفات متفرقه (وات)

# محاسبه ولتاژ و امپدانس تهونن
v_th = v_phase * (xm / np.sqrt(r1**2 + (x1 + xm)**2))
z_th = ((1j*xm) * (r1 + 1j*x1)) / (r1 + 1j*(x1 + xm))
r_th = np.real(z_th)
x_th = np.imag(z_th)

# محاسبه ویژگی گشتاور-سرعت برای مقادیر مختلف لغزش
s = np.arange(0, 0.101, 0.001)  # لغزش
s[0] = 0.001  # برای جلوگیری از تقسیم بر صفر
nm = (1 - s) * n_sync  # سرعت مکانیکی (ر.دقیقه)
wm = nm * 2 * np.pi / 60  # سرعت مکانیکی (راد/ثانیه)

# محاسبه گشتاور، توان تبدیل شده، توان خروجی و بازده
t_ind = np.zeros(len(s))
p_conv = np.zeros(len(s))
p_out = np.zeros(len(s))
p_in = np.zeros(len(s))
eff = np.zeros(len(s))

for ii in range(len(s)):
    # گشتاور القا شده
    t_ind[ii] = (3 * v_th**2 * r2 / s[ii]) / \
                (w_sync * ((r_th + r2/s[ii])**2 + (x_th + x2)**2))

    # توان تبدیل شده
    p_conv[ii] = t_ind[ii] * wm[ii]

    # توان خروجی
    p_out[ii] = p_conv[ii] - p_mech - p_core - p_misc

    # توان ورودی
    zf = 1 / (1 / (1j*xm) + 1 / (r2 / s[ii] + 1j*x2))
    ia = v_phase / (r1 + 1j*x1 + zf)
    p_in[ii] = 3 * v_phase * np.abs(ia) * np.cos(np.arctan(np.imag(ia) / np.real(ia)))

    # بازده
    eff[ii] = p_out[ii] / p_in[ii] * 100

# رسم منحنی گشتاور-سرعت
plt.figure(1)
plt.plot(nm, t_ind, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{\tau_{ind}}$' + ' (N-m)', fontsize=12, weight='bold')
plt.title(r'$\bf{Induced\ Torque\ versus\ Speed}$', fontsize=14, weight='bold')
plt.grid(True)

# رسم منحنی توان تبدیل شده
plt.figure(2)
plt.plot(nm, p_conv / 1000, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{P_{conv}}$' + ' (kW)', fontsize=12, weight='bold')
plt.title(r'$\bf{Power\ Converted\ versus\ Speed}$', fontsize=14, weight='bold')
plt.grid(True)

# رسم منحنی توان خروجی
plt.figure(3)
plt.plot(nm, p_out / 1000, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{P_{out}}$' + ' (kW)', fontsize=12, weight='bold')
plt.title(r'$\bf{Output\ Power\ versus\ Speed}$', fontsize=14, weight='bold')
plt.axis([2700, 3000, 0, 180])
plt.grid(True)

# رسم منحنی بازده
plt.figure(4)
plt.plot(nm, eff, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{\eta}$' + ' (%)', fontsize=12, weight='bold')
plt.title(r'$\bf{Efficiency\ versus\ Speed}$', fontsize=14, weight='bold')
plt.grid(True)

plt.show()
