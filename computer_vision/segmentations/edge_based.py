import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../img.png', cv2.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"

# before applying Canny edge detection good to use blurred.
blurred = cv2.GaussianBlur(image, (5, 5), 0)

