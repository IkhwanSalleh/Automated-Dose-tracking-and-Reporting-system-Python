# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:06:28 2019

@author: Ikhwan Salleh
"""
import pandas

def typeofscanstudy(results):
    try:
        studydescription=str(results).upper()
    except:
        try:
            studydescription=results.upper()
        except:
            studydescription='CT OTHER'
            
    Rawdata=pandas.read_excel('STUDY LIBRARY.xlsx')
    Rawdata=Rawdata.fillna(value=0)
    Headbrain='Head and Brain'
    HeadNeck='Head to Neck'
    HeadCAP='Head and C/A/P'
    Neck='Neck'
    NeakCAP='Neck and C/A/P'
    Chest='Chest'
    ChestAbdomen='Chest and Abdomen'
    CAP='Chest,Abdomen and Pelvis'
    Abdomen='Abdomen'
    AbdomenPelvis='Abdomen and Pelvis'
    Liver='Liver'
    Renal='Renal'
    Kidney='Kidney'
    Pancrease='Pancrease'
    Pelvis='Pelvis'
    SpineFull='Spine,Full'
    Adrenal='Adrenal'
    SpineCervical='Spine,Cervical'
    SpineThoSac='Spine,Thoracic to sacral'
    SpineLumbar='Spine,Lumbar'
    SpineLumSac='Spine,Lumbar to Sacral'
    SpineTho='Spine,Thoracic'
    SpineOth='Spine,Other'
    Limb='Limbs Extremeties'
    CTACor='CTA,Coronary'
    CTABra='CTA,Brain'
    CTAOth='CTA,other'
    Other='OTHER'
    
    
    HEADBRAINCT=list(Rawdata[Headbrain])
    HEADNECKCT=list(Rawdata[HeadNeck])
    HEADCAPCT=list(Rawdata[HeadCAP])
    NECKCT=list(Rawdata[Neck])
    NECKCAPCT=list(Rawdata[NeakCAP])
    CHESTCT=list(Rawdata[Chest])
    CHESTABDOMENCT=list(Rawdata[ChestAbdomen])
    CHESTABDOMENPELVIS=list(Rawdata[CAP])
    ABDOMENCT=list(Rawdata[Abdomen])
    ABDOMENPELVISCT=list(Rawdata[AbdomenPelvis])
    LIVERCT=list(Rawdata[Liver])
    RENAL=list(Rawdata[Renal])
    KIDNEYCT=list(Rawdata[Kidney])
    ADRENALCT=list(Rawdata[Adrenal])
    PANCREASECT=list(Rawdata[Pancrease])
    PELVISCT=list(Rawdata[Pelvis])
    SPINEFULLCT=list(Rawdata[SpineFull])
    SPINECERVICALCT=list(Rawdata[SpineCervical])
    SPINETHORACICSACRALCT=list(Rawdata[SpineThoSac])
    SPINELUMBARCT=list(Rawdata[SpineLumbar])
    SPINELUMBARSACRALCT=list(Rawdata[SpineLumSac])
    SPINETHORACICCT=list(Rawdata[SpineTho])
    SPINEOTHERCT=list(Rawdata[SpineOth])
    LIMBCT=list(Rawdata[Limb])
    CTACORONARYCT=list(Rawdata[CTACor])
    CTABRAINCT=list(Rawdata[CTABra])
    CTAOTHERCT=list(Rawdata[CTAOth])
    OTHERCT=list(Rawdata[Other])
    

    #Upper region of the body
    
    if studydescription in HEADBRAINCT :
        Studygroup = Headbrain
        StudyCode= 1
        
    elif studydescription in HEADNECKCT :
        Studygroup = HeadNeck
        StudyCode=2
        
    elif studydescription in HEADCAPCT :
        Studygroup = HeadCAP
        StudyCode=3
        
    elif studydescription in NECKCT :
        Studygroup = Neck
        StudyCode=4
        
    elif studydescription in NECKCAPCT :
        Studygroup = NeakCAP
        StudyCode=5
    elif studydescription in CHESTCT :
        Studygroup = Chest
        StudyCode=6
    elif studydescription in CHESTABDOMENCT :
        Studygroup = ChestAbdomen
        StudyCode=7
    elif studydescription in CHESTABDOMENPELVIS :
        Studygroup = CAP
        StudyCode=8
    elif studydescription in ABDOMENCT :
        Studygroup = Abdomen
        StudyCode=9
    elif studydescription in  ABDOMENPELVISCT :
        Studygroup = AbdomenPelvis
        StudyCode=10
    elif studydescription in LIVERCT :
        Studygroup = Liver
        StudyCode=11
    elif studydescription in RENAL :
        Studygroup = Renal
        StudyCode=12
    elif studydescription in KIDNEYCT :
        Studygroup = Kidney
        StudyCode=13
    elif studydescription in ADRENALCT:
        Studygroup = Adrenal
        StudyCode=14
    elif studydescription in PANCREASECT :
        Studygroup = Pancrease
        StudyCode=15
    elif studydescription in PELVISCT :
        Studygroup = Pelvis
        StudyCode=16
    elif studydescription in SPINEFULLCT :
        Studygroup = SpineFull
        StudyCode=17
    elif studydescription in SPINECERVICALCT :
        Studygroup = SpineCervical
        StudyCode=18
    elif studydescription in SPINETHORACICSACRALCT :
        Studygroup = SpineThoSac
        StudyCode=19
    elif studydescription in SPINELUMBARCT :
        Studygroup = SpineLumbar
        StudyCode=20
    elif studydescription in SPINELUMBARSACRALCT :
        Studygroup = SpineLumSac
        StudyCode=21
    elif studydescription in SPINETHORACICCT :
        Studygroup = SpineTho
        StudyCode=22
    elif studydescription in SPINEOTHERCT :
        Studygroup = SpineOth
        StudyCode=23
    elif studydescription in LIMBCT :
        Studygroup = Limb
        StudyCode=24
    elif studydescription in CTACORONARYCT :
        Studygroup = CTACor
        StudyCode=25
    elif studydescription in CTABRAINCT :
        Studygroup = CTABra
        StudyCode=26
    elif studydescription in CTAOTHERCT :
        Studygroup = CTAOth
        StudyCode=27
    elif studydescription in OTHERCT :
        Studygroup = Other
        StudyCode=28
    else:
        Studygroup = 'UNSPECIFIED'
        StudyCode=0
    
    return Studygroup,StudyCode