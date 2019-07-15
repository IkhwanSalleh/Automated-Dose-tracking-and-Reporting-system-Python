# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 00:21:04 2018

@author: Ikhwan Salleh
This program is to do the OCR of the image from the dicom. This program
utilised the features of multithredding instead or normal/default sequentional
programm running at 1 thread with 1 core.(DICOMTOIMAGES)
1) The dcm files is read usig the funtion DICOMTOIMAGE into a png files.
2)Applying post processing to the images from dicom files into binary 1 or 0
black or white images.(THRESHOLDINGFUCNTION,process_image)
3)After the images have been read from the dcm file we read their metadata 
containing in the folder.
"""

#Muhammad Ikhwan Bin Salleh
#This is the main programm 

import queue
import pydicom
import numpy
import pydicom as dicom
import tkinter as tk
from tkinter import filedialog
import pandas
import regex as re
import os
import threading
import Sheet_Selection as Lib3
import PROCESS1
import PROCESS2
import PROCESS3
import PROCESS4

import STATISTICALSTUDYMEANANALYSIS


def ChooseDCMFiles():
    root = tk.Tk()
    root.withdraw()
    print("ok")
    filelist=list(numpy.empty(10000000))
    file_path = filedialog.askdirectory()
    dirs = os.listdir(file_path)
    j=0
    for file in dirs:
        filelist[j]=os.path.join('C:/Users/60111/Desktop/Python project/dcmimages',file)
        j=j+1
    filelist=filelist[:j]
    return filelist

def dataanalysis(workbook):
    Rawdata=pandas.read_csv(workbook)
    Rawdata=Rawdata.fillna(value=0)
    studydescriptionList=Rawdata['StudyDescription']
    try:
        STUDYLEVEL=STATISTICALSTUDYMEANANALYSIS.statisticalStudyMeananalysis(studydescriptionList)
    except:
        pass
    return STUDYLEVEL
#This section is converting dicom files to jpg files 
def MasterProcess():
    pathlist=ChooseDCMFiles()
    datacounter=0
    counter=0
    print('Number of files found:{}'.format(len(pathlist)))
    while datacounter<=len(pathlist):
        if datacounter>=4:
            VerificationFiles=pandas.read_csv('DATAFOLEDER/DATA-BASE2.csv')
            AsseccionNumberVerified=VerificationFiles.fillna(value=0)
            AccessionNumberVerifiedList=AsseccionNumberVerified['PatientID']
        q1=queue.Queue()
        q2=queue.Queue()
        q3=queue.Queue()
        q4=queue.Queue()
        
        if datacounter==(len(pathlist)):
            Datamerging=0
            break
        while datacounter<=len(pathlist):
            try: 
               if not (pydicom.dcmread(pathlist[datacounter]).AccessionNumber).strip():
                   datacounter=datacounter+1
               else:
                   if counter==1:
                       if str(pydicom.dcmread(pathlist[datacounter]).AccessionNumber) in list(AccessionNumberVerifiedList):
                           datacounter=datacounter+1
                       else:
                           if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                                if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                                    if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                        t1=threading.Thread(target=PROCESS1.processingmaster1, args=(pathlist[datacounter],q1))
                                        print(pathlist[datacounter])
                                        
                                        
                                        break
                                    else:
                                         datacounter=datacounter+1
                                else:
                                    datacounter=datacounter+1   
                           else:
                                datacounter=datacounter+1
                   else:
                       
                       if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                           if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):                               
                               if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                   t1=threading.Thread(target=PROCESS1.processingmaster1, args=(pathlist[datacounter],q1))
                                   print(pathlist[datacounter])
                                        
                                        
                                   break
                               else:
                                   datacounter=datacounter+1
                           else:  
                                datacounter=datacounter+1   
                       else:
                             datacounter=datacounter+1
                   
               
                      
                       
            except:
                datacounter=datacounter+1
                    
        t1.start()
        datacounter=datacounter+1
        
        
        
        if datacounter==(len(pathlist)):
            Datamerging=1
            break
        while datacounter<=len(pathlist):
            try: 
               if not (pydicom.dcmread(pathlist[datacounter]).AccessionNumber).strip():
                   datacounter=datacounter+1
               else:
                   if counter==1:
                       if str(pydicom.dcmread(pathlist[datacounter]).AccessionNumber) in list(AccessionNumberVerifiedList):
                           datacounter=datacounter+1
                       else:
                           if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                                if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                                    if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                        t2=threading.Thread(target=PROCESS2.processingmaster2, args=(pathlist[datacounter],q2))
                                        print(pathlist[datacounter])
                                        
                                        
                                        break
                                    else:
                                         datacounter=datacounter+1
                                else:
                                    datacounter=datacounter+1   
                           else:
                                datacounter=datacounter+1
                   else:
                       
                       if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                           if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):                               
                               if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                   t2=threading.Thread(target=PROCESS2.processingmaster2, args=(pathlist[datacounter],q2))
                                   print(pathlist[datacounter])
                                        
                                        
                                   break
                               else:
                                   datacounter=datacounter+1
                           else:  
                                datacounter=datacounter+1   
                       else:
                             datacounter=datacounter+1
            except:
                datacounter=datacounter+1
        t2.start()
        datacounter=datacounter+1
        
        
        
        if datacounter==(len(pathlist)):
            Datamerging=2
            break
        while datacounter<=len(pathlist):
            try: 
               if not (pydicom.dcmread(pathlist[datacounter]).AccessionNumber).strip():
                   datacounter=datacounter+1
               else:
                   if counter==1:
                       if str(pydicom.dcmread(pathlist[datacounter]).AccessionNumber) in list(AccessionNumberVerifiedList):
                           datacounter=datacounter+1
                       else:
                           if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                                if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                                    if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                        t3=threading.Thread(target=PROCESS3.processingmaster3, args=(pathlist[datacounter],q3))
                                        print(pathlist[datacounter])
                                        
                                        
                                        break
                                    else:
                                         datacounter=datacounter+1
                                else:
                                    datacounter=datacounter+1   
                           else:
                                datacounter=datacounter+1
                   else:
                       
                       if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                           if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):                               
                               if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                   t3=threading.Thread(target=PROCESS3.processingmaster3, args=(pathlist[datacounter],q3))
                                   print(pathlist[datacounter])
                                        
                                        
                                   break
                               else:
                                   datacounter=datacounter+1
                           else:  
                                datacounter=datacounter+1   
                       else:
                             datacounter=datacounter+1
            except:
                datacounter=datacounter+1
        t3.start()
        datacounter=datacounter+1
        
        
        
        if datacounter==(len(pathlist)):
            Datamerging=3
            break
        while datacounter<=len(pathlist):
          try: 
               if not (pydicom.dcmread(pathlist[datacounter]).AccessionNumber).strip():
                   datacounter=datacounter+1
               else:
                   if counter==1:
                       if str(pydicom.dcmread(pathlist[datacounter]).AccessionNumber) in list(AccessionNumberVerifiedList):
                           datacounter=datacounter+1
                       else:
                           if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                                if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                                    if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                        t4=threading.Thread(target=PROCESS4.processingmaster4, args=(pathlist[datacounter],q4))
                                        print(pathlist[datacounter])
                                        
                                        
                                        break
                                    else:
                                         datacounter=datacounter+1
                                else:
                                    datacounter=datacounter+1   
                           else:
                                datacounter=datacounter+1
                   else:
                       
                       if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                           if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):                               
                               if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                                   t4=threading.Thread(target=PROCESS4.processingmaster4, args=(pathlist[datacounter],q4))
                                   print(pathlist[datacounter])
                                        
                                        
                                   break
                               else:
                                   datacounter=datacounter+1
                           else:  
                                datacounter=datacounter+1   
                       else:
                             datacounter=datacounter+1
          except:
                datacounter=datacounter+1
        t4.start()
        datacounter=datacounter+1
        
        """
        if datacounter==(len(pathlist)):
            Datamerging=4
            break
        while datacounter<=len(pathlist):
            try:
               
               if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                    if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                        if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                            t5=threading.Thread(target=processingmaster5, args=(pathlist[datacounter],q5))
                            print(pathlist[datacounter])
                            
                            
                            break
                        else:
                             datacounter=datacounter+1
                    else:
                        datacounter=datacounter+1   
               else:
                    datacounter=datacounter+1
            except:
                datacounter=datacounter+1
        t5.start()
        datacounter=datacounter+1
        
        
        if datacounter==(len(pathlist)):
            Datamerging=5
            break
        while datacounter<=len(pathlist):
            try:
               
               if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                    if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                        if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                            t6=threading.Thread(target=processingmaster6, args=(pathlist[datacounter],q6))
                            print(pathlist[datacounter])
                            
                            
                            break
                        else:
                             datacounter=datacounter+1
                    else:
                        datacounter=datacounter+1   
               else:
                    datacounter=datacounter+1
            except:
                datacounter=datacounter+1
        t6.start()
        datacounter=datacounter+1
        
        if datacounter==(len(pathlist)):
            Datamerging=6
            break
        while datacounter<=len(pathlist):
            try:
               
               if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                    if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                        if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                            t7=threading.Thread(target=processingmaster7, args=(pathlist[datacounter],q7))
                            print(pathlist[datacounter])
                            
                            
                            break
                        else:
                             datacounter=datacounter+1
                    else:
                        datacounter=datacounter+1   
               else:
                    datacounter=datacounter+1
            except:
                datacounter=datacounter+1
        t7.start()
        datacounter=datacounter+1
        
        
        
        if datacounter==(len(pathlist)):
            Datamerging=7
            break
        while datacounter<=len(pathlist):
            try:
                
                if (pydicom.dcmread(pathlist[datacounter]).Manufacturer=='SIEMENS'):
                    if (pydicom.dcmread(pathlist[datacounter]).SeriesDescription=='Patient Protocol'):
                        if dicom.read_file(pathlist[datacounter])[0x6000,0x0010].value==512:
                            t8=threading.Thread(target=processingmaster8, args=(pathlist[datacounter],q8))
                            print(pathlist[datacounter])
                            
                            
                            break
                        else:
                             datacounter=datacounter+1
                    else:
                        datacounter=datacounter+1   
                else:
                    datacounter=datacounter+1
            except:
                datacounter=datacounter+1
        t8.start()
        datacounter=datacounter+1
        
        """
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        """
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        """
        
        result1=q1.get()
        result2=q2.get()
        result3=q3.get()
        result4=q4.get()
        """
        result5=q5.get()
        result6=q6.get()
        result7=q7.get()
        result8=q8.get()
    
        """
        
        
        conditionnotmet=0
        while conditionnotmet<=1:
            
            try:
                if counter==0:
                    Compilleddata= pandas.concat([result1,result2,result3,result4])
                    Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',Compilleddata,sheet_name='CT DATABASE',startcol=0)
                    Compilleddata.to_csv('DATAFOLEDER/DATA-BASE2.csv', mode='a+')
                    counter=1
                else:
                    Compilleddata= pandas.concat([result1,result2,result3,result4])
                    Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',Compilleddata,sheet_name='CT DATABASE',startcol=0,header=None)
                    Compilleddata.to_csv('DATAFOLEDER/DATA-BASE2.csv', mode='a+',header=False)
        
                print(Compilleddata)
                print('Processed:{}'.format(datacounter))
                print('Left:{}'.format(len(pathlist)-datacounter))
                break
            except:
                pass
        
        
    if Datamerging==1:
        Compilleddata=result1
        print(Compilleddata)
        Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',Compilleddata,sheet_name='CT DATABASE',startcol=0,header=None)
        Compilleddata.to_csv('DATAFOLEDER/DATA-BASE2.csv', mode='a+',header=False)
    elif Datamerging==2:
        Compilleddata= pandas.concat([result1,result2])
        print(Compilleddata)
        Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',Compilleddata,sheet_name='CT DATABASE',startcol=0,header=None)
        Compilleddata.to_csv('DATAFOLEDER/DATA-BASE2.csv', mode='a+',header=False)
    elif Datamerging==3:
        Compilleddata= pandas.concat([result1,result2,result3])
        Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',Compilleddata,sheet_name='CT DATABASE',startcol=0,header=None)
        Compilleddata.to_csv('DATAFOLEDER/DATA-BASE2.csv', mode='a+',header=False)
    elif Datamerging==4:
        Compilleddata= pandas.concat([result1,result2,result3,result4])
        Lib3.append_df_to_excel('DATAFOLEDER/DATA-BASE1.xlsx',Compilleddata,sheet_name='CT DATABASE',startcol=0,header=None)
        Compilleddata.to_csv('DATAFOLEDER/DATA-BASE2.csv', mode='a+',header=False)
    else:
        pass
        
    dataanalysis('DATAFOLEDER/DATA-BASE2.csv')
run = MasterProcess()  