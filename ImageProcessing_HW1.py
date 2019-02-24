# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 14:19:48 2019

@author: serap aydogdu
"""

#Load Libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import try_all_threshold

# Step 1: Read the Image   (Please not use should close the "Colorful Image" window to continue)
img=cv2.imread('lenna.png',1)
cv2.namedWindow("Colorful Image")
cv2.imshow('Colorful Image',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()  


# Step 2: Obtain grayscale image by taking average values of RGB channels
I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Scale Image',I)


# Step 3: Obtain the histogram, h , of the gray scale image
plt.hist(I.ravel(),256,[0,256]); 
plt.xlabel("Intensity")
plt.ylabel("Frequency of occurance")

# Step 4: Inspect h and propose a threshold value, T , to segment into two parts and hence obtain a binary image, B
    
# =============================================================================
# The histogram of an image normally refers to a histogram of the pixel intensity values. 
# Need to determine an threshold value which is used to classify the pixel values. 
# Referring the histogram, h, one of 150,130 and 140 might be a threshold. 
# =============================================================================

# Define a threshold and convert image into a binary image
retval,mask_img = cv2.threshold(I, 150, 255, cv2.THRESH_BINARY)
retval,mask_img_2 = cv2.threshold(I, 130, 255, cv2.THRESH_BINARY)
retval,mask_img_3 = cv2.threshold(I, 140, 255, cv2.THRESH_BINARY)
retval,mask_img_4 = cv2.threshold(I, 175, 255, cv2.THRESH_BINARY)
retval,mask_img_5 = cv2.threshold(I, 135, 255, cv2.THRESH_BINARY)
retval,mask_img_6 = cv2.threshold(I, 110, 255, cv2.THRESH_BINARY)

cv2.imshow("Orginal Lena grayscale", I)
cv2.imshow('150', mask_img)
cv2.imshow('130', mask_img_2)
cv2.imshow('140', mask_img_3)
cv2.imshow('175', mask_img_4)
cv2.imshow('135', mask_img_5)
cv2.imshow('110', mask_img_6)

# So, I decided to choose threshold cas 135.  Because at this threshold colors' intensities 
# are mostly distrubuted corresponded.