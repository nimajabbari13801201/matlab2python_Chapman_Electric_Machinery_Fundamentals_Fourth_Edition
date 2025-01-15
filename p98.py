import numpy as np
import matplotlib.pyplot as plt

# Define the vref function (you may need to define this based on your system)
def vref(t, T):
    # This is a placeholder for the actual vref function
    # Replace with the correct function if needed
    return 100 * np.sin(2 * np.pi * t / T)

# Initialize variables
fs = 20000  # Sampling frequency (Hz)
t = np.arange(0, 4/15, 1/fs)  # Time in seconds
vx = np.zeros_like(t)  # vx
vy = np.zeros_like(t)  # vy
vin = np.zeros_like(t)  # Driving signal
vu = np.zeros_like(t)  # vu
vv = np.zeros_like(t)  # vv
vout = np.zeros_like(t)  # Output signal
fr = 1000  # Frequency of reference signal
T = 1 / fr  # Period of reference signal


def vout_function(vin, vx, vy):
    """
    Function to calculate the output voltage of a PWM modulator
    from the values of vin and the reference voltages vx and vy.
    This function arbitrarily assumes that VDC = 100 V.
    
    Parameters:
    vin: Input voltage
    vx: x reference
    vy: y reference
    
    Returns:
    vout: Output voltage
    vu: Component of output voltage for vx
    vv: Component of output voltage for vy
    """
    # Initialize vu and vv
    if vin > vx:
        vu = 100
    else:
        vu = 0
        
    if vin >= vy:
        vv = 0
    else:
        vv = 100
    
    # Calculate vout
    vout = vv - vu
    
    return vout, vu, vv

# Calculate vx at fr = 1000 Hz
for ii in range(len(t)):
    vx[ii] = vref(t[ii], T)
    vy[ii] = -vx[ii]

# Calculate vin as a 50 Hz sine wave with a peak voltage of 10 V
for ii in range(len(t)):
    vin[ii] = 10 * np.sin(2 * np.pi * 50 * t[ii])

# Now calculate vout
for ii in range(len(t)):
    # Call the vout function (from earlier)
    vout[ii], vu[ii], vv[ii] = vout_function(vin[ii], vx[ii], vy[ii])


# Plot the reference voltages vs time
plt.figure(1)
plt.plot(t, vx, 'b', linewidth=1.0, label='vx')
plt.plot(t, vy, 'k--', linewidth=1.0, label='vy')
plt.title('Reference Voltages for fr = 1000 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.axis([0, 1/30, -10, 10])
plt.show()

# Plot the input voltage vs time
plt.figure(2)
plt.plot(t, vin, 'b', linewidth=1.0)
plt.title('Input Voltage')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.axis([0, 1/30, -10, 10])
plt.show()

# Plot the output voltages versus time
plt.figure(3)
plt.plot(t, vout, 'b', linewidth=1.0)
plt.title('Output Voltage for fr = 1000 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.axis([0, 1/30, -120, 120])
plt.show()

# Now calculate the spectrum of the output voltage
spec = np.fft.fft(vout)
len_t = len(t)
df = fs / len_t
fstep = np.zeros_like(t)
for ii in range(1, len_t//2):
    fstep[ii] = df * (ii - 1)
    fstep[len_t - ii] = -fstep[ii]

# Plot the spectrum
plt.figure(4)
plt.plot(np.fft.fftshift(fstep), np.fft.fftshift(np.abs(spec)))
plt.title('Spectrum of Output Voltage for fr = 1000 Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

# Plot a closeup of the near spectrum (positive side only)
plt.figure(5)
plt.plot(np.fft.fftshift(fstep), np.fft.fftshift(np.abs(spec)))
plt.title('Spectrum of Output Voltage for fr = 1000 Hz')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim([0, 1000])
plt.show()
