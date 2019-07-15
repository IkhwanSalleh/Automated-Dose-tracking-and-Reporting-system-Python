# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:48:01 2019

@author: 60111
"""
from datetime import datetime
import calendar
def PatientStudyDtae_to_PatientStudydateGroup(Study_date1):
    Studydate1=str(Study_date1)
    Studydate1=datetime.strptime(Studydate1,'%Y%m%d').date()
    Studyyear1=Studydate1.year
    Studymonth1=calendar.month_name[Studydate1.month]
    Studyday1=Studydate1.day
    Studygroup1="{}-{}".format(Studydate1.year,calendar.month_name[Studydate1.month])
    
    return  Studyyear1,Studymonth1,Studyday1,Studygroup1