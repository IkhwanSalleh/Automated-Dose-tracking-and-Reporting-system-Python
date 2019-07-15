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
def regionofinteresttesting4(images4,images4B,ManufacturerModelName4,path,Series_library):
    Series_library_4=Series_library
    Series_library= Series_library_4['Series level']
    Region_library= Series_library_4['Scan Region']
    TotalDLParr4=[""]
    #Initialization value
    if ManufacturerModelName4[0]=='Emotion Duo':
        TotalDLParr4[0]=0
        series_4=list([''])*10
        DLP_series_4=list([''])*10
        CTDI_series_4=list([''])*10
        scan_length_4=list([''])*10
        OCR_dataframe_4=pandas.DataFrame({'Scan':series_4})

    
    else:
        
       
        TotalDLP4=pytesseract.image_to_string(images4[140:170,101:251],lang="mylang",config='--psm 6' )
        TotalDLP4=re.sub("\D","",TotalDLP4)
        image_scan_series_4=images4[210:370,0:130]
        image_scan_DLP_series_4=images4[210:400,390:425]
        image_scan_CTDI_series_4=images4[210:400,320:375]
        """
        plt.imshow(image_scan_series_1)
        plt.show()
        plt.imshow(image_scan_DLP_series_1)
        plt.show()
        plt.imshow(image_scan_CTDI_series_1)
        plt.show()
        """
        image_array_4=numpy.array(image_scan_series_4)
       
        sum_row_image_array_4=numpy.sum(image_array_4,axis=1).tolist()
        
        location_4=0
        number_of_series_4=0
        marker_4=0
        upper_location_4=list(numpy.arange(0,20))
        Below_location_4=list(numpy.arange(0,20))
        for pixel_4 in sum_row_image_array_4:
            if pixel_4 > 0:
                pixel_4=1
            if pixel_4==marker_4:
                pass
            else:
                if marker_4 == 0:
                    upper_location_4[number_of_series_4]=location_4-2
                    marker_4=1
                else:
                    Below_location_4[number_of_series_4]=location_4+2
                    if marker_4==1:
                        number_of_series_4=number_of_series_4+1
                        marker_4=0
            location_4=location_4+1
        position_4=0
        number_series_4=list([''])*20
        
        for pixel_4 in upper_location_4:
            image_series_label_4=image_scan_series_4[pixel_4:Below_location_4[position_4],0:130]
            if (Below_location_4[position_4]-pixel_4)>12:
                ret,image_series_label_4=cv2.threshold(image_series_label_4,150,255,cv2.THRESH_BINARY_INV)
                OCR_4=pytesseract.image_to_string(image_series_label_4,lang="eng",config='--psm 6' ) 
                number_series_4[position_4]=OCR_4
            else:
                number_series_4[position_4]=''
            
            
            position_4=position_4+1
        number_series_4=number_series_4[0:(position_4-1)]
        series_4=list([''])*10
        DLP_series_4=list([''])*10
        CTDI_series_4=list([''])*10
        scan_length_4=list([''])*10
        number_of_series_4=0
        marker_4=0
        OCR_dataframe_4=pandas.DataFrame({'Scan':number_series_4})
       
        for data_4 in number_series_4:
           
            searching_location_4=0
            if str(data_4) in list(Series_library):
                #series_4 is for scan type
                for data_searching in list(Series_library):
                    if data_searching == data_4:
                        break
                    searching_location_4=searching_location_4+1
                #print(list(Series_library[loc_index]))
                series_4[number_of_series_4]=Region_library[searching_location_4]
                
                DLP_series_images_4=image_scan_DLP_series_4[upper_location_4[marker_4]:Below_location_4[marker_4],0:35]
               
                
    
                
                try:
                    if (Below_location_4[marker_4]-upper_location_4[marker_4])>10:
                        DLP_series_4[number_of_series_4]=int(pytesseract.image_to_string(DLP_series_images_4,lang="mylang",config='--psm 8'))
                        if DLP_series_4[number_of_series_4] > int(TotalDLP4):
                            DLP_series_4[number_of_series_4]=DLP_series_4[number_of_series_4]/10
                            if DLP_series_4[number_of_series_4] > int(TotalDLP4):
                                DLP_series_4[number_of_series_4]=DLP_series_4[number_of_series_4]/10
                            else:
                                pass
                    else:
                        pass
                        
                except:
                    DLP_series_4[number_of_series_4]=pytesseract.image_to_string(DLP_series_images_4,lang="mylang",config='--psm 8')
              
                
                
                CTDI_series_images_4=image_scan_CTDI_series_4[upper_location_4[marker_4]:Below_location_4[marker_4],0:35]
                try:
                    CTDI_series_4[number_of_series_4]=int(pytesseract.image_to_string(CTDI_series_images_4,lang="mylang",config='--psm 8'))/100
                except:
                    CTDI_series_4[number_of_series_4]=pytesseract.image_to_string(CTDI_series_images_4,lang="mylang",config='--psm 8')
                
                try:
                    scan_length_4[number_of_series_4]=DLP_series_4[number_of_series_4]/CTDI_series_4[number_of_series_4]
                except:
                    scan_length_4[number_of_series_4]=0
                number_of_series_4=number_of_series_4+1
            marker_4=marker_4+1
        
            
        
        try:
           scan_length_4=max(scan_length_4[0:number_of_series_4])
        except:
            scan_length_4=scan_length_4[1]
        try:    
            TotalDLParr4[0]=int(TotalDLP4)
        except:
            TotalDLParr4[0]=TotalDLP4
            
    return TotalDLParr4,series_4,DLP_series_4,CTDI_series_4,scan_length_4,OCR_dataframe_4
