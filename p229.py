import numpy as np
import matplotlib.pyplot as plt

# بارگذاری داده‌های منحنی مغناطیسی
data = np.loadtxt('p95_mag.dat')
if_values = data[:, 0]  # مقادیر جریان میدان
ea_values = data[:, 1]  # ولتاژ داخلی تولید شده

n_0 = 1200  # سرعت (ر.دقیقه)

# مقادیر اولیه
v_t = 120  # ولتاژ ترمینال (V)
r_a = 0.36  # مقاومت آرماچر + مقاومت میدان (اهم)
i_a = np.arange(9, 59, 1)  # جریان‌های آرماچر (آمپر)

# محاسبه ولتاژ داخلی تولید شده برای هر جریان آرماچر
e_a = v_t - i_a * r_a

# محاسبه ولتاژ داخلی تولید شده در 1200 ر.دقیقه با استفاده از منحنی مغناطیسی
e_a0 = np.interp(i_a, if_values, ea_values, left=None, right=None)

# محاسبه سرعت‌ها با استفاده از فرمول داده شده
n1 = 1050  # سرعت در بار کامل (1050 ر.دقیقه)
Eao1 = np.interp(58, if_values, ea_values, left=None, right=None)
Ea1 = v_t - 58 * r_a

Eao2 = np.interp(i_a, if_values, ea_values, left=None, right=None)
n = (e_a / Ea1) * (Eao1 / Eao2) * n1

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
