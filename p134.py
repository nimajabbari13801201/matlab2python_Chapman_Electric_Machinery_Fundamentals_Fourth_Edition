import numpy as np
import matplotlib.pyplot as plt

# مقادیر این ژنراتور
EA = 509  # ولتاژ داخلی ژنراتور (V)
I = 361   # جریان (A)
R = 0.04  # مقاومت (Ω)
X = 0.695 # reactance (Ω)

# محاسبه زاویه امپدانس theta (درجه)
theta = np.arange(-31.8, 31.8 + 0.318, 0.318)
th = np.radians(theta)  # تبدیل به رادیان

# محاسبه ولتاژ فازی و ولتاژ ترمینال
VP = np.sqrt(EA**2 - (X * I * np.cos(th) - R * I * np.sin(th))**2) - R * I * np.cos(th) - X * I * np.sin(th)
VT = VP * np.sqrt(3)

# رسم نمودار ولتاژ ترمینال بر حسب زاویه امپدانس
plt.plot(theta, np.abs(VT), 'b-', linewidth=2.0)
plt.title(r'$\bf{Terminal\ Voltage\ Versus\ Impedance\ Angle}$', fontsize=14, weight='bold')
plt.xlabel(r'$\bf{Impedance\ Angle\ (deg)}$', fontsize=12, weight='bold')
plt.ylabel(r'$\bf{Terminal\ Voltage\ (V)}$', fontsize=12, weight='bold')
plt.grid(True)
plt.show()
