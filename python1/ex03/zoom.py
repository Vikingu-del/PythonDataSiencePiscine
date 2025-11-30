import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from load_image import ft_load

# import sys
# import os
# sys.path.insert(
#     0, os.path.abspath(
#         os.path.join(
#             os.path.dirname(__file__),
#             '..')
#         )
#     )
# from ex02.load_image import ft_load


def zoom_image(img: np.ndarray) -> None:
    """Prints some information
about the image array that takes as a parameter
and display it after "zooming".
• The size in pixel on both X and Y axis
• The number of channel
• The pixel content of the image.
• Display the scale on the x and y axis on the image
If anything went wrong, the program must not stop abruptly and handle any error
with a clear message."""
    try:
        if img is None:
            print("Error: no image to process (ft_load returned None)")
            return

        if not isinstance(img, np.ndarray):
            print("Error: img must be a numpy ndarray")
            return
        img_alias = img
        img_alias = cv.cvtColor(img_alias, cv.COLOR_BGR2GRAY)
        h, w = img_alias.shape[:2]
        size = min(400, h, w)
        startx = (w - size) // 2
        starty = (h - size) // 2
        cropped_copy = img_alias[starty:starty + size, startx:startx + size]
        if cropped_copy.ndim == 2:
            print(f"New shape after slicing: ({cropped_copy.shape[0]},\
                  {cropped_copy.shape[1]}, 1) or {cropped_copy.shape}")
            cropped_copy = cropped_copy.reshape(
                cropped_copy.shape[0], cropped_copy.shape[1], 1
            )
        else:
            print(f"New shape after slicing: {cropped_copy.shape}")
        print(cropped_copy)
        plt.imshow(cropped_copy, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error in zoom_image: {e}")


def main():
    """Entrypoing script for zoom.py"""
    try:
        img = ft_load("animal.jpeg")
        print(img)
        zoom_image(img)
    except Exception as e:
        print(f"Error in main(): {e}")


if __name__ == "__main__":
    main()
