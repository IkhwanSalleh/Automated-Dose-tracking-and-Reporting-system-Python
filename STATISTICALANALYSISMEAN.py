# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:00:51 2019

@author: 60111
This is a function to perform a statistical analysis on the data
"""

def StatisticalAnalysisMean(group , TotalDLP , STUDYCOUNT):
    j=0
    CTABDOMENMEAN=0
    CTCARDIACMEAN=0
    CTBRAINMEAN=0
    CTCHESTMEAN=0
    CTHEADMEAN=0
    CTPELVISMEAN=0
    CTSPINEMEAN=0
    CTTHORAXMEAN=0
    CTWHOLEBODYMEAN=0
    CTOTHERMEAN=0
    for i in group:
        if  'CT ABDOMEN' in i:
            CTABDOMENMEAN=CTABDOMENMEAN+TotalDLP[j]
        elif 'CT CARDIAC'in i:
            CTCARDIACMEAN=CTCARDIACMEAN+TotalDLP[j]
        elif 'CT BRAIN' in i:
            CTBRAINMEAN=CTBRAINMEAN+TotalDLP[j]
        elif 'CT CHEST' in i:
            CTCHESTMEAN=CTCHESTMEAN+TotalDLP[j]
        elif 'CT HEAD' in i:
            CTHEADMEAN=CTHEADMEAN+TotalDLP[j]
        elif 'CT PELVIS' in i:
            CTPELVISMEAN=CTPELVISMEAN+TotalDLP[j]
        elif 'CT SPINE' in i:
            CTSPINEMEAN=CTSPINEMEAN+TotalDLP[j]
        elif 'CT THORAX' in i:
            CTTHORAXMEAN=CTTHORAXMEAN+TotalDLP[j]
        elif 'CT WHOLEBODY' in i:
            CTWHOLEBODYMEAN=CTWHOLEBODYMEAN+TotalDLP[j]
        else:
            CTOTHERMEAN=CTOTHERMEAN+TotalDLP[j]
        j=j+1
    
    STUDYMEAN=[(CTABDOMENMEAN/STUDYCOUNT[0]),(CTCARDIACMEAN/STUDYCOUNT[1]),(CTBRAINMEAN/STUDYCOUNT[2]),(CTCHESTMEAN/STUDYCOUNT[3]),(CTHEADMEAN/STUDYCOUNT[4]),(CTPELVISMEAN/STUDYCOUNT[5]),(CTSPINEMEAN/STUDYCOUNT[6]),(CTTHORAXMEAN/STUDYCOUNT[7]),(CTWHOLEBODYMEAN/STUDYCOUNT[8]),(CTOTHERMEAN/STUDYCOUNT[9])]
    return STUDYMEAN     

