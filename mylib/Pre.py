import numpy as np
import cv2

# simple image processing to start with
class preproc(object):

    def contrast(img):

        img = cv2.imread('data/cropped image.png', cv2.IMREAD_GRAYSCALE)
        # increase contrast and reduce the background noise
        pxmin = np.min(img)
        pxmax = np.max(img)
        # optimise the pixel values (255, 300, 350 etc) and check the output
        # 400 value gave a better output on noisy 'handwritten.png' along with the thickness 1
        # (iterations = 1), when tested seperately
        imgContrast = (img - pxmin) / (pxmax - pxmin) * 400

        # increase the text line width or thickness
        kernel = np.ones((3, 3), np.uint8)
        imgMorph = cv2.erode(imgContrast, kernel, iterations = 1)

        # save the img
        cv2.imwrite('data/processed image.png', imgMorph)
