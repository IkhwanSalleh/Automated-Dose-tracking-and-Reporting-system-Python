# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:18:09 2019

@author: 60111
"""
import pydicom
import INSTITUTIONGROUPS
def Metadata_pydicom_analysis1(Input_from_server1):#This is where we analyses the metadata of the dicom files
    meta_data_pydicom1 = pydicom.dcmread(Input_from_server1) #get dicom files from the server central files dicom
    
    Patient_ID1=[""]
    Patient_ID1[0]=meta_data_pydicom1.PatientID
    

    Patient_StudyDate1=meta_data_pydicom1.StudyDate
    
    Manufacturer1=['']
    Manufacturer1[0]=meta_data_pydicom1.Manufacturer
    ManufacturerModelName1=['']
    ManufacturerModelName1[0]=meta_data_pydicom1.ManufacturerModelName
    try:
        StudyDescription1=meta_data_pydicom1.StudyDescription
    except:
        StudyDescription1=''
    try:
        PatientAge1=meta_data_pydicom1.PatientAge
    except:
        PatientAge1='0Y'
    try:
        PatientSex1=meta_data_pydicom1.PatientSex
    except:
        PatientSex1='UNKNOWN'
    try:
        codemeaning1=meta_data_pydicom1.RequestedProcedureDescription
        codemeaning1=codemeaning1.upper()
        if 'NON CONTRAST' in codemeaning1:
            Contrastgroup1='Yes'
        else:
            Contrastgroup1='No'
    except:
        Contrastgroup1='UNKNOWN'
    try:
        InstitutionName1=meta_data_pydicom1.InstitutionName
        InstitutionGroup1=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName1)
    except:
        InstitutionName1='UNSPECIFIED'
        InstitutionGroup1=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName1)
    try:
        OperatorName1=meta_data_pydicom1.OperatorsName
    except:
        OperatorName1='UNKNOWN'
    
    
    return Patient_ID1,Patient_StudyDate1,Manufacturer1,ManufacturerModelName1,StudyDescription1,PatientAge1,PatientSex1,Contrastgroup1,InstitutionName1,InstitutionGroup1,OperatorName1