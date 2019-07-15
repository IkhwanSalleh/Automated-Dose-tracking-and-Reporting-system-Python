# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:47:32 2019

@author: Ikhwan Salleh
"""
import regex as re
#This is the library of series description of CT scan procedures
def typeofscan(Totalscan,i,blackcounter):
    scantesting=0
    serieslabel='PleaseChange:{}'.format(Totalscan)
    print(Totalscan)
#OTHER STUFF
    if 'TOPO' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'MONITORING' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'PREMONITORING' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'PATIENT POSITION H-SP' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'NEW POSITION' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'PATIENT POSITION F-SP' in Totalscan:
        scantesting=2
        blackcounter=0
        
    elif 'PATIENT POSITION H-PR' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'CONTRAST' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'CONT' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'TRACT' in Totalscan:
        scantesting=2
        blackcounter=0
    elif 'PET' in Totalscan:
        scantesting=2
        blackcounter=0
        
#Computed Tomography(CT) - Abdomen and pelvis
        #Subcategory
        #(A)Abdomen + Pelvis 1A
        #(B)Abdomen 1B
        #(C)Pelvis 1C
#ThorAbdPelvis
    elif 'ABD' in Totalscan:
        scantesting=1
        blackcounter=0
        re.sub("ABD","",Totalscan,count=1)
        if 'PEL' in Totalscan:
            re.sub("PEL","",Totalscan,count=1)
            if 'THO' in Totalscan:
                
                if 'IV' in Totalscan:
                    serieslabel='THORAX,ABDOMEN,PELVIS IV'
                elif 'V' in Totalscan:
                    serieslabel='THORAX,ABDOMEN,PELVIS IV'
                else:
                    serieslabel='THORAX,ABDOMEN,PELVIS'
                
            elif 'PVP' in Totalscan:
                serieslabel='ABDOMEN,PELVIS PVP'
            elif 'PYP' in Totalscan:
                serieslabel='ABDOMEN,PELVIS PVP'   
            elif 'NP' in Totalscan:
                serieslabel='ABDOMEN,PELVIS NP'
            elif 'IV' in Totalscan:
                serieslabel='ABDOMEN,PELVIS IV'
            elif 'PLAIN' in Totalscan:
                serieslabel='ABDOMEN,PELVIS PLAIN'
            elif 'IAN' in Totalscan:
                serieslabel='ABDOMEN,PELVIS PLAIN'
            elif 'I' in Totalscan:
                serieslabel='ABDOMEN,PELVIS IV'
            else:
                serieslabel='ABDOMEN,PELVIS'
                
        elif 'THO' in Totalscan:
            if 'PEL' in Totalscan:
               serieslabel='THORAX,ABDOMEN,PELVIS'
            elif 'ART' in Totalscan:
                serieslabel='THORAX, ABDOMEN ART'
            else:
                serieslabel='THORAX , ABDOMEN'
        elif 'PVP' in Totalscan:
            serieslabel='ABDOMEN PVP'
        elif 'PYP' in Totalscan:
            serieslabel='ABDOMEN PVP'
        elif 'PLAIN' in Totalscan:
            serieslabel='ABDOMEN PLAIN'
        elif 'IV' in Totalscan:
            serieslabel='ABDOMEN IV'
        elif 'VENOUS' in Totalscan:
            serieslabel='ABDOMEN VENOUS'
        elif 'I' in Totalscan:
            serieslabel='ABDOMEN IV'
        else:
            serieslabel=' ABDOMEN'
            
    #Pelvis    
    elif 'PEL' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'PLAIN' in Totalscan:
            serieslabel='PELVIS PLAIN'
        elif'IV' in Totalscan:
            serieslabel='PELVIS IV'
        elif'I' in Totalscan:
            serieslabel='PELVIS IV'
        elif'CYSTO' in Totalscan:
            serieslabel='PELVIS CYSTO'
        else: 
            serieslabel='PELVIS'
            
    elif 'THOR' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'IV' in Totalscan:
            serieslabel='THORAX IV'
        elif'HR' in Totalscan:
            serieslabel='THORAX HR'
        elif'C' in Totalscan:
            serieslabel='THORAX + CONTRAST'
        if 'I' in Totalscan:
            serieslabel='THORAX IV'
        else: 
            serieslabel='THORAX'

        
    elif 'RENAL' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'CMP' in Totalscan:
             serieslabel='RENAL CMP'
        elif 'NP' in Totalscan:
             serieslabel='RENAL NP'
        else:
             serieslabel='RENAL'
            
   
            
    elif 'SPINE' in Totalscan:
        scantesting = 1
        blackcounter=0
        serieslabel='SPINE'
    elif 'EMBOLISM' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='EMBOLISM'
    elif 'KIDNEY' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'CMP' in Totalscan:
            serieslabel='KIDNEY CMP'
        else:
            serieslabel='KIDNEY'
    
        
    
        
    elif 'NECK' in Totalscan:
        scantesting=1
        blackcounter=0
        re.sub("NECK","",Totalscan,count=1)
        if 'BD' in Totalscan:
            serieslabel='NECK IV'
        elif'CAP' in Totalscan:
            if 'IV' in Totalscan: 
                serieslabel='NECK CAP IV'
            elif 'V' in Totalscan: 
                serieslabel='NECK CAP IV'
            else:
                serieslabel='NECK CAP'
        elif'IV' in Totalscan:
            serieslabel='NECK IV'
        elif'I' in Totalscan:
            serieslabel='NECK IV'
        elif'V' in Totalscan:
            serieslabel='NECK IV'
        
        elif 'C' in Totalscan:
            serieslabel='NECK + CONTRAST'
        else:
            serieslabel='NECK'
        
    elif 'TAP' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'IV' in Totalscan: 
            serieslabel='TAP IV'
        elif 'I' in Totalscan:
            serieslabel='TAP IV'
        else:
            serieslabel='TAP'
            
    
#Computed Tomography(CT) - Head       
#NECK_BD
    
    
    
    
#HEAD    
    elif 'ANGIO' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'ART' in Totalscan:    
            serieslabel='ANGIO ART'
        elif 'RUN' in Totalscan:
            serieslabel='ANGIORUNOFF'
        elif 'HEAD' in Totalscan:
            serieslabel='HEADANGIO'
        elif 'CAROTID' in Totalscan:
            serieslabel='CAROTID ANGIO'
        elif 'PLAIN' in Totalscan:
            serieslabel='ANGIO PLAIN'
        else:
            serieslabel='ANGIO'
        
            
    elif 'HEAD' in Totalscan:
        scantesting = 1
        blackcounter=0
        if 'IV' in Totalscan:
            serieslabel='HEAD IV'
        elif 'IGS' in Totalscan:
            serieslabel='HEAD IGS'
        elif 'PLAIN' in Totalscan:
            serieslabel='HEAD PLAIN'
        elif 'Seq' in Totalscan:
            serieslabel='HEADSEQ PLAIN'
        elif 'G' in Totalscan:
            serieslabel='HEAD IGS'
        elif 'I' in Totalscan:
            serieslabel='HEAD IV'
        else:
            serieslabel='HEAD'
        
        
    
        
    
    
#BRAINS    
    elif 'BRAIN' in Totalscan:
        re.sub("BRAIN","",Totalscan,count=1)
        scantesting = 1
        blackcounter=0
        if 'PLAIN' in Totalscan:
            serieslabel='BRAIN PLAIN'
        elif 'ORBIT' in Totalscan:
            serieslabel='BRAIN ORBIT'
        elif 'SPIRAL' in Totalscan:
            re.sub("SPIRAL","",Totalscan,count=1)
            if 'IV' in Totalscan:
                serieslabel='Brain spiral IV'
            elif 'I' in Totalscan:
                serieslabel='Brain spiral IV'
            else:
                serieslabel='Brain spiral'
        elif 'CTA' in Totalscan:
           serieslabel='CTA BRAIN'
        elif 'TA' in Totalscan:
           serieslabel='CTA BRAIN'
        elif 'IV' in Totalscan:
            serieslabel='Brain IV'
        elif 'V' in Totalscan:
            serieslabel='Brain IV'
        else:
            serieslabel='Brain'
        
        
    elif 'CASCSEQ' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'DS' in Totalscan:
            serieslabel='DS_CaScSeq'
        else:
            serieslabel='CaScSeq'

    elif 'CORCTA' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'DS' in Totalscan:
            serieslabel='DS_CorCTA'
        else:
            serieslabel='CorCTA'
            
   
        
    elif 'SKULL' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'EXT' in Totalscan:
            serieslabel='SKULL EXT'
        else:
            serieslabel='SKULL'
    
    elif 'COLO' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'PRONE' in Totalscan:
            serieslabel='Colo Prone'
        elif 'SUPINE' in Totalscan:
            serieslabel='Colo Supine'
          
    elif 'INNER' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'EAR' in Totalscan:
            if 'UHR' in Totalscan:
                serieslabel='Inner Ear UHR'
            else:
                serieslabel='Inner Ear'
        else:
            serieslabel='Inner Ear'
        
#Computer Tomography(CT) - Others
#BLADDER

        
    elif 'DELAY' in Totalscan:
        scantesting = 1
        blackcounter=0
        if 'BLADDER' in Totalscan:
            serieslabel='Delay Bladder'
        elif 'BD' in Totalscan:
            serieslabel='Delay Bladder'
        elif 'PHASE' in Totalscan:
            serieslabel='Delay Phase'
        
        else:
            serieslabel='DELAY'
    

   
    elif 'BOLUS' in Totalscan:
        scantesting=1
        blackcounter=0
        re.sub("BOLUS","",Totalscan,count=1) 
        if 'TEST' in Totalscan:
            serieslabel='TestBolus'
        elif 'IV' in Totalscan:
            serieslabel='IV Bolus'
        elif '1.' in Totalscan:
            serieslabel='IV Bolus'
        elif 'I' in Totalscan:
            serieslabel='IV Bolus'
        else:
            serieslabel='Bolus'
        
    elif 'LIV' in Totalscan:
        scantesting=1
        blackcounter=0
        
        if 'EAP' in Totalscan:
            serieslabel='Liver EAP'
        elif 'LAP' in Totalscan:
            serieslabel='Liver LAP'
        elif 'PLAIN' in Totalscan:
            serieslabel='Liver Plain'
        elif 'DELAVED' in Totalscan:
            serieslabel='Delayed Liver'
        elif 'DELAYED' in Totalscan:
            serieslabel='Delayed liver'
        elif 'PANCR' in Totalscan:
            serieslabel='LIVER,PANCREASE'
        elif 'PAN' in Totalscan:
            serieslabel='LIVER,PANCREASE'
        else:
            serieslabel='LIVER'
            
    elif 'CAP' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'IV' in Totalscan:
            serieslabel='CAP IV'
        elif 'I' in Totalscan:
            serieslabel='CAP IV'
        elif 'PVP' in Totalscan:
            serieslabel='CAP PVP'
        elif 'PYP' in Totalscan:
            serieslabel='CAP PVP'
        else:
            serieslabel='CAP IV'
            
      
    elif 'SINUS' in Totalscan:
        scantesting = 1
        blackcounter=0
        if 'IV' in Totalscan:
            serieslabel='Sinus IV'
        elif 'I' in Totalscan:
            serieslabel='Sinus IV'
        elif 'PLAIN' in Totalscan:
            serieslabel='Sinus Plain'
        else:
            serieslabel='Sinus'
        
        
    elif 'PLAIN' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'ADRENAL' in Totalscan:
            serieslabel='Plain adrenal'
        elif 'RENAL' in Totalscan:
            serieslabel='Plain adrenal'
        elif 'LIVER' in Totalscan:
            serieslabel='Plain Liver'
        elif 'VER' in Totalscan:
            serieslabel='Plain Liver'
        elif 'SINUS' in Totalscan:
            serieslabel='Sinus Plain'
        else:
            serieslabel='Plain'
        
    elif 'CT' in Totalscan:
        scantesting=1
        blackcounter=0
        re.sub("CT","",Totalscan,count=1)
        if 'WB' in Totalscan:
            serieslabel='CT WB'
        elif 'EB' in Totalscan:
            serieslabel='CT WB'   
        elif 'WHOLESPINE' in Totalscan:
            serieslabel='CT Wholespine'
        elif 'BRAIN' in Totalscan:
            serieslabel='CTA Brain'
        elif 'THOR' in Totalscan:
            re.sub("THOR","",Totalscan,count=1)
            if 'LUM' in Totalscan:
                serieslabel='CT THOR/LUM'
            else:
                serieslabel='CT THORAXIC'
        elif 'FACIAL' in Totalscan:
            serieslabel='CT FACIAL'
        
        elif' EP' in Totalscan:
            serieslabel='CTU EP'
        elif 'W' in Totalscan:
            serieslabel='CT WB'
        elif 'U' in Totalscan:
            if 'IVU' in Totalscan:
                serieslabel='CTU IVU'
            else:
                serieslabel='CTU'
        elif 'A' in Totalscan:
            if 'DE' in Totalscan:
                serieslabel='DE CTA'
            elif'BRAIN' in Totalscan:
                serieslabel='CTA BRAIN'
            elif'IN' in Totalscan:
                serieslabel='CTA BRAIN'    
            else:
                serieslabel='CTA'
        else:
            serieslabel='CT:{}'.format(Totalscan)
    elif 'BLADDER' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='Bladder'
    elif 'BILATERAL LIMBS' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='Bilateral Limbs'
        
    elif 'PANCR' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'LIV' in Totalscan:
            serieslabel='LIVER , PANCREASE'
        elif 'EAP' in Totalscan:
            serieslabel='PANCREASE EAP'
        elif 'E' in Totalscan:
            serieslabel='PANCREASE EAP'
        else:
            serieslabel='PANCREASE'            
            
        
    elif 'BASE' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='Base'
    elif 'CRB' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='CRB'
    elif 'KNEE' in Totalscan:
        scantesting = 1
        blackcounter=0
        if 'BELOW' in Totalscan:
            serieslabel='Below Knee'
        else:
            serieslabel='Knee'
    elif 'FLUORO' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='Fluoro'
    elif 'LT HIP' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='LT HIP'
    elif 'LT KNEE' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='LT KNEE'
        
    elif 'LUNGLOWDOSE' in Totalscan:
        scantesting = 1
        blackcounter=0
        serieslabel='Lung Low Dose'
    elif 'AC' in Totalscan:
        scantesting = 1
        blackcounter=0
        if 'IV' in Totalscan:
            serieslabel='IAC IV'
        elif 'V' in Totalscan:
            serieslabel='IAC IV'
        else:
            serieslabel='IAC'
        
    
    elif 'ARTERIAL' in Totalscan:
        scantesting=1
        blackcounter=0
        if 'PHASE' in Totalscan:
            serieslabel='Arterial Phase'
        elif 'LATE' in Totalscan:
            serieslabel='Late Arterial'
        else:
            serieslabel='Arterial'
    
    elif 'VENOUS PHASE' in Totalscan:
        scantesting=1
        blackcounter=0
        serieslabel='Venous Phase'
            
    elif '' in Totalscan:
        blackcounter=blackcounter+1
    else : 
        pass
    serieslabel=serieslabel.upper()
    return scantesting,blackcounter,serieslabel