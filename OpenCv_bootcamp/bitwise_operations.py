import cv2
import matplotlib.pyplot as plt


img_rec = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_cir = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=[20, 8])
plt.subplot(231);plt.imshow(img_rec, cmap="gray"); plt.title("Original rect")
plt.subplot(232);plt.imshow(img_cir, cmap="gray"); plt.title("Original circle")
print(img_rec.shape)

# Bitwise AND Operator
result_and = cv2.bitwise_and(img_rec, img_cir, mask=None)
plt.subplot(233); plt.imshow(result_and, cmap="gray"); plt.title("Bitwise And")
print(result_and.shape)

result_or = cv2.bitwise_or(img_rec, img_cir, mask=None)
plt.subplot(234); plt.imshow(result_or, cmap="gray"); plt.title("Bitwise Or")
print(result_or.shape)

result_xor = cv2.bitwise_xor(img_rec, img_cir, mask=None)
plt.subplot(235); plt.imshow(result_xor, cmap="gray"); plt.title("Bitwise Xor")
print(result_xor.shape)

result_xor = cv2.bitwise_xor(img_rec, img_cir, mask=None)
plt.subplot(235); plt.imshow(result_xor, cmap="gray"); plt.title("Bitwise Xor")
print(result_xor.shape)



plt.show()