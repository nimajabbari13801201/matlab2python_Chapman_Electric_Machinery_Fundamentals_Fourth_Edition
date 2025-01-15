import numpy as np
import matplotlib.pyplot as plt

# تعریف مقادیر ترانسفورماتور
VL = 13800  # ولتاژ خط اولیه (V)
VPP = VL / np.sqrt(3)  # ولتاژ فاز اولیه (V)
amps = np.arange(0, 12.6, 0.0126)  # مقادیر جریان فاز (A)
Req = 6.94  # مقاومت معادل (اهم)
Xeq = 24.7  # راکتانس معادل (اهم)

# محاسبه جریان برای سه ضریب توان
re = 0.85
im = np.sin(np.arccos(re))

I = np.zeros((3, len(amps)), dtype=complex)
I[0, :] = amps * (re - 1j * im)  # ضریب توان 0.85 پس‌فاز
I[1, :] = amps * 1.0             # ضریب توان 1.0
I[2, :] = amps * (re + 1j * im)  # ضریب توان 0.85 پیش‌فاز

# محاسبه ولتاژ فاز ثانویه نسبت به سمت اولیه
aVSP = VPP - (Req * I + 1j * Xeq * I)

# ارجاع ولتاژ فاز ثانویه به سمت ثانویه (در اتصال دلتا، این ولتاژ همان ولتاژ خط است)
VSP = aVSP * (480 / 7967)

# رسم نمودار ولتاژ ثانویه در برابر بار
plt.plot(amps, np.abs(VSP[0, :]), 'b-', linewidth=2.0, label='0.85 PF lagging')
plt.plot(amps, np.abs(VSP[1, :]), 'k--', linewidth=2.0, label='1.0 PF')
plt.plot(amps, np.abs(VSP[2, :]), 'r-.', linewidth=2.0, label='0.85 PF leading')

# تنظیمات نمودار
plt.title('Secondary Voltage Versus Load')
plt.xlabel('Load (A)')
plt.ylabel('Secondary Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()
