import numpy as np
import matplotlib.pyplot as plt
from zoom import zoom_image
from load_image import ft_load
# import cv2 as cv


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


def transpose_image(arr: np.ndarray) -> np.ndarray:
    """A function to transpose an image"""
    h, w = arr.shape[:2]

    transposed = np.zeros((w, h), dtype=arr.dtype)

    for i in range(h):
        for j in range(w):
            transposed[j, i] = arr[i, j]
    return transposed


def rotate_image(img: np.ndarray) -> None:
    """Cut a square part from it
and transpose it to produce the image below.
It should display it, print the new shape
and the data of the image after the transpose."""
    try:
        zoomed = zoom_image(img)
        shape_stat = f"The shape of image is: {zoomed.shape}"
        if zoomed.ndim == 3:
            print(f"{shape_stat} or ({zoomed.shape[0]}, {zoomed.shape[1]})")
        else:
            print(f"{shape_stat}")
        print(zoomed)
        zoomed = zoomed.squeeze()
        transposed = transpose_image(zoomed)
        # transposed = zoomed.T faster because is compiled in c
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error in rotate_image: {e}")


def main():
    """Entrypoing script for zoom.py"""
    try:
        img = ft_load("animal.jpeg")
        rotate_image(img)
    except Exception as e:
        print(f"Error in main(): {e}")


if __name__ == "__main__":
    main()
