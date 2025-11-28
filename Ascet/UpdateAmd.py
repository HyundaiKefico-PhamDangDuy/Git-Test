import pandas as pd 
import xml.etree.ElementTree as ET

from AmdConfig import *
from AmdMain import AmdMain
from AmdSpec import updateSpec,AmdSpec



uSpec=updateSpec(implpath,scu_target)
uSpec.EraseName()
uSpec.ReplaceName()


