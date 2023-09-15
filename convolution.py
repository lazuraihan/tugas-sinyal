import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Load the image
img = Image.open('image.jpg')
plt.imshow(img)
plt.show()
# Ubah image ke grayscale
img = img.convert('L')
# Convert image ke array
img = np.array(img)

def convolve2D(image, kernel):
    # Dimensi image dan kernel
    i_h, i_w = image.shape
    k_h, k_w = kernel.shape

    # Perhitungan dimensi matrix
    o_h = i_h - k_h + 1
    o_w = i_w - k_w + 1

    # Initialize the output array
    output = np.zeros((o_h, o_w))

    # Proses Filter Kernel 
    for y in range(o_h):
        for x in range(o_w):
            output[y][x] = np.sum(image[y:y+k_h, x:x+k_w] * kernel)

    return output

#Identitas
print("Nama: Lazuardi Raihan")
print("NRP: 5009201006")

# Define the mean kernel
kernel = np.ones((3,3)) / 9

# Apply the convolution
convolved_img = convolve2D(img, kernel)

plt.imshow(convolved_img)
plt.show()





