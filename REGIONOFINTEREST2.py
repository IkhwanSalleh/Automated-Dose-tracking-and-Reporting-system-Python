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
def regionofinteresttesting2(images2,images2B,ManufacturerModelName2,path,Series_library):
     Series_library_2=Series_library
     Series_library= Series_library_2['Series level']
     Region_library= Series_library_2['Scan Region']
     TotalDLParr2=[""]
     #Initialization value
     if ManufacturerModelName2[0]=='Emotion Duo':
         TotalDLParr2[0]=0
         series_2=list([''])*10
         DLP_series_2=list([''])*10
         CTDI_series_2=list([''])*10
         scan_length_2=list([''])*10
         OCR_dataframe_2=pandas.DataFrame({'Scan':series_2})
    
     else:
        
       
        TotalDLP2=pytesseract.image_to_string(images2[140:170,101:251],lang="mylang",config='--psm 6' )
        TotalDLP2=re.sub("\D","",TotalDLP2)
        image_scan_series_2=images2[210:370,0:130]
        image_scan_DLP_series_2=images2[210:400,390:425]
        image_scan_CTDI_series_2=images2[210:400,320:375]
        
        image_array_2=numpy.array(image_scan_series_2)
       
        sum_row_image_array_2=numpy.sum(image_array_2,axis=1).tolist()
        
        location_2=0
        number_of_series_2=0
        marker_2=0
        upper_location_2=list(numpy.arange(0,20))
        Below_location_2=list(numpy.arange(0,20))
        for pixel_2 in sum_row_image_array_2:
            if pixel_2 > 0:
                pixel_2=1
            if pixel_2==marker_2:
                pass
            else:
                if marker_2 == 0:
                    upper_location_2[number_of_series_2]=location_2-2
                    marker_2=1
                else:
                    Below_location_2[number_of_series_2]=location_2+2
                    if marker_2==1:
                        number_of_series_2=number_of_series_2+1
                        marker_2=0
            location_2=location_2+1
        position_2=0
        number_series_2=list([''])*20
        
        for pixel_2 in upper_location_2:
            image_series_label_2=image_scan_series_2[pixel_2:Below_location_2[position_2],0:130]
            if (Below_location_2[position_2]-pixel_2)>12:
                ret,image_series_label_2=cv2.threshold(image_series_label_2,150,255,cv2.THRESH_BINARY_INV)
                
                OCR_2=pytesseract.image_to_string(image_series_label_2,lang="eng",config='--psm 6' ) 
                number_series_2[position_2]=OCR_2
            else:
                number_series_2[position_2]=''
            position_2=position_2+1
        number_series_2=number_series_2[0:(position_2-1)]
        series_2=list([''])*10
        DLP_series_2=list([''])*10
        CTDI_series_2=list([''])*10
        scan_length_2=list([''])*10
        number_of_series_2=0
        marker_2=0
        OCR_dataframe_2=pandas.DataFrame({'Scan':number_series_2})
        
        for data_2 in number_series_2:
            searching_location_2=0
            if str(data_2) in list(Series_library):
                #series_2 is for scan type
                for data_searching in list(Series_library):
                    if data_searching == data_2:
                        break
                    searching_location_2=searching_location_2+1
                #print(list(Series_library[loc_index]))
                series_2[number_of_series_2]=Region_library[searching_location_2]
                
                
                DLP_series_images_2=image_scan_DLP_series_2[upper_location_2[marker_2]:Below_location_2[marker_2],0:35]
                try:
                    if (Below_location_2[marker_2]-upper_location_2[marker_2])>10:
                        DLP_series_2[number_of_series_2]=int(pytesseract.image_to_string(DLP_series_images_2,lang="mylang",config='--psm 8'))
                        if DLP_series_2[number_of_series_2] > int(TotalDLP2):
                            DLP_series_2[number_of_series_2]=DLP_series_2[number_of_series_2]/10
                            if DLP_series_2[number_of_series_2] > int(TotalDLP2):
                                DLP_series_2[number_of_series_2]=DLP_series_2[number_of_series_2]/10
                            else:
                                pass
                    else:
                        pass
                        
                except:
                    DLP_series_2[number_of_series_2]=pytesseract.image_to_string(DLP_series_images_2,lang="mylang",config='--psm 8')
                
                
                
                CTDI_series_images_2=image_scan_CTDI_series_2[upper_location_2[marker_2]:Below_location_2[marker_2],0:35]
                try:
                    CTDI_series_2[number_of_series_2]=int(pytesseract.image_to_string(CTDI_series_images_2,lang="mylang",config='--psm 8'))/100
                except:
                    CTDI_series_2[number_of_series_2]=pytesseract.image_to_string(CTDI_series_images_2,lang="mylang",config='--psm 8')
                
                try:
                    scan_length_2[number_of_series_2]=DLP_series_2[number_of_series_2]/CTDI_series_2[number_of_series_2]
                except:
                    scan_length_2[number_of_series_2]=0
                number_of_series_2=number_of_series_2+1
            marker_2=marker_2+1
        
            
        
        try:
           scan_length_2=max(scan_length_2[0:number_of_series_2])
        except:
            scan_length_2=scan_length_2[1]
        try:    
            TotalDLParr2[0]=int(TotalDLP2)
        except:
            TotalDLParr2[0]=TotalDLP2
            
     return TotalDLParr2,series_2,DLP_series_2,CTDI_series_2,scan_length_2,OCR_dataframe_2