# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:18:09 2019

@author: 60111
"""
import pydicom
import INSTITUTIONGROUPS
def Metadata_pydicom_analysis5(Input_from_server5):#This is where we analyses the metadata of the dicom files
    meta_data_pydicom5 = pydicom.dcmread(Input_from_server5) #get dicom files from the server central files dicom
    
    Patient_ID5=[""]
    Patient_ID5[0]=meta_data_pydicom5.PatientID
    

    Patient_StudyDate5=meta_data_pydicom5.StudyDate
    
    Manufacturer5=['']
    Manufacturer5[0]=meta_data_pydicom5.Manufacturer
    ManufacturerModelName5=['']
    ManufacturerModelName5[0]=meta_data_pydicom5.ManufacturerModelName
    try:
        StudyDescription5=meta_data_pydicom5.StudyDescription
    except:
        StudyDescription5=''
    try:
        PatientAge5=meta_data_pydicom5.PatientAge
    except:
        PatientAge5='0Y'
    try:
        PatientSex5=meta_data_pydicom5.PatientSex
    except:
        PatientSex5='UNKNOWN'
    try:
        codemeaning5=meta_data_pydicom5.RequestedProcedureDescription
        codemeaning5=codemeaning5.upper()
        if 'NON CONTRAST' in codemeaning5:
            Contrastgroup5='Yes'
        else:
            Contrastgroup5='No'
    except:
        Contrastgroup5='UNKNOWN'
    try:
        InstitutionName5=meta_data_pydicom5.InstitutionName
        InstitutionGroup5=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName5)
    except:
        InstitutionName5='UNSPECIFIED'
        InstitutionGroup5=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName5)
    try:
        OperatorName5=meta_data_pydicom5.OperatorsName
    except:
        OperatorName5='UNKNOWN'
    
    
    return Patient_ID5,Patient_StudyDate5,Manufacturer5,ManufacturerModelName5,StudyDescription5,PatientAge5,PatientSex5,Contrastgroup5,InstitutionName5,InstitutionGroup5,OperatorName5