import os
import cv2

def callback(x):
    pass

def average_filter(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Could not read image from {image_path}")
        return

    win_name = 'Average Filter'
    cv2.namedWindow(win_name)
    cv2.createTrackbar('Kernel Size', win_name, 1, 100, callback)  # start at 1

    # Resize image for performance
    height, width = img.shape[:2]
    scale = 0.25
    resized_img = cv2.resize(img, (int(width * scale), int(height * scale)))

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        k = cv2.getTrackbarPos('Kernel Size', win_name)
        k = max(1, k)  # Kernel size must be >= 1
        if k % 2 == 0:
            k += 1  # optional: make kernel size odd for better smoothing

        blurred = cv2.blur(resized_img, (k, k))
        cv2.imshow(win_name, blurred)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    root = os.getcwd()
    image_path = os.path.join(root, 'img_5.png')
    average_filter(image_path)
