# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:40:12 2019

@author: 60111
"""

import DICOMTOIMAGE4
import IMAGEPROCESSING4
import METADATAPYDICOMANALYSIS4
import REGIONOFINTEREST4
import TOEXCEL4
from matplotlib import pyplot as plt


def processingmaster4(path,q4,Series_library,q4A):
    
    try:
        overlay4=DICOMTOIMAGE4.DICOM_TO_IMAGE_FUNCTION4(path)
        plt.imsave("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage4.png", overlay4,cmap='gray')
    except:
        print('ERROR')
        pass
    
#This Section Read image processing the function
    thresholded_master_image4,master_images4=IMAGEPROCESSING4.process_image4("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage4.png")
    PatientID4,PatientStudyDate4,Manufacturer4,ManufacturerModelName4,StudyDescription4,PatientAge4,PatientSex4,Contrastgroup4,InstitutionName4,InstitutionGroup4,OperatorName4=METADATAPYDICOMANALYSIS4.Metadata_pydicom_analysis4(path)
    TotalDLParr4,series_4,DLP_series_4,CTDI_series_4,scan_length_4,Compilledscan4=REGIONOFINTEREST4.regionofinteresttesting4(thresholded_master_image4,master_images4,ManufacturerModelName4,path,Series_library)
    Compilleddata4= TOEXCEL4.toexcel(PatientID4,TotalDLParr4,series_4,DLP_series_4,CTDI_series_4,scan_length_4,PatientStudyDate4,Manufacturer4,ManufacturerModelName4,StudyDescription4,path,PatientAge4,PatientSex4,Contrastgroup4,InstitutionName4,InstitutionGroup4,OperatorName4)
    q4.put(Compilleddata4)
    q4A.put(Compilledscan4)
    return Compilleddata4