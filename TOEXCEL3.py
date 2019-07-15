# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:24:32 2019

@author: 60111
"""
import PatientStudyDateGroup2
import Studygrouplibrary as Lib2
import regex as re
import pandas
def toexcel(PatientID,TotalDLParr3,series_3,DLP_series_3,CTDI_series_3,scan_length_3,PatientStudyDate,Manufacturer,ManufacturerModelName,StudyDescription,path,PatientAge,PatientSex,Contrastgroup,InstitutionName3,InstitutionGroup3,OperatorName3):
    StudyGroup,StudyCode=Lib2.typeofscanstudy(StudyDescription)
    patharr=['']
    patharr[0]=path
    
    studydescriptionarr=['']
    studydescriptionarr[0]=StudyDescription
    
    
    StudyGrouparr=['']
    StudyGrouparr[0]=StudyGroup
    PatientAgearr=['']
    PatientAgearr[0]=PatientAge
    PatientAgearr3=re.sub("\D","",PatientAge)
    if int(PatientAgearr3) <= 18:
        AgeGroup='CHILD'
    else:
        AgeGroup='ADULT'
    PatientAgegrouparr=['']  
    PatientAgegrouparr[0]=AgeGroup
    PatientSexarr=['']
    PatientSexarr[0]=PatientSex
    Studyyear,Studymonth,Studyday,Studygroup=PatientStudyDateGroup2.PatientStudyDtae_to_PatientStudydateGroup2(PatientStudyDate)    
    
    Compileddataexcel=pandas.DataFrame({'PatientID':PatientID,'PatientAge':PatientAgearr,'AgeGroup':PatientAgegrouparr,'PatientSsex':PatientSexarr,'Study Date':PatientStudyDate,'Day':Studyday,'Month':Studymonth,'Year':Studyyear,'Date Group':Studygroup,'Manufacturer':Manufacturer,'ManufacturerModelName':ManufacturerModelName,'StudyDescription':studydescriptionarr,'Group':StudyGrouparr,'Series 1 scan':series_3[0],'Series 1 DLP':DLP_series_3[0],'Series 1 CTDI':CTDI_series_3[0],'Series 2 scan':series_3[1],'Series 2 DLP':DLP_series_3[1],'Series 2 CTDI':CTDI_series_3[1],'Series 3 scan':series_3[2],'Series 3 DLP':DLP_series_3[2],'Series 3 CTDI':CTDI_series_3[2],'Series 4 scan':series_3[3],'Series 4 DLP':DLP_series_3[3],'Series 4 CTDI':CTDI_series_3[3],'TotalDLP':TotalDLParr3,'Scan Length':scan_length_3,'InstitutionName':InstitutionName3,'InstitutionGroup':InstitutionGroup3,'Path':patharr})
    return Compileddataexcel