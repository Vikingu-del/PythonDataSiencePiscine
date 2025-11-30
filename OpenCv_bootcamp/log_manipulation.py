import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# img_log_manipulated = cv2.imread("Logo_Manipulation.png")
# img_log_manipulated = cv2.cvtColor(img_log_manipulated, cv2.COLOR_BGR2RGB)
# plt.imshow(img_log_manipulated, cmap="gray"); plt.title("manipulated logo")
# plt.show()

# load logo image
img_bgr = cv2.imread("coca-cola-logo.png")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

print(img_rgb.shape)

logo_h = img_rgb.shape[0]
logo_w = img_rgb.shape[1]

plt.figure(figsize=[20, 10])
plt.subplot(331); plt.imshow(img_rgb, cmap="gray"); plt.title("redlogo")

# load background image
img_background_bgr = cv2.imread("checkerboard_color.png")
img_background_rgb = cv2.cvtColor(img_background_bgr, cv2.COLOR_BGR2RGB)
# resize to the log image
img_background_rgb = cv2.resize(img_background_rgb, (logo_w, logo_h), interpolation=cv2.INTER_AREA)
plt.subplot(332); plt.imshow(img_background_rgb, cmap="gray"); plt.title("background")

# Create mask for original Image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
# Apply global thresholding to create a binary mask of the logo
retval, img_mask = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
plt.subplot(333); plt.imshow(img_mask, cmap="gray"); plt.title("img_gray_mask")

# Invert the mask
img_mask_inv = cv2.bitwise_not(img_mask)
plt.subplot(334); plt.imshow(img_mask_inv, cmap="gray"); plt.title("img_gray_mask_inv")

# Apply background on the mask
img_background_mask = cv2.bitwise_and(img_background_rgb, img_background_rgb, mask=img_mask)
plt.subplot(335); plt.imshow(img_background_mask, cmap="gray"); plt.title("img_bacground_mask")

# Isolate foreground from image
img_foreground = cv2.bitwise_and(img_rgb, img_rgb, mask=img_mask_inv)
plt.subplot(336); plt.imshow(img_foreground, cmap="gray"); plt.title("img_foreground")


# Result: Merge Foreground and Background
img_result = cv2.bitwise_or(img_foreground, img_background_mask, mask=None)
plt.subplot(337); plt.imshow(img_result, cmap="gray"); plt.title("final_logo")

result = cv2.add(img_background_mask, img_foreground)
plt.subplot(338); plt.imshow(result, cmap="gray"); plt.title("final_logo2")
cv2.imwrite("logo_final.png", result[:, :, ::-1])


plt.show()