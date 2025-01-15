import numpy as np
import matplotlib.pyplot as plt

# تعریف مقادیر ترانسفورماتور
VP = 15000  # ولتاژ اولیه (V)
amps = np.arange(0, 16667, 166.67)  # مقادیر جریان (A)
Req = 0.0135  # مقاومت معادل (اهم)
Xeq = 0.0563  # راکتانس معادل (اهم)

# محاسبه جریان برای سه ضریب توان
I = np.zeros((3, len(amps)), dtype=complex)
I[0, :] = amps * (0.8 - 1j * 0.6)  # ضریب توان 0.8 پس‌فاز
I[1, :] = amps * 1.0               # ضریب توان 1.0
I[2, :] = amps * (0.8 + 1j * 0.6)  # ضریب توان 0.8 پیش‌فاز

# محاسبه ولتاژ ثانویه نسبت به سمت اولیه
aVS = VP - (Req * I + 1j * Xeq * I)

# ارجاع ولتاژ ثانویه به سمت ثانویه
VS = aVS * (200 / 15)

# رسم نمودار ولتاژ ثانویه (به کیلوولت) در برابر بار
plt.plot(amps, np.abs(VS[0, :] / 1000), 'b-', linewidth=2.0, label='0.8 PF lagging')
plt.plot(amps, np.abs(VS[1, :] / 1000), 'k--', linewidth=2.0, label='1.0 PF')
plt.plot(amps, np.abs(VS[2, :] / 1000), 'r-.', linewidth=2.0, label='0.8 PF leading')

# تنظیمات نمودار
plt.title('Secondary Voltage Versus Load')
plt.xlabel('Load (A)')
plt.ylabel('Secondary Voltage (kV)')
plt.legend()
plt.grid(True)
plt.show()
