import os
import cv2 as cv
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image (JPG / JPEG), print its shape and return pixels in RGB"""
    if not isinstance(path, str):
        print("Error: path must be a string")
        return None
    if not os.path.exists(path):
        print(f"Error: file '{path}' not found")
        return None
    img_bgr = cv.imread(path)
    if img_bgr is None:
        print(f"Error: failed to load image '{path}'")
        return None
    # img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    img_rgb = img_bgr[:, :, ::-1]
    print(f"The shape of image is: {img_rgb.shape}")
    print(img_rgb)
    return img_rgb


def main():
    """Entrypoint script for load_image"""
    ndarr = ft_load("landscape.jpg")
    if ndarr is not None:
        window1 = cv.namedWindow("w1")
        Alive = True
        while Alive:
            cv.imshow(window1, ndarr)
            keypress = cv.waitKey(1)
            if keypress == ord('q'):
                Alive = False
        cv.destroyWindow(window1)
        cv.destroyAllWindows


if __name__ == "__main__":
    main()
