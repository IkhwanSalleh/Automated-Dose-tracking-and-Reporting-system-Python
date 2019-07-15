# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:18:09 2019

@author: 60111
"""
import pydicom
import INSTITUTIONGROUPS
def Metadata_pydicom_analysis4(Input_from_server):#This is where we analyses the metadata of the dicom files
    meta_data_pydicom4 = pydicom.dcmread(Input_from_server) #get dicom files from the server central files dicom
    Patient_ID4=[""]
    Patient_ID4[0]=meta_data_pydicom4.PatientID
    

    
    Patient_StudyDate4=meta_data_pydicom4.StudyDate
    
    Manufacturer4=['']
    Manufacturer4[0]=meta_data_pydicom4.Manufacturer
    ManufacturerModelName4=['']
    ManufacturerModelName4[0]=meta_data_pydicom4.ManufacturerModelName
    try:
        StudyDescription4=meta_data_pydicom4.StudyDescription
    except:
        StudyDescription4=''
    try:
        PatientAge4=meta_data_pydicom4.PatientAge
    except:
        PatientAge4='0Y'
    try:
        PatientSex4=meta_data_pydicom4.PatientSex
    except:
        PatientSex4='UNKNOWN'
    try:
        codemeaning4=meta_data_pydicom4.RequestedProcedureDescription
        codemeaning4=codemeaning4.upper()
        if 'NON CONTRAST' in codemeaning4:
            Contrastgroup4='Yes'
        else:
            Contrastgroup4='No'
    except:
        Contrastgroup4='UNKNOWN'
    try:
        InstitutionName4=meta_data_pydicom4.InstitutionName
        InstitutionGroup4=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName4)
    except:
        InstitutionName4='UNSPECIFIED'
        InstitutionGroup4=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName4)
    try:
        OperatorName4=meta_data_pydicom4.OperatorsName
    except:
        OperatorName4='UNKNOWN'
    
    return Patient_ID4,Patient_StudyDate4,Manufacturer4,ManufacturerModelName4,StudyDescription4,PatientAge4,PatientSex4,Contrastgroup4,InstitutionName4,InstitutionGroup4,OperatorName4