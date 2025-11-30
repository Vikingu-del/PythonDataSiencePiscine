import cv2
import matplotlib.pyplot as plt

from urllib.request import urlretrieve

from IPython.display import Image

img_bgr = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Display 18x18 pixel image
# Image(filename="New_Zealand_Coast.jpg") # for Jupyter notebook

plt.imshow(img_rgb)
plt.axis("off")
plt.show()