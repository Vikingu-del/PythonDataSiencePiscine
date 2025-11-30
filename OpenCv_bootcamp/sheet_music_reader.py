## Application: Sheet Music Reader
# Suppose you wanted to build an application that could read (decode) sheet music. This is similar to
# Optical Character Recognigition (OCR) for text documents where the goal is to recognize text
# characters. In either application, one of the first steps in the processing pipeline is to isolate the
# important information in the image of a document (separating it from the background). This task can be
# accomplished with thresholding techniques. Let's take a look at an example.


import cv2
import matplotlib.pyplot as plt

# Read the original image
img_read = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

# shows a histogram of pixels to take desicions how to threshold
# plt.hist(img_read.ravel(), bins=256)
# plt.show()

# Perform global thresholding
retval, img_thresh_gbl_1 = cv2.threshold(img_read, 50, 255, cv2.THRESH_BINARY)

# Perform global thresholding
retval, img_thresh_gbl_2 = cv2.threshold(img_read, 130, 255, cv2.THRESH_BINARY)


# Perform adaptive thresholding
img_thresh_adp = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

plt.figure(figsize=[18,15])
plt.subplot(221); plt.imshow(img_read,        cmap="gray");  plt.title("Original");
plt.subplot(222); plt.imshow(img_thresh_gbl_1,cmap="gray");  plt.title("Thresholded (global: 50)");
plt.subplot(223); plt.imshow(img_thresh_gbl_2,cmap="gray");  plt.title("Thresholded (global: 130)");
plt.subplot(224); plt.imshow(img_thresh_adp,  cmap="gray");  plt.title("Thresholded (adaptive)");

plt.show()