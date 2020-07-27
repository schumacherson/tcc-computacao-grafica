from __future__ import print_function
from builtins import input
import cv2 as cv2
import numpy as np
import argparse

def main():
    image = cv2.VideoCapture(0)
    ret, frame = image.read()

    
    alpha = 1.0
    beta = 0. 

    try:
        alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
        beta = int(input('* Enter the beta value [0-100]: '))
    except ValueError:
        print('Error, not a number')

    


    while image.isOpened():
        new_image = np.zeros(frame.shape, frame.dtype)
        
        new_image = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
        
        if ret == True:
            cv2.imshow('Original Image', frame)
            cv2.imshow('New Image', new_image)

        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            print("Saindo...")
            break

if __name__ == "__main__":
    main()