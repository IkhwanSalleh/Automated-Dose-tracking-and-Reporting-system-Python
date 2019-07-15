# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:14:14 2019

@author: 60111
"""
import cv2
def thresholding_function3(master_image3):
    
    #Thresholding image
    ret,thresholded_master_image3=cv2.threshold(master_image3,150,255,cv2.THRESH_BINARY) 
    #return the thresholded images
    return thresholded_master_image3

def process_image3(image3):
    #Read the image file as jpg change to numpy array
    master_image3=cv2.imread(image3,0)
    #Thresholding the function using thresholding function
    thresholded_master_image3=thresholding_function3(master_image3)
    #save the image as thresholded img
    return thresholded_master_image3,master_image3