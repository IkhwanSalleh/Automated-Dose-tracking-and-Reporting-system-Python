# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:02:58 2019

@author: Ikhwan Salleh
"""
import DICOMTOIMAGE5
import IMAGEPROCESSING5
import METADATAPYDICOMANALYSIS5
import REGIONOFINTEREST5
import TOEXCEL5
from matplotlib import pyplot as plt


def processingmaster5(path,q5,Series_library,q5A):
    
    try:
        overlay5=DICOMTOIMAGE5.DICOM_TO_IMAGE_FUNCTION5(path)
        plt.imsave("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage5.png", overlay5,cmap='gray')
    except:
        print('ERROR')
        pass
    
#This Section Read image processing the function
    thresholded_master_image5,master_images5=IMAGEPROCESSING5.process_image5("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage5.png")
    PatientID5,PatientStudyDate5,Manufacturer5,ManufacturerModelName5,StudyDescription5,PatientAge5,PatientSex5,Contrastgroup5,InstitutionName5,InstitutionGroup5,OperatorName5=METADATAPYDICOMANALYSIS5.Metadata_pydicom_analysis5(path)
    TotalDLParr5,series_5,DLP_series_5,CTDI_series_5,scan_length_5,Compilledscan5=REGIONOFINTEREST5.regionofinteresttesting5(thresholded_master_image5,master_images5,ManufacturerModelName5,path,Series_library)
    Compilleddata5= TOEXCEL5.toexcel(PatientID5,TotalDLParr5,series_5,DLP_series_5,CTDI_series_5,scan_length_5,PatientStudyDate5,Manufacturer5,ManufacturerModelName5,StudyDescription5,path,PatientAge5,PatientSex5,Contrastgroup5,InstitutionName5,InstitutionGroup5,OperatorName5)
    q5.put(Compilleddata5)
    q5A.put(Compilledscan5)
    return Compilleddata5