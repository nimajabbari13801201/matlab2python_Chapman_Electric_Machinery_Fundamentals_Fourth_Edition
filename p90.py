import numpy as np

def biphase_controller(wt, theta0, fire):
    """
    شبیه‌سازی خروجی یک کنترل‌کننده‌ی زاویه‌ی فاز دو‌فاز (Biphase Controller)
    که روی نیم‌سیکل‌های مثبت و منفی به‌صورت متقارن عمل می‌کند.

    پارامترها:
    wt: فاز جاری بر حسب درجه
    theta0: زاویه‌ی فاز اولیه بر حسب درجه
    fire: زاویه‌ی آتش (Firing Angle) بر حسب درجه

    خروجی:
    volts: مقدار ولتاژ خروجی کنترل‌کننده
    """

    # تبدیل درجه به رادیان
    deg2rad = np.pi / 180

    # حذف ابهام فازی و محدود کردن زاویه به بازه‌ی ۰ تا ۳۶۰ درجه
    ang = (wt + theta0) % 360

    # شبیه‌سازی عملکرد کنترل‌کننده‌ی زاویه‌ی فاز
    if fire <= ang <= 180 or (fire + 180) <= ang <= 360:
        volts = 170 * np.sin(ang * deg2rad)
    else:
        volts = 0

    return volts
