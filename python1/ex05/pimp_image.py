import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(arr: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted_array = 255 - arr
    plt.imshow(inverted_array)
    plt.title("Inverted Image")
    plt.show()
    return arr


def ft_red(arr: np.ndarray) -> np.ndarray:
    """Makes the image red"""
    red_arr = arr.copy()
    red_arr[:, :, 1] = red_arr[:, :, 1] * 0
    red_arr[:, :, 2] = red_arr[:, :, 2] * 0
    plt.imshow(red_arr)
    plt.title("Red Image")
    plt.show()
    return red_arr


def ft_green(arr: np.ndarray) -> np.ndarray:
    """Makes the image green"""
    green_arr = arr.copy()
    green_arr[:, :, 0] = green_arr[:, :, 0] - green_arr[:, :, 0]
    green_arr[:, :, 2] = green_arr[:, :, 2] - green_arr[:, :, 2]
    plt.imshow(green_arr)
    plt.title("Green Image")
    plt.show()
    return green_arr


def ft_blue(arr: np.ndarray) -> np.ndarray:
    """Makes the image blue"""
    blue_arr = arr.copy()
    blue_arr[:, :, 0] = 0
    blue_arr[:, :, 1] = 0
    plt.imshow(blue_arr)
    plt.title("Blue Image")
    plt.show()
    return blue_arr


def ft_grey(arr: np.ndarray) -> np.ndarray:
    """Makes the image grey"""
    gray_arr = arr.copy()
    grey_mask = gray_arr[:, :, 1] / 1
    gray_arr[:, :, 0] = grey_mask
    gray_arr[:, :, 1] = grey_mask
    gray_arr[:, :, 2] = grey_mask
    plt.imshow(gray_arr, cmap="gray")
    plt.title("Gray Image")
    plt.show()
    return gray_arr


def main():
    """Entrypoint script for load_image"""
    ft_grey(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
