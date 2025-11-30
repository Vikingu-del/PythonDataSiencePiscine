import cv2
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

matrix_low_contrast = np.ones(img_rgb.shape) * 0.8
matrix_high_contrast = np.ones(img_rgb.shape) * 1.2

img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb), matrix_low_contrast))
img_rgb_brighter = np.uint8(cv2.multiply(np.float64(img_rgb), matrix_high_contrast))

# Show the images
# plt.figure(figsize=[18, 5])
# plt.subplot(131); plt.imshow(img_rgb_darker); plt.title("Lower Contrast");
# plt.subplot(132); plt.imshow(img_rgb); plt.title("Original");
# plt.subplot(133); plt.imshow(img_rgb_brighter); plt.title("Brighter Contrast");
# plt.show()

# The issue is that after multiplying, the values which are already high, are becoming greater 
# than 255. Thus, the overflow issue. How do we overcome this?

# Handling Overflow using np.clip
img_rgb_darker  = np.uint8(cv2.multiply(np.float64(img_rgb), matrix_low_contrast))
img_rgb_brighter = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix_high_contrast), 0, 255))

# show the images
plt.figure(figsize=[18, 5])
plt.subplot(131); plt.imshow(img_rgb_darker); plt.title("Lower Contrast");
plt.subplot(132); plt.imshow(img_rgb); plt.title("Original");
plt.subplot(133); plt.imshow(img_rgb_brighter); plt.title("Brighter Contrast");

plt.show()