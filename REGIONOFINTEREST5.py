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

def regionofinteresttesting5(images5,images5B,ManufacturerModelName5,path,Series_library):
    Series_library_5=Series_library
    Series_library= Series_library_5['Series level']
    Region_library= Series_library_5['Scan Region']
    TotalDLParr5=[""]
    #Initialization value
    if ManufacturerModelName5[0]=='Emotion Duo':
        TotalDLParr5[0]=0
        series_5=list([''])*10
        DLP_series_5=list([''])*10
        CTDI_series_5=list([''])*10
        scan_length_5=list([''])*10
        OCR_dataframe_5=pandas.DataFrame({'Scan':series_5})
    
    
    else:
        
       
        TotalDLP5=pytesseract.image_to_string(images5[140:170,101:251],lang="mylang",config='--psm 6' )
        TotalDLP5=re.sub("\D","",TotalDLP5)
        image_scan_series_5=images5[210:370,0:130]
        image_scan_DLP_series_5=images5[210:400,390:425]
        image_scan_CTDI_series_5=images5[210:400,320:375]
        """
        plt.imshow(image_scan_series_1)
        plt.show()
        plt.imshow(image_scan_DLP_series_1)
        plt.show()
        plt.imshow(image_scan_CTDI_series_1)
        plt.show()
        """
        image_array_5=numpy.array(image_scan_series_5)
       
        sum_row_image_array_5=numpy.sum(image_array_5,axis=1).tolist()
        
        location_5=0
        number_of_series_5=0
        marker_5=0
        upper_location_5=list(numpy.arange(0,20))
        Below_location_5=list(numpy.arange(0,20))
        for pixel_5 in sum_row_image_array_5:
            if pixel_5 > 0:
                pixel_5=1
            if pixel_5==marker_5:
                pass
            else:
                if marker_5 == 0:
                    upper_location_5[number_of_series_5]=location_5-2
                    marker_5=1
                else:
                    Below_location_5[number_of_series_5]=location_5+2
                    if marker_5==1:
                        number_of_series_5=number_of_series_5+1
                        marker_5=0
            location_5=location_5+1
        position_5=0
        number_series_5=list([''])*20
        
        for pixel_5 in upper_location_5:
            image_series_label_5=image_scan_series_5[pixel_5:Below_location_5[position_5],0:130]
            if (Below_location_5[position_5]-pixel_5)>12:
                ret,image_series_label_5=cv2.threshold(image_series_label_5,150,255,cv2.THRESH_BINARY_INV)
                OCR_5=pytesseract.image_to_string(image_series_label_5,lang="eng",config='--psm 6' ) 
                number_series_5[position_5]=OCR_5
            else:
                number_series_5[position_5]=''
            
            
            position_5=position_5+1
        number_series_5=number_series_5[0:(position_5-1)]

        series_5=list([''])*10
        DLP_series_5=list([''])*10
        CTDI_series_5=list([''])*10
        scan_length_5=list([''])*10
        number_of_series_5=0
        marker_5=0
        OCR_dataframe_5=pandas.DataFrame({'Scan':number_series_5})
        for data_5 in number_series_5:

            searching_location_5=0
            if str(data_5) in list(Series_library):
                #series_5 is for scan type
                for data_searching in list(Series_library):
                    if data_searching == data_5:
                        break
                    searching_location_5=searching_location_5+1
                #print(list(Series_library[loc_index]))
                series_5[number_of_series_5]=Region_library[searching_location_5]
                
                DLP_series_images_5=image_scan_DLP_series_5[upper_location_5[marker_5]:Below_location_5[marker_5],0:35]
               
                
    
                
                try:
                    if (Below_location_5[marker_5]-upper_location_5[marker_5])>10:
                        DLP_series_5[number_of_series_5]=int(pytesseract.image_to_string(DLP_series_images_5,lang="mylang",config='--psm 8'))
                        if DLP_series_5[number_of_series_5] > int(TotalDLP5):
                            DLP_series_5[number_of_series_5]=DLP_series_5[number_of_series_5]/10
                            if DLP_series_5[number_of_series_5] > int(TotalDLP5):
                                DLP_series_5[number_of_series_5]=DLP_series_5[number_of_series_5]/10
                            else:
                                pass
                    else:
                        pass
                        
                except:
                    DLP_series_5[number_of_series_5]=pytesseract.image_to_string(DLP_series_images_5,lang="mylang",config='--psm 8')
                
                
                
                CTDI_series_images_5=image_scan_CTDI_series_5[upper_location_5[marker_5]:Below_location_5[marker_5],0:35]
                try:
                    CTDI_series_5[number_of_series_5]=int(pytesseract.image_to_string(CTDI_series_images_5,lang="mylang",config='--psm 8'))/100
                except:
                    CTDI_series_5[number_of_series_5]=pytesseract.image_to_string(CTDI_series_images_5,lang="mylang",config='--psm 8')
                
                try:
                    scan_length_5[number_of_series_5]=DLP_series_5[number_of_series_5]/CTDI_series_5[number_of_series_5]
                except:
                    scan_length_5[number_of_series_5]=0
                number_of_series_5=number_of_series_5+1
            marker_5=marker_5+1
        
            
        
        try:
           scan_length_5=max(scan_length_5[0:number_of_series_5])
        except:
            scan_length_5=scan_length_5[1]
        try:    
            TotalDLParr5[0]=int(TotalDLP5)
        except:
            TotalDLParr5[0]=TotalDLP5
            
    return TotalDLParr5,series_5,DLP_series_5,CTDI_series_5,scan_length_5,OCR_dataframe_5