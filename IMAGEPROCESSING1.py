# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:14:14 2019

@author: 60111
"""
import cv2
def thresholding_function1(master_image1):
    
    #Thresholding image
    ret1,thresholded_master_image1=cv2.threshold(master_image1,150,255,cv2.THRESH_BINARY) 
    #return the thresholded images
    return thresholded_master_image1

def process_image1(image1):
    #Read the image file as jpg change to numpy array
    master_image1=cv2.imread(image1,0)
    #Thresholding the function using thresholding function
    thresholded_master_image1=thresholding_function1(master_image1)
    #save the image as thresholded img
    return thresholded_master_image1,master_image1