import pandas as pd 
import xml.etree.ElementTree as ET
path_1 = r"C:\Users\42024013\DUY_13\03.KGP\01.CAN\RPA\Ascet\amd\update\test_one_hierachy\CanFDSCUD_1\CanFDSCUD_2.data.amd"
path_2 = r"C:\Users\42024013\DUY_13\03.KGP\01.CAN\RPA\Ascet\amd\update\test_one_hierachy\CanFDTCUD_test.data.amd"

def get_element_data(path):
    #------- parse through xml file -------
    tree = ET.parse(path)  
    root = tree.getroot()
    name_arr=[]
    
    #------ Check all "DataEntry" tag and their child ---------
    for data_entry in root.findall('.//DataEntry'):
        name = data_entry.get('elementName')
        name_arr.append(name)
    print(name_arr)
    return name_arr

def replace_string(target,path):
    arr=get_element_data(path)
    replacement=r"(-)"
    
    new_arr = []
    
    for item in arr: 
        for tar in target: 
            if tar in item: 
                item=item.replace(tar,replacement)
        new_arr.append(item)   
    # print(new_arr)    
    return new_arr

# replace_string(['ScuFf01','SCUFF01','SCU','Scu'],path_1)

# replace_string(['TCU01','Tcu01','Tcu','TCU'],path_2)

