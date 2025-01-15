import numpy as np
import matplotlib.pyplot as plt

# بارگذاری داده‌ها (به فرض اینکه فایل‌ها در فرمت CSV باشند)
# برای استفاده در پایتون باید داده‌ها را به فرمت قابل استفاده بارگذاری کنید
# فرض می‌کنیم که داده‌ها در فایل‌های CSV هستند
occ_data = np.loadtxt('p52_occ.csv', delimiter=',')  # داده‌های ویژگی مدار باز
scc_data = np.loadtxt('p52_scc.csv', delimiter=',')  # داده‌های ویژگی مدار کوتاه

# استخراج داده‌ها از هر دو فایل
if_occ = occ_data[:, 0]  # جریان میدان از داده‌های مدار باز
vt_occ = occ_data[:, 1]  # ولتاژ ترمینال از داده‌های مدار باز

if_scc = scc_data[:, 0]  # جریان میدان از داده‌های مدار کوتاه
ia_scc = scc_data[:, 1]  # جریان آرماتور از داده‌های مدار کوتاه

# محاسبه Xs (مقاومت سنکرون)
If = np.arange(0.001, 1.02, 0.02)  # گام‌های جریان
vt = np.interp(If, if_occ, vt_occ)  # ولتاژ ترمینال با استفاده از درونیابی
ia = np.interp(If, if_scc, ia_scc)  # جریان با استفاده از درونیابی
Xs = (vt / np.sqrt(3)) / ia  # محاسبه Xs

# رسم نمودار Xs
plt.plot(If, Xs, linewidth=2.0)
plt.title(r'$\bf{Saturated\ Synchronous\ Reactance}\ X_s$', fontsize=14, weight='bold')
plt.xlabel(r'$\bf{Field\ Current\ (A)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{X_s\ (Ohm)}$', fontsize=12, weight='bold')
plt.grid(True)
plt.show()
