# Binary Images have a lot of use cases in Image Processing.
# One of the most common use cases is that of creating masks.
# Image Masks allow us to process on specific parts of an image keeping the other parts intact.
# Image Thresholding is used to create Binary Images from grayscale images.
# You can use different thresholds to create different binary images from the same original image.

import cv2
import matplotlib.pyplot as plt

img_read = cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)
print(img_read)
retval, img_thresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)

# Show the images
plt.figure(figsize=[18, 5])

plt.subplot(121); plt.imshow(img_read, cmap="gray"); plt.title("Original");
plt.subplot(122); plt.imshow(img_thresh, cmap="gray"); plt.title("Thresholded");

plt.show()
print(img_thresh)