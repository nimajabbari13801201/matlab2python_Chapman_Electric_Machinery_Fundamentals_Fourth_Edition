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
r_a = 0.18  # مقاومت آرماچر + مقاومت سری (اهم)
i_f = np.arange(0, 6.005, 0.005)  # جریان میدان (آمپر)
n = 1800  # سرعت ژنراتور (ر.دقیقه)

# محاسبه Ea بر اساس If
Ea = np.interp(i_f, if_values, ea_values)

# محاسبه Vt بر اساس If
Vt = (r_f + r_adj) * i_f

# محاسبه ولتاژ ترمینال و جریان خط برای هر مقدار از جریان آرماچر
i_a = np.arange(0, 51, 1)  # جریان‌های آرماچر (آمپر)
v_t = np.zeros_like(i_a, dtype=float)
i_l = np.zeros_like(i_a, dtype=float)

for jj in range(len(i_a)):
    # محاسبه اختلاف ولتاژ
    diff = Ea - Vt - i_a[jj] * r_a

    # پیدا کردن نقطه‌ای که اختلاف به منفی تبدیل می‌شود
    was_pos = False
    for ii in range(len(i_f)):
        if diff[ii] > 0:
            was_pos = True
        if diff[ii] < 0 and was_pos:
            break

    # ذخیره ولتاژ ترمینال در این نقطه
    v_t[jj] = Vt[ii]
    i_l[jj] = i_a[jj] - v_t[jj] / (r_f + r_adj)

# رسم ویژگی‌های ترمینال ژنراتور
plt.figure(1)
plt.plot(i_l, v_t, 'b-', linewidth=2.0)

plt.xlabel(r'$\bf{I_L}$ (A)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{V_T}$ (V)', fontsize=12, weight='bold')
plt.title(r'$\bf{Terminal\ Characteristic\ of\ a\ Shunt\ DC\ Generator}$', fontsize=14, weight='bold')

plt.axis([0, 50, 0, 120])
plt.grid(True)
plt.show()
