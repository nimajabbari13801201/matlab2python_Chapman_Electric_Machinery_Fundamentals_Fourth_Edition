import numpy as np
import matplotlib.pyplot as plt

# بارگذاری داده‌های منحنی مغناطیسی
data = np.loadtxt('p97_mag.dat')
if_values = data[:, 0]  # مقادیر جریان میدان
ea_values = data[:, 1]  # ولتاژ داخلی تولید شده

n_0 = 1800  # سرعت ژنراتور (ر.دقیقه)

# مقادیر اولیه
r_f = 24  # مقاومت میدان (اهم)
r_adj = 10  # مقاومت قابل تنظیم (اهم)
r_a = 0.19  # مقاومت آرماچر + مقاومت سری (اهم)
i_f = np.arange(0, 6.02, 0.02)  # جریان میدان (آمپر)
n = 1800  # سرعت ژنراتور (ر.دقیقه)

# محاسبه Ea بر اساس If
Ea = np.interp(i_f, if_values, ea_values)

# محاسبه Vt بر اساس If
Vt = (r_f + r_adj) * i_f

# یافتن نقطه‌ای که اختلاف بین دو منحنی برابر 3.6V باشد
diff = Ea - Vt - 3.6

# پیدا کردن نقطه تلاقی
was_pos = False
for ii in range(len(i_f)):
    if diff[ii] > 0:
        was_pos = True
    if diff[ii] < 0 and was_pos:
        break

# نمایش مقادیر
print(f'Ea = {Ea[ii]:.2f} V')
print(f'Vt = {Vt[ii]:.2f} V')
print(f'If = {i_f[ii]:.2f} A')

# رسم منحنی‌ها
plt.figure(1)
plt.plot(i_f, Ea, 'b-', linewidth=2.0, label=r'$E_a$ line')
plt.plot(i_f, Vt, 'k--', linewidth=2.0, label=r'$V_t$ line')

# رسم نقاط تلاقی
plt.plot([i_f[ii], i_f[ii]], [0, Ea[ii]], 'k-')
plt.plot([0, i_f[ii]], [Vt[ii], Vt[ii]], 'k-')
plt.plot([0, i_f[ii]], [Ea[ii], Ea[ii]], 'k-')

plt.xlabel(r'$\bf{I_F}$ (A)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{E_A}$ or $\bf{V_T}$', fontsize=12, weight='bold')
plt.title(r'$\bf{Plot\ of\ E_A\ and\ V_T\ vs.\ field\ current}$', fontsize=14, weight='bold')

# تنظیمات نمودار
plt.axis([0, 5, 0, 150])
plt.xticks(np.arange(0, 5.5, 0.5))
plt.yticks(np.arange(0, 151, 10))
plt.legend(loc=4)

# نمایش نمودار
plt.grid(True)
plt.show()
