# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:14:14 2019

@author: 60111
"""
import cv2
def thresholding_function5(master_image5):
    
    #Thresholding image
    ret5,thresholded_master_image5=cv2.threshold(master_image5,150,255,cv2.THRESH_BINARY) 
    #return the thresholded images
    return thresholded_master_image5

def process_image5(image5):
    #Read the image file as jpg change to numpy array
    master_image5=cv2.imread(image5,0)
    #Thresholding the function using thresholding function
    thresholded_master_image5=thresholding_function5(master_image5)
    #save the image as thresholded img
    return thresholded_master_image5,master_image5