# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:40:12 2019

@author: 60111
"""

import DICOMTOIMAGE3
import IMAGEPROCESSING3
import METADATAPYDICOMANALYSIS3
import REGIONOFINTEREST3
import TOEXCEL3
from matplotlib import pyplot as plt


def processingmaster3(path,q3,Series_library,q3A):
    
    try:
        overlay3=DICOMTOIMAGE3.DICOM_TO_IMAGE_FUNCTION3(path)
        plt.imsave("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage3.png", overlay3,cmap='gray')
    except:
        print('ERROR')
        pass
    
#This Section Read image processing the function
    thresholded_master_image3,master_images3=IMAGEPROCESSING3.process_image3("C:/Users/60111/Desktop/Python project/SUPPORTING FILES/DicomImage3.png")
    PatientID3,PatientStudyDate3,Manufacturer3,ManufacturerModelName3,StudyDescription3,PatientAge3,PatientSex3,Contrastgroup3,InstitutionName3,InstitutionGroup3,OperatorName3=METADATAPYDICOMANALYSIS3.Metadata_pydicom_analysis3(path)
    TotalDLParr3,series_3,DLP_series_3,CTDI_series_3,scan_length_3,Compilledscan3=REGIONOFINTEREST3.regionofinteresttesting3(thresholded_master_image3,master_images3,ManufacturerModelName3,path,Series_library)
    Compilleddata3= TOEXCEL3.toexcel(PatientID3,TotalDLParr3,series_3,DLP_series_3,CTDI_series_3,scan_length_3,PatientStudyDate3,Manufacturer3,ManufacturerModelName3,StudyDescription3,path,PatientAge3,PatientSex3,Contrastgroup3,InstitutionName3,InstitutionGroup3,OperatorName3)
    q3.put(Compilleddata3)
    q3A.put(Compilledscan3)
    return Compilleddata3