# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:11:05 2019

@author: 60111
"""
import pydicom as dicom
import numpy as np

def DICOM_TO_IMAGE_FUNCTION4(file_path):
    data4 = dicom.read_file(file_path)
    # overlay index 
    n_bits4 = 8
    
    
    # On (60xx,3000) are stored ovelays. 
    # First is (6000,3000), second (6002,3000), third (6004,3000),  
    # and so on.
    dicom_tag1 = 0x6000 

    overlay_raw4 = data4[dicom_tag1 ,0x3000].value

    # On (60xx,0010) and (60xx,0011) is stored overlay size
    rows = data4[dicom_tag1,0x0010].value # rows = 512
    cols = data4[dicom_tag1,0x0011].value # cols = 512

    decoded_linear4 = np.zeros(len(overlay_raw4)*n_bits4)

    # Decoding data. Each bit is stored as array element
    for i in range(1,len(overlay_raw4)):
        for k in range (0,n_bits4):
            byte_as_int4 = overlay_raw4[i]
            decoded_linear4[i*n_bits4 + k] = (byte_as_int4 >> k) & 0b1

    #overlay = np.array(pol)

    overlay4 = np.reshape(decoded_linear4,[rows,cols])
    return overlay4