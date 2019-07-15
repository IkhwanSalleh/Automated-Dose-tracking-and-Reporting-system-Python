# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:11:05 2019

@author: 60111
"""
import pydicom as dicom
import numpy as np

def DICOM_TO_IMAGE_FUNCTION2(file_path):
    data2 = dicom.read_file(file_path)
    # overlay index 
    n_bits2 = 8
    
    
    # On (60xx,3000) are stored ovelays. 
    # First is (6000,3000), second (6002,3000), third (6004,3000),  
    # and so on.
    dicom_tag1 = 0x6000 

    overlay_raw2 = data2[dicom_tag1 ,0x3000].value

    # On (60xx,0010) and (60xx,0011) is stored overlay size
    rows = data2[dicom_tag1,0x0010].value # rows = 512
    cols = data2[dicom_tag1,0x0011].value # cols = 512

    decoded_linear2 = np.zeros(len(overlay_raw2)*n_bits2)

    # Decoding data. Each bit is stored as array element
    for i in range(1,len(overlay_raw2)):
        for k in range (0,n_bits2):
            byte_as_int2 = overlay_raw2[i]
            decoded_linear2[i*n_bits2 + k] = (byte_as_int2 >> k) & 0b1

    #overlay = np.array(pol)

    overlay2 = np.reshape(decoded_linear2,[rows,cols])
    return overlay2