# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:49:47 2019

@author: 60111
"""
import pandas
import Sheet_Selection as Lib3
def modelscounts(ManufacturerModelName):
    ManufacturerModel1=0
    ManufacturerModel2=0
    ManufacturerModel3=0
    ManufacturerModel4=0
    ManufacturerModel5=0
    ManufacturerModel6=0
    ManufacturerModel7=0
    ManufacturerModel8=0
    for i in ManufacturerModelName:
        if  'Sensation 16' in i:
            ManufacturerModel1=ManufacturerModel1+1
        elif 'Sensation Cardiac 64' in i:
            ManufacturerModel2=ManufacturerModel2+1
        elif 'SOMATAM Definition AS+' in i:
            ManufacturerModel3=ManufacturerModel3+1
        elif 'SOMATAM Definition' in i:
            ManufacturerModel4=ManufacturerModel4+1
        elif 'SOMATOM FORCE' in i:
            ManufacturerModel5=ManufacturerModel5+1
        elif 'Perspective' in i:
            ManufacturerModel6=ManufacturerModel6+1
        elif 'Emotion 16(2010)' in i:
            ManufacturerModel7=ManufacturerModel7+1
        elif'Emotion Duo' in i:
            ManufacturerModel8=ManufacturerModel8+1
        else:
            print(i)
    MODELSCOUNT=[ManufacturerModel1,ManufacturerModel2,ManufacturerModel3,ManufacturerModel4,ManufacturerModel5,ManufacturerModel6,ManufacturerModel7,ManufacturerModel8]
    MODELSTYPE=['Sensation 16','Sensation Cardiac 64','SOMATAM Deifinition AS+','SOMATAM Definition','SOMATAM FORCE','Perspective','Emotion 16(2010)','Emotion Duo']
    MODELcompilleddata=pandas.DataFrame({'MODEL TYPE':MODELSTYPE,'MODEL COUNTS':MODELSCOUNT})
    Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',MODELcompilleddata,sheet_name='CT MODEL ANALYSIS',startcol=0)
    
    return MODELcompilleddata
        
    
