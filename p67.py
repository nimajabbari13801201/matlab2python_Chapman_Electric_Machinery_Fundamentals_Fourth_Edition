import numpy as np

def fullwave3(wt):
    """
    تابعی برای شبیه‌سازی خروجی یک یکسوکننده‌ی تمام‌موج سه‌فاز.
    wt: فاز بر حسب رادیان (= امگا × زمان)
    خروجی: دامنه‌ی سیگنال یکسو شده
    """
    # تبدیل wt به بازه‌ی 0 تا 2*pi
    wt = wt % (2 * np.pi)
    
    # محاسبه‌ی ولتاژ لحظه‌ای سه فاز
    a = np.sin(wt)
    b = np.sin(wt - 2 * np.pi / 3)
    c = np.sin(wt + 2 * np.pi / 3)
    
    # ولتاژ خروجی یکسوکننده‌ی تمام‌موج
    return max(a, b, c) - min(a, b, c)

def ripple(waveform):
    """
    تابعی برای محاسبه‌ی ضریب ریپل موج ورودی.
    waveform: آرایه‌ای از مقادیر موج یکسو شده
    خروجی: مقدار ضریب ریپل به درصد (%)
    """
    # محاسبه‌ی مقدار میانگین موج
    average = np.mean(waveform)

    # محاسبه‌ی مقدار RMS موج
    rms = np.sqrt(np.mean(np.square(waveform)))

    # محاسبه‌ی ضریب ریپل
    return np.sqrt((rms / average) ** 2 - 1) * 100

# 📌 اجرای برنامه‌ی تست برای محاسبه‌ی ضریب ریپل خروجی یکسوکننده‌ی تمام‌موج
waveform = np.zeros(128)
for ii in range(128):
    waveform[ii] = fullwave3(ii * np.pi / 64)

# محاسبه‌ی ضریب ریپل
r = ripple(waveform)

# نمایش نتیجه
print(f'The ripple is {r:.4f}%.')
