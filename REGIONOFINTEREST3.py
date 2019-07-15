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
sys.path.insert(0, 'C:/Users/60111/Desktop/Python project/PYTHON CODES')

def regionofinteresttesting3(images3,images3B,ManufacturerModelName3,path,Series_library):
    Series_library_3=Series_library
    Series_library= Series_library_3['Series level']
    Region_library= Series_library_3['Scan Region']
    TotalDLParr3=[""]
    #Initialization value
    if ManufacturerModelName3[0]=='Emotion Duo':
        TotalDLParr3[0]=0
        series_3=list([''])*10
        DLP_series_3=list([''])*10
        CTDI_series_3=list([''])*10
        scan_length_3=list([''])*10
        OCR_dataframe_3=pandas.DataFrame({'Scan':series_3})
    
    else:
        
       
        TotalDLP3=pytesseract.image_to_string(images3[140:170,101:251],lang="mylang",config='--psm 6' )
        TotalDLP3=re.sub("\D","",TotalDLP3)
        image_scan_series_3=images3[210:370,0:130]
        image_scan_DLP_series_3=images3[210:400,390:425]
        image_scan_CTDI_series_3=images3[210:400,320:375]
        """
        plt.imshow(image_scan_series_1)
        plt.show()
        plt.imshow(image_scan_DLP_series_1)
        plt.show()
        plt.imshow(image_scan_CTDI_series_1)
        plt.show()
        """
        image_array_3=numpy.array(image_scan_series_3)
       
        sum_row_image_array_3=numpy.sum(image_array_3,axis=1).tolist()
        
        location_3=0
        number_of_series_3=0
        marker_3=0
        upper_location_3=list(numpy.arange(0,20))
        Below_location_3=list(numpy.arange(0,20))
        for pixel_3 in sum_row_image_array_3:
            if pixel_3 > 0:
                pixel_3=1
            if pixel_3==marker_3:
                pass
            else:
                if marker_3 == 0:
                    upper_location_3[number_of_series_3]=location_3-2
                    marker_3=1
                else:
                    Below_location_3[number_of_series_3]=location_3+2
                    if marker_3==1:
                        number_of_series_3=number_of_series_3+1
                        marker_3=0
            location_3=location_3+1
        position_3=0
        number_series_3=list([''])*20
        
        for pixel_3 in upper_location_3:
            image_series_label_3=image_scan_series_3[pixel_3:Below_location_3[position_3],0:130]
            if (Below_location_3[position_3]-pixel_3)>12:
                ret,image_series_label_3=cv2.threshold(image_series_label_3,150,255,cv2.THRESH_BINARY_INV)
                OCR_3=pytesseract.image_to_string(image_series_label_3,lang="eng",config='--psm 6' ) 
                number_series_3[position_3]=OCR_3
            else:
                number_series_3[position_3]=''
            
            
            position_3=position_3+1
        number_series_3=number_series_3[0:(position_3-1)]
        series_3=list([''])*10
        DLP_series_3=list([''])*10
        CTDI_series_3=list([''])*10
        scan_length_3=list([''])*10
        number_of_series_3=0
        marker_3=0
        OCR_dataframe_3=pandas.DataFrame({'Scan':number_series_3})
       
        
        for data_3 in number_series_3:
            
            searching_location_3=0
            if str(data_3) in list(Series_library):
                #series_3 is for scan type
                for data_searching in list(Series_library):
                    if data_searching == data_3:
                        break
                    searching_location_3=searching_location_3+1
                #print(list(Series_library[loc_index]))
                series_3[number_of_series_3]=Region_library[searching_location_3]
                
                DLP_series_images_3=image_scan_DLP_series_3[upper_location_3[marker_3]:Below_location_3[marker_3],0:35]
               
                
    
                
                try:
                    if (Below_location_3[marker_3]-upper_location_3[marker_3])>10:
                        DLP_series_3[number_of_series_3]=int(pytesseract.image_to_string(DLP_series_images_3,lang="mylang",config='--psm 8'))
                        if DLP_series_3[number_of_series_3] > int(TotalDLP3):
                            DLP_series_3[number_of_series_3]=DLP_series_3[number_of_series_3]/10
                            if DLP_series_3[number_of_series_3] > int(TotalDLP3):
                                DLP_series_3[number_of_series_3]=DLP_series_3[number_of_series_3]/10
                            else:
                                pass
                    else:
                        pass
                        
                except:
                    DLP_series_3[number_of_series_3]=pytesseract.image_to_string(DLP_series_images_3,lang="mylang",config='--psm 8')
                
                
                CTDI_series_images_3=image_scan_CTDI_series_3[upper_location_3[marker_3]:Below_location_3[marker_3],0:35]
                try:
                    CTDI_series_3[number_of_series_3]=int(pytesseract.image_to_string(CTDI_series_images_3,lang="mylang",config='--psm 8'))/100
                except:
                    CTDI_series_3[number_of_series_3]=pytesseract.image_to_string(CTDI_series_images_3,lang="mylang",config='--psm 8')
                
                try:
                    scan_length_3[number_of_series_3]=DLP_series_3[number_of_series_3]/CTDI_series_3[number_of_series_3]
                except:
                    scan_length_3[number_of_series_3]=0
                number_of_series_3=number_of_series_3+1
            marker_3=marker_3+1
        
            
        
        try:
           scan_length_3=max(scan_length_3[0:number_of_series_3])
        except:
            scan_length_3=scan_length_3[1]
        try:    
            TotalDLParr3[0]=int(TotalDLP3)
        except:
            TotalDLParr3[0]=TotalDLP3
            
    return TotalDLParr3,series_3,DLP_series_3,CTDI_series_3,scan_length_3,OCR_dataframe_3
