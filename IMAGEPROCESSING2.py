# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:14:14 2019

@author: 60111
"""
import cv2
def thresholding_function2(master_image2):
    
    #Thresholding image
    ret,thresholded_master_image2=cv2.threshold(master_image2,150,255,cv2.THRESH_BINARY) 
    #return the thresholded images
    return thresholded_master_image2

def process_image2(image2):
    #Read the image file as jpg change to numpy array
    master_image2=cv2.imread(image2,0)
    #Thresholding the function using thresholding function
    thresholded_master_image2=thresholding_function2(master_image2)
    #save the image as thresholded img
    return thresholded_master_image2,master_image2