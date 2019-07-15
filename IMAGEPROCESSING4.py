# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:14:14 2019

@author: 60111
"""
import cv2
def thresholding_function4(master_image4):
    
    #Thresholding image
    ret,thresholded_master_image4=cv2.threshold(master_image4,150,255,cv2.THRESH_BINARY) 
    #return the thresholded images
    return thresholded_master_image4

def process_image4(image4):
    #Read the image file as jpg change to numpy array
    master_image4=cv2.imread(image4,0)
    #Thresholding the function using thresholding function
    thresholded_master_image4=thresholding_function4(master_image4)
    #save the image as thresholded img
    return thresholded_master_image4,master_image4