import numpy as np
import matplotlib.pyplot as plt

# Parameter Sinyal
#Interval Sinyal (Interval -A < t < A)
T = 2.0  # Asumsi A = 1
Fs = 1000  # Sampling frequency
t = np.linspace(-T, T, int(T * Fs), endpoint=False)

# Sinyal Masukan
sign_rect = np.zeros_like(t)
sign_rect[np.logical_and(t >= -T/2, t < T/2)] = 1

# Algoritma FFT
n = len(sign_rect)
yf = np.fft.fft(sign_rect)
xf = np.fft.fftfreq(n, 1/Fs)

# Plot sinyal dan hasil FFT
plt.figure(figsize=(12, 4))

# Plot sinyal masukan
plt.subplot(1, 2, 1)
plt.plot(t, sign_rect)
plt.title('Sinyal')
plt.xlabel('Waktu')
plt.ylabel('Amplitude')
plt.xlim(-2, 2) 

# Plot Sinyal Hasil FFT
plt.subplot(1, 2, 2)
plt.plot(xf, np.abs(yf))
plt.title('FFT')
plt.xlabel('Frekuensi')
plt.ylabel('Amplitude')
plt.xlim(-Fs / 200, Fs / 200) 

plt.tight_layout()
plt.show()

print("Lazuardi Raihan")
print("5009201006")