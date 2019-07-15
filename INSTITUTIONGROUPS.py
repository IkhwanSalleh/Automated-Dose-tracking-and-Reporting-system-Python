import pandas
def InstitutionNameLocation(Institutions):
    Rawdata=pandas.read_excel('STUDY LIBRARY.xlsx','Sheet2')
    InstitutionList=list(Rawdata['InstitutionName'])
    if Institutions in InstitutionList:
        InstitutionGroup = 'INSIDE PPUM'
    elif Institutions is 'UNSPECIFIED':
        InstitutionGroup='UNKNOWN'
    
    else:
        InstitutionGroup='OUTSIDE PPUM'
        
    return InstitutionGroup