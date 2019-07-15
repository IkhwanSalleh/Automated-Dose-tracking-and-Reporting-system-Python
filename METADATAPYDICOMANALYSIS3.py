# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:18:09 2019

@author: 60111
"""
import pydicom
import INSTITUTIONGROUPS
def Metadata_pydicom_analysis3(Input_from_server3):#This is where we analyses the metadata of the dicom files
    meta_data_pydicom3 = pydicom.dcmread(Input_from_server3) #get dicom files from the server central files dicom
    Patient_ID3=[""]
    Patient_ID3[0]=meta_data_pydicom3.PatientID
    

    Patient_StudyDate3=meta_data_pydicom3.StudyDate
    
    Manufacturer3=['']
    Manufacturer3[0]=meta_data_pydicom3.Manufacturer
    ManufacturerModelName3=['']
    ManufacturerModelName3[0]=meta_data_pydicom3.ManufacturerModelName
    try:
        StudyDescription3=meta_data_pydicom3.StudyDescription
    except:
        StudyDescription3=''
    try:
        PatientAge3=meta_data_pydicom3.PatientAge
    except:
        PatientAge3='0Y'
    try:
        PatientSex3=meta_data_pydicom3.PatientSex
    except:
        PatientSex3='UNKNOWN'
    try:
        codemeaning3=meta_data_pydicom3.RequestedProcedureDescription
        codemeaning3=codemeaning3.upper()
        if 'NON CONTRAST' in codemeaning3:
            Contrastgroup3='Yes'
        else:
            Contrastgroup3='No'
    except:
        Contrastgroup3='UNKNOWN'
    try:
        InstitutionName3=meta_data_pydicom3.InstitutionName
        InstitutionGroup3=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName3)
    except:
        InstitutionName3='UNSPECIFIED'
        InstitutionGroup3=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName3) 
    try:
        OperatorName3=meta_data_pydicom3.OperatorsName
    except:
        OperatorName3='UNKNOWN'
    
    
    return Patient_ID3,Patient_StudyDate3,Manufacturer3,ManufacturerModelName3,StudyDescription3,PatientAge3,PatientSex3,Contrastgroup3,InstitutionName3,InstitutionGroup3,OperatorName3