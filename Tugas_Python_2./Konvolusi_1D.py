# Convolution without modules or library
def convolution_1d(signal, kernel):
    len1, len2 = len(signal), len(kernel)
    result_length = len1 + len2 - 1
    result = [0] * result_length

    for i in range(result_length):
        for j in range(len1):
            if i - j >= 0 and i - j < len2:
                result[i] += signal[j] * kernel[i - j]

    return result

# Define the 1D array or signal
signal = [3, 1, 3, 2, 2]
kernel = [0, 1, 0.5, 4]

convolution_result = convolution_1d(signal, kernel)

print("Naive Implementation of 1D Convolution")
print("Lazuardi Raihan")
print("5009201006")
print(convolution_result)
