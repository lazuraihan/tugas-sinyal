import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    twiddle_factors = [np.exp(-2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    twiddle_factors = [np.exp(2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)]

def fft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = fft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

def fmcc(matrix):
    # FFT
    fft_matrix = fft2d(matrix)

    # Log Spectrogram
    log_spectrum = np.log(np.abs(fft_matrix) ** 2 + 1e-10)

    # Inverse FFT
    cepstrum = ifft2d(log_spectrum)

    return cepstrum

def ifft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = ifft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = ifft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

def display_matrix(matrix, title):
    plt.imshow(np.abs(matrix), cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.show()

# Example usage with a different input matrix
input_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],


]

for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
        input_matrix[i][j] += i + j  # Modify matrix values

fmcc_result = fmcc(input_matrix)

# Tampilkan Matriks
display_matrix(input_matrix, 'Input Matrix')

# Display the result of FMCC implementation
display_matrix(fmcc_result, 'FMCC')