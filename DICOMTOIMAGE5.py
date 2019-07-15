# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:11:05 2019

@author: 60111
"""
import pydicom as dicom
import numpy as np

def DICOM_TO_IMAGE_FUNCTION5(file_path):
    data5 = dicom.read_file(file_path)
    # overlay index 
    n_bits5 = 8
    
    
    # On (60xx,3000) are stored ovelays. 
    # First is (6000,3000), second (6002,3000), third (6004,3000),  
    # and so on.
    dicom_tag5 = 0x6000 

    overlay_raw5 = data5[dicom_tag5 ,0x3000].value

    # On (60xx,0050) and (60xx,0051) is stored overlay size
    rows = data5[dicom_tag5,0x0010].value # rows = 512
    cols = data5[dicom_tag5,0x0011].value # cols = 512

    decoded_linear5 = np.zeros(len(overlay_raw5)*n_bits5)

    # Decoding data. Each bit is stored as array element
    for i in range(1,len(overlay_raw5)):
        for k in range (0,n_bits5):
            byte_as_int = overlay_raw5[i]
            decoded_linear5[i*n_bits5 + k] = (byte_as_int >> k) & 0b1

    #overlay = np.array(pol)

    overlay5 = np.reshape(decoded_linear5,[rows,cols])
    return overlay5