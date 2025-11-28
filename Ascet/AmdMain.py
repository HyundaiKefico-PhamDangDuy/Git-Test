import pandas as pd
import xml.etree.ElementTree as ET
Main_path=r"C:\Users\42024013\DUY_13\03.KGP\01.CAN\RPA\Ascet\amd\Sample_finish_v1\CanFDSCUD_1.main.amd"
scu_target=['ScuFf01','SCUFF01','SCU','Scu']

class AmdMain:
    def __init__(self,path,target):
        self.path=path
        self.target=target
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()
    
    def getName(self):
        elemMain=[]
        for elem in self.root.findall('.//Element'):
            name=elem.get('name')
            eid=elem.get('OID')
            elemMain.append(
                {
                    "Name": name, 
                    "ElementID":eid
                }
            )
        elemMain=pd.DataFrame(elemMain)
        print(elemMain)

elem=AmdMain(Main_path,scu_target)
elem.getName()
