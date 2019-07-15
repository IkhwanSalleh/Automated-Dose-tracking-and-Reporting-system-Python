# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:48:01 2019

@author: 60111
"""
from datetime import datetime
import calendar
def PatientStudyDtae_to_PatientStudydateGroup2(Study_date2):
    Studydate2=str(Study_date2)
    Studydate2=datetime.strptime(Studydate2,'%Y%m%d').date()
    Studyyear2=Studydate2.year
    Studymonth2=calendar.month_name[Studydate2.month]
    Studyday2=Studydate2.day
    Studygroup2="{}-{}".format(Studydate2.year,calendar.month_name[Studydate2.month])
    
    return  Studyyear2,Studymonth2,Studyday2,Studygroup2