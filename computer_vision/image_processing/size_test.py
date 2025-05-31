import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img_1.png')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

scale_factor_1 = 3.0
scale_factor_2 = 1 / 3.0

height, width = rgb_image.shape[:2]

new_height = int(height * scale_factor_1)
new_width = int(width * scale_factor_1)
print("old height: {}, old width: {}".format(height, width))
print("new height: {}, new width: {}".format(new_height, new_width))
zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

# plt.figure(figsize=(10, 5))
# plt.subplot(121), plt.imshow(rgb_image), plt.title('original image'), plt.axis('off')
# plt.subplot(122), plt.imshow(zoomed_image), plt.title('zoomed image'), plt.axis('off')
# plt.tight_layout()
# plt.show()
cv2.imshow('Original', rgb_image)
cv2.imshow("zoomed image", zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()