# داده‌های مربوط به منحنی مغناطیس‌کنندگی را از فایل p22_mag.dat بارگذاری می‌کند.
# مقدار شار مغناطیسی را با توجه به ولتاژ و فرکانس ورودی محاسبه می‌کند.
# مقدار نیروی مغناطیس‌کنندگی (MMF) را با مقداردهی درونی (interp1) از منحنی استخراج می‌کند.
# جریان مغناطیس‌کنندگی را محاسبه کرده و مقدار RMS آن را تعیین می‌کند.
# نسبت درصدی جریان مغناطیس‌کنندگی به جریان نامی را محاسبه کرده و نمایش می‌دهد.
# نمودار جریان مغناطیس‌کنندگی را برحسب زمان ترسیم می‌کند.

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# بارگذاری داده‌های منحنی مغناطیس‌کنندگی (فرض بر این است که داده‌ها در فایل p22_mag.dat ذخیره شده‌اند)
data = np.loadtxt('p22_mag.dat')
mmf_data = data[:, 0]  # نیروی مغناطیس‌کنندگی
flux_data = data[:, 1]  # شار مغناطیسی

# مقداردهی اولیه متغیرها
S = 1000  # توان ظاهری (VA)
Vrms = 120  # ولتاژ مؤثر (V)
VM = Vrms * np.sqrt(2)  # ولتاژ ماکزیمم (V)
NP = 500  # تعداد دور اولیه
freq = 60  # فرکانس (Hz)
w = 2 * np.pi * freq  # سرعت زاویه‌ای

# محاسبه بردار زمان
time = np.arange(0, 1/30, 1/3000)  # از 0 تا 1/30 ثانیه با گام 1/3000

# محاسبه شار مغناطیسی بر حسب زمان
flux = -VM / (w * NP) * np.cos(w * time)

# مقداردهی درونی برای بدست آوردن mmf متناظر با شار مغناطیسی
interp_func = interp1d(flux_data, mmf_data, fill_value='extrapolate')
mmf = interp_func(flux)

# محاسبه جریان مغناطیس‌کنندگی
im = mmf / NP

# محاسبه مقدار RMS جریان
irms = np.sqrt(np.mean(im**2))
print(f'The rms current at 120 V and 60 Hz is {irms:.4f} A')

# محاسبه جریان نامی و درصد جریان مغناطیس‌کنندگی نسبت به جریان نامی
i_fl = S / Vrms
percnt = (irms / i_fl) * 100
print(f'The magnetization current is {percnt:.2f}% of full-load current.')

# رسم نمودار جریان مغناطیس‌کنندگی
plt.figure(figsize=(8, 5))
plt.plot(time, im, label='Magnetization Current')
plt.title('Magnetization Current at 120V and 60Hz', fontsize=12, fontweight='bold')
plt.xlabel('Time (s)', fontsize=10, fontweight='bold')
plt.ylabel(r'$I_m$ (A)', fontsize=10, fontweight='bold')
plt.axis([0, 0.04, -0.5, 0.5])
plt.grid(True)
plt.legend()
plt.show()
