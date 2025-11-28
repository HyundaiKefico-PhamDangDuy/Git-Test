import pandas as pd 
import xml.etree.ElementTree as ET

scu_target=['ScuFf01','SCUFF01','SCU','Scu']
         ##############       Setup function (Udpate Specification file)      ################

class updateSpec():
    def __init__(self,path,target):
        self.path=path
        self.target=target
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()
        
    def Get_GrapOID(self):
        graphic_oids = []
        for elem in self.root.iter():
            if 'graphicOID' in elem.attrib:
                graphic_oids.append(int(elem.attrib['graphicOID']))  # Convert to int for numeric sort
        graphic_oids.sort() 
        print(graphic_oids)
        return graphic_oids

    def ReplaceName(self):   #replace element name by special key "(-)"
        simple_arr=[]
        replacement=r"(-)"
        for element in self.root.findall('.//SimpleElement') + self.root.findall('.//ComplexElement'):
            name = element.get('elementName')
            simple_arr.append(name)
            for tar in self.target: 
                if tar in name:
                    name=name.replace(tar,replacement)
            element.set('elementName', name)
        print(simple_arr)
        self.tree.write(self.path, encoding="utf-8", xml_declaration=True)
    
    def EraseName(self):
        for element in self.root.findall('.//SimpleElement') + self.root.findall('.//ComplexElement'):
            elemID=element.get('elementOID')
            elemID=''
            element.set('elementOID', elemID)
        self.tree.write(self.path, encoding="utf-8", xml_declaration=True)
        print('finish')
        
        
            
            ################     For new module     ############## 
class AmdSpec():
    def __init__(self,path,target):
        self.path=path
        self.target=target
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()
        
    def getName(self):
        elemSpec=[]
        for data_entry in self.root.findall('.//Element') + self.root.findall('.//Local'):
            name = data_entry.get('name')
            elemSpec.append(name)
        print(elemSpec)
        
        # replace by special key "(-)"
        name_replace=[]
        replacement=r"(-)"
        
        for nam in elemSpec: 
            for tar in self.target: 
                if tar in nam: 
                    nam=nam.replace(tar,replacement)
            name_replace.append(nam)
        print(name_replace)
        return elemSpec,name_replace

    def WriteSpec(self, template_path):
        originName,modifiName=self.getName(self,self.target)
        
        #------- parse through xml file -------
        
        for element in self.root.findall('.//SimpleElement') + self.root.findall('.//ComplexElement'):
            name = element.get('elementName')
            for id,newnam in enumerate(modifiName): 
                if newnam == name:
                    name = originName[id] #update name
            element.set('elementName', name)
        self.tree.write(template_path, encoding="utf-8", xml_declaration=True)

    