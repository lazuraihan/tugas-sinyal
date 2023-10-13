import numpy as np
import matplotlib.pyplot as plt

# Tentukan Ukuran Matriks 2D
width, height = 9, 9

# Isi matriks dengan nilai 0 
signal_1d = np.zeros(width * height)

# Konversi matriks 1D ke matriks 2d
# Sinyal interval -A/2 < t < A/2
signal_2d = np.reshape(signal_1d, (width, height))
signal_2d[:,6] = 1

# Algoritma FFT 2D
signal_fft = np.fft.fft2(signal_2d)

# Posisikan hasil FFT di tengah spektrum
signal_fft_shifted = np.fft.fftshift(signal_fft)

# Hitung nilai besaran spektrum
magnitude_spectrum = np.abs(signal_fft_shifted)

# Plot sinyal asli dan sinyal hasil FFT
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Sinyal Asli 2D')
plt.imshow(signal_2d, cmap='Greens')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('FFT 2D')
plt.imshow(magnitude_spectrum, cmap='Oranges')
plt.colorbar()
plt.show()