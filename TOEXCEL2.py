# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:24:32 2019

@author: 60111
"""
import PatientStudyDateGroup1
import Studygrouplibrary as Lib2
import regex as re
import pandas
def toexcel(PatientID,TotalDLParr2,series_2,DLP_series_2,CTDI_series_2,scan_length_2,PatientStudyDate,Manufacturer,ManufacturerModelName,StudyDescription,path,PatientAge,PatientSex,Contrastgroup,InstitutionName2,InstitutionGroup2,OperatorName2):
    StudyGroup,StudyCode=Lib2.typeofscanstudy(StudyDescription)
    patharr=['']
    patharr[0]=path
    
    studydescriptionarr=['']
    studydescriptionarr[0]=StudyDescription
    
    
    StudyGrouparr=['']
    StudyGrouparr[0]=StudyGroup
    PatientAgearr=['']
    PatientAgearr[0]=PatientAge
    PatientAgearr2=re.sub("\D","",PatientAge)
    if int(PatientAgearr2) <= 18:
        AgeGroup='CHILD'
    else:
        AgeGroup='ADULT'
    PatientAgegrouparr=['']  
    PatientAgegrouparr[0]=AgeGroup
    PatientSexarr=['']
    PatientSexarr[0]=PatientSex
    Studyyear,Studymonth,Studyday,Studygroup=PatientStudyDateGroup1.PatientStudyDtae_to_PatientStudydateGroup(PatientStudyDate)   
    
    Compileddataexcel=pandas.DataFrame({'PatientID':PatientID,'PatientAge':PatientAgearr,'AgeGroup':PatientAgegrouparr,'PatientSsex':PatientSexarr,'Study Date':PatientStudyDate,'Day':Studyday,'Month':Studymonth,'Year':Studyyear,'Date Group':Studygroup,'Manufacturer':Manufacturer,'ManufacturerModelName':ManufacturerModelName,'StudyDescription':studydescriptionarr,'Group':StudyGrouparr,'Series 1 scan':series_2[0],'Series 1 DLP':DLP_series_2[0],'Series 1 CTDI':CTDI_series_2[0],'Series 2 scan':series_2[1],'Series 2 DLP':DLP_series_2[1],'Series 2 CTDI':CTDI_series_2[1],'Series 3 scan':series_2[2],'Series 3 DLP':DLP_series_2[2],'Series 3 CTDI':CTDI_series_2[2],'Series 4 scan':series_2[3],'Series 4 DLP':DLP_series_2[3],'Series 4 CTDI':CTDI_series_2[3],'TotalDLP':TotalDLParr2,'Scan Length':scan_length_2,'InstitutionName':InstitutionName2,'InstitutionGroup':InstitutionGroup2,'Path':patharr})
    return Compileddataexcel