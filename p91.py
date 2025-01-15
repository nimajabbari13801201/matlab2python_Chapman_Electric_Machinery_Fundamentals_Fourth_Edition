import numpy as np
import matplotlib.pyplot as plt

def biphase_controller(wt, theta0, fire):
    """
    شبیه‌سازی خروجی کنترل‌کننده‌ی زاویه‌ی فاز دو‌فاز (Biphase Controller) 
    برای یکسوکننده‌ی سه‌فاز.
    
    wt: زاویه‌ی لحظه‌ای (درجه)
    theta0: زاویه‌ی اولیه‌ی فاز (درجه)
    fire: زاویه‌ی آتش (درجه)
    
    خروجی: مقدار ولتاژ در لحظه‌ی موردنظر
    """
    deg2rad = np.pi / 180
    ang = (wt + theta0) % 360  # نرمال‌سازی زاویه بین 0 تا 360 درجه
    
    if fire <= ang <= 180 or (fire + 180) <= ang <= 360:
        return 170 * np.sin(ang * deg2rad)
    else:
        return 0

def ripple(waveform):
    """
    محاسبه‌ی ضریب ریپل از روی شکل موج ورودی.
    """
    avg = np.mean(waveform)
    rms = np.sqrt(np.mean(np.square(waveform)))
    return np.sqrt((rms / avg) ** 2 - 1) * 100

# ** محاسبه‌ی ولتاژهای سه‌فاز **
t = np.arange(0, 1/30, 1/21600)  # زمان از 0 تا 1/30 ثانیه با گام 1/21600
va = np.array([biphase_controller(21600 * ti, 0, 90) for ti in t])
vb = np.array([biphase_controller(21600 * ti, -120, 90) for ti in t])
vc = np.array([biphase_controller(21600 * ti, 120, 90) for ti in t])

# ** محاسبه‌ی ولتاژ خروجی یکسوکننده **
out = np.array([max(va[i], vb[i], vc[i]) - min(va[i], vb[i], vc[i]) for i in range(len(t))])

# ** محاسبه و نمایش مقدار ریپل **
ripple_value = ripple(out)
print(f'The ripple is {ripple_value:.2f}%')

# ** رسم نمودار ولتاژهای سه‌فاز **
plt.figure(figsize=(10, 5))
plt.plot(t, va, 'b', linewidth=2, label='Phase a')
plt.plot(t, vb, 'r:', linewidth=2, label='Phase b')
plt.plot(t, vc, 'k--', linewidth=2, label='Phase c')
plt.title('Phase Voltages')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()

# ** رسم نمودار ولتاژ خروجی یکسوکننده **
plt.figure(figsize=(10, 5))
plt.plot(t, out, 'b', linewidth=2)
plt.title('Output Voltage')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.ylim(0, 260)
plt.grid(True)
plt.show()
