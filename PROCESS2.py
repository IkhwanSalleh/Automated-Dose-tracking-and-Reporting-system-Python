# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:38:25 2019

@author: 60111
"""

import DICOMTOIMAGE2
import IMAGEPROCESSING2
import METADATAPYDICOMANALYSIS2
import REGIONOFINTEREST2
import TOEXCEL2
from matplotlib import pyplot as plt


def processingmaster2(path,q2,Series_library,q2A):
    
    try:
        overlay2=DICOMTOIMAGE2.DICOM_TO_IMAGE_FUNCTION2(path)
        plt.imsave("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage2.png", overlay2,cmap='gray')
    except:
        print('ERROR')
        pass
    
#This Section Read image processing the function
    thresholded_master_image2,master_images2=IMAGEPROCESSING2.process_image2("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage2.png")
    PatientID2,PatientStudyDate2,Manufacturer2,ManufacturerModelName2,StudyDescription2,PatientAge2,PatientSex2,Contrastgroup2,InstitutionName2,InstitutionGroup2,OperatorName2=METADATAPYDICOMANALYSIS2.Metadata_pydicom_analysis2(path)
    TotalDLParr2,series_2,DLP_series_2,CTDI_series_2,scan_length_2,Compilledscan2=REGIONOFINTEREST2.regionofinteresttesting2(thresholded_master_image2,master_images2,ManufacturerModelName2,path,Series_library)
    Compilleddata2= TOEXCEL2.toexcel(PatientID2,TotalDLParr2,series_2,DLP_series_2,CTDI_series_2,scan_length_2,PatientStudyDate2,Manufacturer2,ManufacturerModelName2,StudyDescription2,path,PatientAge2,PatientSex2,Contrastgroup2,InstitutionName2,InstitutionGroup2,OperatorName2)
    q2.put(Compilleddata2)
    q2A.put(Compilledscan2)
    return Compilleddata2