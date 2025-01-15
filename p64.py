import numpy as np

def halfwave3(wt):
    """
    تابعی برای شبیه‌سازی خروجی یک یکسوکننده‌ی نیم‌موج سه‌فاز.
    wt: فاز بر حسب رادیان (= امگا × زمان)
    خروجی: بیشترین مقدار ولتاژ لحظه‌ای از سه فاز
    """
    # تبدیل wt به بازه‌ی 0 تا 2*pi
    wt = wt % (2 * np.pi)
    
    # محاسبه‌ی ولتاژ لحظه‌ای سه فاز
    a = np.sin(wt)
    b = np.sin(wt - 2 * np.pi / 3)
    c = np.sin(wt + 2 * np.pi / 3)
    
    # ولتاژ خروجی یکسوکننده (بیشترین مقدار بین سه فاز)
    return max(a, b, c)

def ripple(waveform):
    """
    تابعی برای محاسبه‌ی ضریب ریپل موج ورودی.
    waveform: آرایه‌ای از مقادیر موج یکسو شده
    خروجی: مقدار ضریب ریپل به درصد (%)
    """
    nvals = len(waveform)

    # محاسبه‌ی مقدار میانگین موج
    average = np.mean(waveform)

    # محاسبه‌ی مقدار RMS موج
    rms = np.sqrt(np.mean(np.square(waveform)))

    # محاسبه‌ی ضریب ریپل
    return np.sqrt((rms / average) ** 2 - 1) * 100

# 📌 اجرای برنامه‌ی تست برای محاسبه‌ی ضریب ریپل خروجی یکسوکننده
waveform = np.zeros(128)
for ii in range(128):
    waveform[ii] = halfwave3(ii * np.pi / 64)

# محاسبه‌ی ضریب ریپل
r = ripple(waveform)

# نمایش نتیجه
print(f'The ripple is {r:.4f}%.')
