# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:22:04 2019

@author: 60111
"""
import regex as re
import pytesseract
import cv2
import numpy
import pandas
import sys
from matplotlib import pyplot as plt
sys.path.insert(0, 'C:/Users/60111/Desktop/Python project/PYTHON CODES')
def regionofinteresttesting1(images1,images1B,ManufacturerModelName1,path,Series_library):
    Series_library_1=Series_library
    Series_library= Series_library_1['Series level']
    Region_library= Series_library_1['Scan Region']
    TotalDLParr1=[""]
    #Initialization value
    if ManufacturerModelName1[0]=='Emotion Duo':
        TotalDLParr1[0]=0
        series_1=list([''])*10
        DLP_series_1=list([''])*10
        CTDI_series_1=list([''])*10
        scan_length_1=list([''])*10
        OCR_dataframe_1=pandas.DataFrame({'Scan':series_1})
        
    else:
        
       
        TotalDLP1=pytesseract.image_to_string(images1[140:170,101:251],lang="mylang",config='--psm 6' )
        TotalDLP1=re.sub("\D","",TotalDLP1)
        image_scan_series_1=images1[210:370,0:130]
        image_scan_DLP_series_1=images1[210:400,390:425]
        image_scan_CTDI_series_1=images1[210:400,320:375]

        image_array_1=numpy.array(image_scan_series_1)
       
        sum_row_image_array_1=numpy.sum(image_array_1,axis=1).tolist()
        
        location_1=0
        number_of_series_1=0
        marker_1=0
        upper_location_1=list(numpy.arange(0,20))
        Below_location_1=list(numpy.arange(0,20))
        for pixel_1 in sum_row_image_array_1:
            if pixel_1 > 0:
                pixel_1=1
            if pixel_1==marker_1:
                pass
            else:
                if marker_1 == 0:
                    upper_location_1[number_of_series_1]=location_1-2
                    marker_1=1
                else:
                    Below_location_1[number_of_series_1]=location_1+2
                    if marker_1==1:
                        number_of_series_1=number_of_series_1+1
                        marker_1=0
            location_1=location_1+1
        position_1=0
        number_series_1=list([''])*20
        for pixel_1 in upper_location_1:
            image_series_label_1=image_scan_series_1[pixel_1:Below_location_1[position_1],0:130]
            if (Below_location_1[position_1]-pixel_1)>12:
                ret,image_series_label_1=cv2.threshold(image_series_label_1,150,255,cv2.THRESH_BINARY_INV)
                OCR_1=pytesseract.image_to_string(image_series_label_1,lang="eng",config='--psm 6' ) 
                number_series_1[position_1]=OCR_1

                
            else:
                number_series_1[position_1]=''
            position_1=position_1+1
        number_series_1=number_series_1[0:(position_1-1)]
        
        series_1=list([''])*10
        DLP_series_1=list([''])*10
        CTDI_series_1=list([''])*10
        scan_length_1=list([''])*10
        number_of_series_1=0
        marker_1=0
        OCR_dataframe_1=pandas.DataFrame({'Scan':number_series_1})
        
        for data_1 in number_series_1:
            searching_location_1=0
            if str(data_1) in list(Series_library):
                #series_1 is for scan type
                for data_searching in list(Series_library):
                    if data_searching == data_1:
                        break
                    searching_location_1=searching_location_1+1
                #print(list(Series_library[loc_index]))
                series_1[number_of_series_1]=Region_library[searching_location_1]
                
                
                DLP_series_images_1=image_scan_DLP_series_1[upper_location_1[marker_1]:Below_location_1[marker_1],0:35]
                try:
                    if (Below_location_1[marker_1]-upper_location_1[marker_1])>10:
                        DLP_series_1[number_of_series_1]=int(pytesseract.image_to_string(DLP_series_images_1,lang="mylang",config='--psm 8'))
                        if DLP_series_1[number_of_series_1] > int(TotalDLP1):
                            DLP_series_1[number_of_series_1]=DLP_series_1[number_of_series_1]/10
                            if DLP_series_1[number_of_series_1] > int(TotalDLP1):
                                DLP_series_1[number_of_series_1]=DLP_series_1[number_of_series_1]/10
                            else:
                                pass
                    else:
                        pass
                except:
                    DLP_series_1[number_of_series_1]=pytesseract.image_to_string(DLP_series_images_1,lang="mylang",config='--psm 8')
                
                
                
                CTDI_series_images_1=image_scan_CTDI_series_1[upper_location_1[marker_1]:Below_location_1[marker_1],0:35]
                try:
                    CTDI_series_1[number_of_series_1]=int(pytesseract.image_to_string(CTDI_series_images_1,lang="mylang",config='--psm 8'))/100
                except:
                    CTDI_series_1[number_of_series_1]=pytesseract.image_to_string(CTDI_series_images_1,lang="mylang",config='--psm 8')
                
                try:
                    scan_length_1[number_of_series_1]=DLP_series_1[number_of_series_1]/CTDI_series_1[number_of_series_1]
                except:
                    scan_length_1[number_of_series_1]=0
                number_of_series_1=number_of_series_1+1
            marker_1=marker_1+1
        
            
        
        try:
            scan_length_1=max(scan_length_1[0:number_of_series_1])
        except:
            scan_length_1=scan_length_1[0]
        try:    
            TotalDLParr1[0]=int(TotalDLP1)
        except:
            TotalDLParr1[0]=TotalDLP1
            
    return TotalDLParr1,series_1,DLP_series_1,CTDI_series_1,scan_length_1,OCR_dataframe_1
