# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:18:09 2019

@author: 60111
"""
import pydicom
import INSTITUTIONGROUPS
def Metadata_pydicom_analysis2(Input_from_server2):#This is where we analyses the metadata of the dicom files
    meta_data_pydicom2 = pydicom.dcmread(Input_from_server2) #get dicom files from the server central files dicom
    Patient_ID2=[""]
    Patient_ID2[0]=meta_data_pydicom2.PatientID
    

    
    Patient_StudyDate2=meta_data_pydicom2.StudyDate
    
    Manufacturer2=['']
    Manufacturer2[0]=meta_data_pydicom2.Manufacturer
    ManufacturerModelName2=['']
    ManufacturerModelName2[0]=meta_data_pydicom2.ManufacturerModelName
    try:
        StudyDescription2=meta_data_pydicom2.StudyDescription
    except:
        StudyDescription2=''
    try:
        PatientAge2=meta_data_pydicom2.PatientAge
    except:
        PatientAge2='0Y'
    try:
        PatientSex2=meta_data_pydicom2.PatientSex
    except:
        PatientSex2='UNKNOWN'
    try:
        codemeaning2=meta_data_pydicom2.RequestedProcedureDescription
        codemeaning2=codemeaning2.upper()
        if 'NON CONTRAST' in codemeaning2:
            Contrastgroup2='Yes'
        else:
            Contrastgroup2='No'
    except:
        Contrastgroup2='UNKNOWN'
    try:
        InstitutionName2=meta_data_pydicom2.InstitutionName
        InstitutionGroup2=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName2)
    except:
        InstitutionName2='UNSPECIFIED'
        InstitutionGroup2=INSTITUTIONGROUPS.InstitutionNameLocation(InstitutionName2)
    try:
        OperatorName2=meta_data_pydicom2.OperatorsName
    except:
        OperatorName2='UNKNOWN'
    
    return Patient_ID2,Patient_StudyDate2,Manufacturer2,ManufacturerModelName2,StudyDescription2,PatientAge2,PatientSex2,Contrastgroup2,InstitutionName2,InstitutionGroup2,OperatorName2