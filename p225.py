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
r_a = 0.44  # مقاومت آرماچر + مقاومت سری (اهم)
i_l = np.arange(0, 51, 1)  # جریان‌های خطی (آمپر)
n_f = 2700  # تعداد دورهای میدان شانت
n_se = 27  # تعداد دورهای میدان سری

# محاسبه جریان آرماچر برای هر بار بار
i_a = i_l - v_t / (r_f + r_adj)

# محاسبه ولتاژ داخلی تولید شده برای هر جریان آرماچر
e_a = v_t - i_a * r_a

# محاسبه جریان میدان موثر برای هر جریان آرماچر
i_f = v_t / (r_f + r_adj) - (n_se / n_f) * i_a

# محاسبه ولتاژ داخلی تولید شده برای سرعت 1200 ر.دقیقه با استفاده از منحنی مغناطیسی
e_a0 = np.interp(i_f, if_values, ea_values)

# محاسبه سرعت‌ها با استفاده از فرمول (9-13)
n = (e_a / e_a0) * n_0

# محاسبه گشتاور القا شده برای هر سرعت
t_ind = e_a * i_a / (n * 2 * np.pi / 60)

# رسم منحنی گشتاور-سرعت
plt.figure(1)
plt.plot(t_ind, n, 'b-', linewidth=2.0)
plt.xlabel(r'$\bf{\tau_{ind}}$' + ' (N-m)', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{n_{m}}$' + ' (r/min)', fontsize=12, weight='bold')
plt.title(r'$\bf{Differentially-Compounded\ DC\ Motor\ Torque-Speed\ Characteristic}$', fontsize=14, weight='bold')
plt.axis([0, 100, 800, 1600])
plt.grid(True)
plt.show()
