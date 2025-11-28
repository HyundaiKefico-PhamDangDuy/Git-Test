import pandas as pd 
import xml.etree.ElementTree as ET
path_data = r"C:\Users\42024013\DUY_13\03.KGP\01.CAN\RPA\Ascet\amd\update\test_one_hierachy\CanFDSCUD_1\CanFDSCUD_2.data.amd"
path_spec = r"C:\Users\42024013\DUY_13\03.KGP\01.CAN\RPA\Ascet\amd\update\test_one_hierachy\CanFDSCUD_v3\replace\CanFDSCUD_1.specification.amd"

scu_target=['ScuFf01','SCUFF01','SCU','Scu']

def replace_data_xml(path, target):
    #------- parse through xml file -------
    tree = ET.parse(path)  
    root = tree.getroot()
    name_arr=[]
    replacement=r"(-)"
    
    #------ Check all "DataEntry" tag and their child ---------
    for data_entry in root.findall('.//DataEntry'):
        name = data_entry.get('elementName')
        name_arr.append(name)
        for tar in target: 
            if tar in name:
                name=name.replace(tar,replacement)
        data_entry.set('elementName', name)
    print(name_arr)
    tree.write(path, encoding="utf-8", xml_declaration=True)




def replace_spec_xml(path, target):
    #------- parse through xml file -------
    tree = ET.parse(path)  
    root = tree.getroot()
    complex_arr=[]
    simple_arr=[]
    replacement=r"(-)"
    
    #------ Check all "DataEntry" tag and their child ---------
    for element in root.findall('.//SimpleElement') + root.findall('.//ComplexElement'):
        name = element.get('elementName')
        simple_arr.append(name)
        for tar in target: 
            if tar in name:
                name=name.replace(tar,replacement)
        element.set('elementName', name)
    print(simple_arr)
    tree.write(path, encoding="utf-8", xml_declaration=True)
    
    return simple_arr

# replace_data_xml(path_data,scu_target)    
replace_spec_xml(path_spec,scu_target)   



