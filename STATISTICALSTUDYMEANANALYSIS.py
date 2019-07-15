# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 23:23:36 2019

@author: 60111
"""
import numpy as np
import pandas
import Sheet_Selection as Lib3

def statisticalStudyMeananalysis(results):
    studyanalysis=list(np.arange(0,1000))
    HEADBRAINstudyanalysis=list(np.arange(0,1000))
    NECKstudyanalysis=list(np.arange(0,1000))
    CHESTstudyanalysis=list(np.arange(0,1000))
    ABDOMENstudyanalysis=list(np.arange(0,1000))
    PELVISstudyanalysis=list(np.arange(0,1000))
    THORAXstudyanalysis=list(np.arange(0,1000))
    ABDOMENPELVISstudyanalysis=list(np.arange(0,1000))
    NECKCHESTstudyanalysis=list(np.arange(0,1000))
    HEADBRAINNECKstudyanalysis=list(np.arange(0,1000))
    NECKTHORAXstudyanalysis=list(np.arange(0,1000))
    HEADTHORAXstudyanalysis=list(np.arange(0,1000))
    CARDIACstudyanalysis=list(np.arange(0,1000))
    SPINEstudyanalysis=list(np.arange(0,1000))
    VASCULARstudyanalysis=list(np.arange(0,1000))
    EXTREMETIESstudyanalysis=list(np.arange(0,1000))
    OTHERstudyanalysis=list(np.arange(0,1000))
    j=0
    jHEADBRAIN=0
    jNECK=0
    jCHEST=0
    jABDOMEN=0
    jPELVIS=0
    jTHORAX=0
    jABDOMENPELVIS=0
    jNECKCHEST=0
    jHEADBRAINNECK=0
    jNECKTHORAX=0
    jHEADTHORAX=0
    jCARDIAC=0
    jSPINE=0
    jVASCULAR=0
    jEXTREMETIES=0
    jOTHER=0
    
    
    for i in results:
        i=str(i).upper()
        if i in studyanalysis:
            pass
        else:
            if 'HEAD ,BRAIN' in i:
                HEADBRAINstudyanalysis[jHEADBRAIN]=i
                jHEADBRAIN=jHEADBRAIN+1
            elif 'NECK' in i:
                NECKstudyanalysis[jNECK]=i
                jNECK=jNECK+1
            elif 'CHEST' in i:
                CHESTstudyanalysis[jCHEST]=i
                jCHEST=jCHEST+1
            elif 'ABDOMEN' in i:
                ABDOMENstudyanalysis[jABDOMEN]=i
                jABDOMEN=jABDOMEN+1
            elif 'ABDOMEN&PELVIS' in i:
                ABDOMENPELVISstudyanalysis[jABDOMENPELVIS]=i
                jABDOMENPELVIS=jABDOMENPELVIS+1
            elif 'NECK&CHEST' in i:
                NECKCHESTstudyanalysis[jNECKCHEST]=i
                jNECKCHEST=jNECKCHEST+1
            elif 'HEAD,BRAIN,NECK' in i:
                HEADBRAINNECKstudyanalysis[jHEADBRAINNECK]=i
                jHEADBRAINNECK=jHEADBRAINNECK+1
            elif 'NECK.THORAX' in i:
                NECKTHORAXstudyanalysis[jNECKTHORAX]=i
                jNECKTHORAX=jNECKTHORAX+1
            elif 'CARDIAC' in i:
                CARDIACstudyanalysis[jCARDIAC]=i
                jCARDIAC=jCARDIAC+1
            elif 'HEAD,THORAX' in i:
                HEADTHORAXstudyanalysis[jHEADTHORAX]=i
                jHEADTHORAX=jHEADTHORAX+1
            elif 'VASCULAR' in i:
                VASCULARstudyanalysis[jVASCULAR]=i
                jVASCULAR=jVASCULAR+1
            elif 'PELVIS' in i:
                PELVISstudyanalysis[jPELVIS]=i
                jPELVIS=jPELVIS+1
            elif 'SPINE' in i:
                SPINEstudyanalysis[jSPINE]=i
                jSPINE=jSPINE+1
            elif 'THORAX' in i:
                THORAXstudyanalysis[jTHORAX]=i
                jTHORAX=jTHORAX+1
            elif 'EXTREMETIES' in i:
                EXTREMETIESstudyanalysis[jEXTREMETIES]=i
                jEXTREMETIES=jEXTREMETIES+1
            else: 
                OTHERstudyanalysis[jOTHER]=i
                jOTHER=jOTHER+1
            studyanalysis[j]=i
            j=j+1
            
    studycompilleddata=pandas.DataFrame({'STUDYDESCRIPTION':studyanalysis,'HEAD ,BRAIN':HEADBRAINstudyanalysis,'NECK':NECKstudyanalysis,'CHEST':CHESTstudyanalysis,'ABDOMEN':ABDOMENstudyanalysis,'ABDOMEN&PELVIS':ABDOMENPELVISstudyanalysis,'NECK&CHEST':NECKCHESTstudyanalysis,'HEAD,BRAIN,NECK':HEADBRAINNECKstudyanalysis,'NECK&THORAX':NECKTHORAXstudyanalysis,'HEAD&THORAX':HEADTHORAXstudyanalysis,'CARDIAC':CARDIACstudyanalysis,'VASCULAR':VASCULARstudyanalysis,'PELVIS':PELVISstudyanalysis,'SPINE':SPINEstudyanalysis,'THORAX':THORAXstudyanalysis,'EXTREMETIES':EXTREMETIESstudyanalysis,'OTHER STUDY':OTHERstudyanalysis})
    Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',studycompilleddata,sheet_name='CT STUDY GROUP',startcol=0)    
                
        
    return studyanalysis

            