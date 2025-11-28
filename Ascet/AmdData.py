import pandas as pd 
import xml.etree.ElementTree as ET
path = r"C:\Users\42024013\DUY_13\03.KGP\01.CAN\RPA\Ascet\amd\update\test_one_hierachy\CanFDSCUD_1\CanFDSCUD_2.data.amd"

def get_element_data(path):
    #------- parse through xml file -------
    tree = ET.parse(path)  
    root = tree.getroot()
    scalar = []
    complex = []
    
    #------ Check all "DataEntry" tag and their child ---------
    for data_entry in root.findall('.//DataEntry'):
        name = data_entry.get('elementName')
        oid = data_entry.get('elementOID') 
        type_tag=(list(data_entry)[0])[0].tag
        
        if type_tag == "ScalarType":
            # print(f"scalar {name}")
            child = ((list(data_entry)[0])[0])[0]
            value = child.get('value')
            type = child.tag 
            scalar.append(
            {
                "Name": name,
                "Element OID":oid,
                "Type": type, 
                "Value": value
            })
        
        elif type_tag == "ComplexType":
            element=(list(data_entry)[0])[0]
            dataname=element.get('dataName')
            dataOID=element.get('dataOID')
            complex.append(
            {
                "Name": name,
                "Element OID":oid,
                "dataName": dataname, 
                "dataOID": dataOID
            })
    scalar=pd.DataFrame(scalar)    
    complex=pd.DataFrame(complex)
    scalar=scalar.to_excel('scalar.xlsx', sheet_name='Data', index=False)
    complex=complex.to_excel('complex.xlsx', sheet_name='Data', index=False)
    return scalar,complex

get_element_data(path)

