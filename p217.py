import numpy as np
import matplotlib.pyplot as plt

# بارگذاری داده‌های منحنی مغناطیسی
data = np.loadtxt('p91_mag.dat')
if_values = data[:, 0]  # مقادیر جریان میدان
ea_values = data[:, 1]  # ولتاژ داخلی تولید شده

n_0 = 1200  # سرعت (ر.دقیقه)

# مقادیر اولیه
v_t = 240  # ولتاژ ترمینال (V)
r_f = 100  # مقاومت میدان (اهم)
r_adj = 175  # مقاومت قابل تنظیم (اهم)
r_a = 0.40  # مقاومت آرماچر (اهم)
i_l = np.arange(0, 56, 1)  # جریان‌های خطی (آمپر)
n_f = 2700  # تعداد دورهای میدان
f_ar0 = 1200  # واکنش آرماچر در 55 آمپر (A-t/m)

# محاسبه جریان آرماچر برای هر بار بار
i_a = i_l - v_t / (r_f + r_adj)

# محاسبه ولتاژ داخلی تولید شده برای هر جریان آرماچر
e_a = v_t - i_a * r_a

# محاسبه واکنش آرماچر (MMF) برای هر جریان آرماچر
f_ar = (i_a / 55) * f_ar0

# محاسبه جریان میدان موثر با و بدون واکنش آرماچر
i_f_ar = v_t / (r_f + r_adj) - f_ar / n_f
i_f_noar = v_t / (r_f + r_adj)

# محاسبه ولتاژ داخلی تولید شده برای سرعت 1200 ر.دقیقه با استفاده از منحنی مغناطیسی
e_a0_ar = np.interp(i_f_ar, if_values, ea_values)
e_a0_noar = np.interp(i_f_noar, if_values, ea_values)

# محاسبه سرعت‌ها با استفاده از فرمول (9-13)
n_ar = (e_a / e_a0_ar) * n_0
n_noar = (e_a / e_a0_noar) * n_0

# محاسبه گشتاور القا شده برای هر سرعت
t_ind_ar = e_a * i_a / (n_ar * 2 * np.pi / 60)
t_ind_noar = e_a * i_a / (n_noar * 2 * np.pi / 60)

# رسم منحنی گشتاور-سرعت
plt.figure(1)
plt.plot(t_ind_noar, n_noar, 'b-', linewidth=2.0, label='No armature reaction')
plt.plot(t_ind_ar, n_ar, 'k--', linewidth=2.0, label='With armature reaction')
plt.xlabel(r'$\bf{\tau_{ind}}$' + ' (N-m)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.title(r'$\bf{Shunt\ DC\ Motor\ Torque-Speed\ Characteristic}$', fontsize=14, weight='bold')
plt.legend()
plt.axis([0, 125, 800, 1250])
plt.grid(True)
plt.show()
