# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:02:58 2019

@author: Ikhwan Salleh
"""
import DICOMTOIMAGE1
import IMAGEPROCESSING1
import METADATAPYDICOMANALYSIS1
import REGIONOFINTEREST1
import TOEXCEL1
from matplotlib import pyplot as plt


def processingmaster1(path,q1,Series_library,q1A):
    
    try:
        overlay1=DICOMTOIMAGE1.DICOM_TO_IMAGE_FUNCTION1(path)
        plt.imsave("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage1.png", overlay1,cmap='gray')
    except:
        print('ERROR')
        pass
    
#This Section Read image processing the function
    thresholded_master_image1,master_images1=IMAGEPROCESSING1.process_image1("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage1.png")
    PatientID1,PatientStudyDate1,Manufacturer1,ManufacturerModelName1,StudyDescription1,PatientAge1,PatientSex1,Contrastgroup1,InstitutionName1,InstitutionGroup1,OperatorName1=METADATAPYDICOMANALYSIS1.Metadata_pydicom_analysis1(path)
    TotalDLParr1,series_1,DLP_series_1,CTDI_series_1,scan_length_1,Compilledscan1=REGIONOFINTEREST1.regionofinteresttesting1(thresholded_master_image1,master_images1,ManufacturerModelName1,path,Series_library)
    Compilleddata1= TOEXCEL1.toexcel(PatientID1,TotalDLParr1,series_1,DLP_series_1,CTDI_series_1,scan_length_1,PatientStudyDate1,Manufacturer1,ManufacturerModelName1,StudyDescription1,path,PatientAge1,PatientSex1,Contrastgroup1,InstitutionName1,InstitutionGroup1,OperatorName1)
    q1.put(Compilleddata1)
    q1A.put(Compilledscan1)
    return Compilleddata1,Compilledscan1