import numpy as np
from PIL import ImageGrab
import cv2

def get_frames():
    im = ImageGrab.grab((60,60,600,600))
    im=np.array(im)
    im=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
    im=cv2.resize(im,(80,60))
    return im
