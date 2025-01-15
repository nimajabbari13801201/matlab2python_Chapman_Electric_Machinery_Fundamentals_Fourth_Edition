import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# بارگذاری داده‌های منحنی مغناطیس‌شدگی
p22_mag = np.loadtxt('p22_mag.dat')
mmf_data = p22_mag[:, 0]  # ستون اول: mmf
flux_data = p22_mag[:, 1]  # ستون دوم: شار مغناطیسی

# مقداردهی اولیه
S = 1000  # توان ظاهری (VA)
Vrms = 240  # ولتاژ موثر (V)
VM = Vrms * np.sqrt(2)  # ولتاژ بیشینه (V)
NP = 1000  # تعداد دور اولیه

# محاسبه فرکانس زاویه‌ای برای 50 هرتز
freq = 50  # فرکانس (Hz)
w = 2 * np.pi * freq

# محاسبه شار نسبت به زمان
time = np.arange(0, 1/25, 1/2500)  # بازه‌ی زمانی
flux = -VM / (w * NP) * np.cos(w * time)

# محاسبه‌ی mmf متناظر با شار مغناطیسی با استفاده از درونیابی
interp_func = interp1d(flux_data, mmf_data, fill_value="extrapolate")
mmf = interp_func(flux)

# محاسبه‌ی جریان مغناطیس‌شدگی
im = mmf / NP

# محاسبه مقدار rms جریان
irms = np.sqrt(np.mean(im ** 2))
print(f'The rms current at 50 Hz is {irms:.4f} A')

# محاسبه جریان نامی و درصد جریان مغناطیس‌شدگی از جریان نامی
i_fl = S / Vrms
percnt = (irms / i_fl) * 100
print(f'The magnetization current is {percnt:.2f}% of full-load current.')

# رسم نمودار جریان مغناطیس‌شدگی
plt.figure(figsize=(8, 5))
plt.plot(time, im, label='Magnetization Current')
plt.title('Magnetization Current at 240 V and 50 Hz', fontsize=12, fontweight='bold')
plt.xlabel('Time (s)', fontsize=10, fontweight='bold')
plt.ylabel(r'$I_m$ (A)', fontsize=10, fontweight='bold')
plt.axis([0, 0.04, -0.5, 0.5])
plt.grid(True)
plt.legend()
plt.show()
