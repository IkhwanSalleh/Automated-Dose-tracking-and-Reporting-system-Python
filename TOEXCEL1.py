# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:24:32 2019

@author: 60111
"""
import PatientStudyDateGroup1
import Studygrouplibrary as Lib2
import regex as re
import pandas
def toexcel(PatientID,TotalDLParr1,series_1,DLP_series_1,CTDI_series_1,scan_length_1,PatientStudyDate,Manufacturer,ManufacturerModelName,StudyDescription,path,PatientAge,PatientSex,Contrastgroup,InstitutionName1,InstitutionGroup1,OperatorName1):
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
    
    Compileddataexcel=pandas.DataFrame({'PatientID':PatientID,'PatientAge':PatientAgearr,'AgeGroup':PatientAgegrouparr,'PatientSsex':PatientSexarr,'Study Date':PatientStudyDate,'Day':Studyday,'Month':Studymonth,'Year':Studyyear,'Date Group':Studygroup,'Manufacturer':Manufacturer,'ManufacturerModelName':ManufacturerModelName,'StudyDescription':studydescriptionarr,'Group':StudyGrouparr,'Series 1 scan':series_1[0],'Series 1 DLP':DLP_series_1[0],'Series 1 CTDI':CTDI_series_1[0],'Series 2 scan':series_1[1],'Series 2 DLP':DLP_series_1[1],'Series 2 CTDI':CTDI_series_1[1],'Series 3 scan':series_1[2],'Series 3 DLP':DLP_series_1[2],'Series 3 CTDI':CTDI_series_1[2],'Series 4 scan':series_1[3],'Series 4 DLP':DLP_series_1[3],'Series 4 CTDI':CTDI_series_1[3],'TotalDLP':TotalDLParr1,'Scan Length':scan_length_1,'InstitutionName':InstitutionName1,'InstitutionGroup':InstitutionGroup1,'Path':patharr})
    
    return Compileddataexcel