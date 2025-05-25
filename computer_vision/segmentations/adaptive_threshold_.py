import cv2
import matplotlib.pyplot as plt
import os


# Read image in grayscale
img = cv2.imread('../img.png', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Mean thresholding
thresh_mean = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
) #

# Gaussian thresholding
thresh_gauss = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

# Titles and images
titles = ['Original Image', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, thresh_mean, thresh_gauss]

# Plot
for i in range(3):
    plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
