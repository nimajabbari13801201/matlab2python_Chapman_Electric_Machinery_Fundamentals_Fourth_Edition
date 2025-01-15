import numpy as np
import matplotlib.pyplot as plt

# بارگذاری داده‌های منحنی مغناطیسی
data = np.loadtxt('p96_mag.dat')
if_values = data[:, 0]  # مقادیر جریان میدان
ea_values = data[:, 1]  # ولتاژ داخلی تولید شده

n_0 = 1200  # سرعت (ر.دقیقه)

# مقادیر اولیه
v_t = 240  # ولتاژ ترمینال (V)
r_a = 0.19  # مقاومت آرماچر + مقاومت سری (اهم)
i_l = np.arange(20, 46, 1)  # جریان‌های خط (آمپر)
n_f = 1500  # تعداد دورهای میدان شنت
n_se = 12  # تعداد دورهای میدان سری

# محاسبه جریان آرماچر برای هر بار
i_a = i_l

# محاسبه ولتاژ داخلی تولید شده برای هر جریان آرماچر
e_a = v_t - i_a * r_a

# محاسبه جریان موثر میدان برای هر جریان آرماچر
i_f = (n_se / n_f) * i_a

# محاسبه ولتاژ داخلی تولید شده در 1800 ر.دقیقه با استفاده از منحنی مغناطیسی
e_a0 = np.interp(i_f, if_values, ea_values, left=None, right=None)

# محاسبه سرعت با استفاده از فرمول داده شده
n = (e_a / e_a0) * n_0

# محاسبه گشتاور القا شده برای هر سرعت
t_ind = e_a * i_a / (n * 2 * np.pi / 60)

# رسم منحنی گشتاور-سرعت
plt.figure(1)
plt.plot(t_ind, n, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{\tau_{ind}}$' + ' (N-m)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.title(r'$\bf{Series\ DC\ Motor\ Torque-Speed\ Characteristic}$', fontsize=14, weight='bold')
plt.grid(True)
plt.show()
