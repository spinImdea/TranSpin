# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:00:34 2022

@author: Transport
"""


import pandas as pd
import sys
from io import StringIO

from pyvisa.errors import VisaIOError
from pymeasure.instruments import list_resources 
from pymeasure.adapters import VISAAdapter

class Experiment:
    
    
    def GetInstruments(self):
        print("Reading the connected instruments...")
        old_std = sys.stdout
        result = StringIO()
        sys.stdout = result
        list_resources()
        listRes = result.getvalue()
        sys.stdout = old_std
        
        resData = {'Resource ID':[],'Port':[],'Name':[]}
        for auxIter in listRes.splitlines():
            """
            Get name from the *IDN? SCIP command
            """
            auxPort = auxIter.split(' : ')[1].replace('::INSTR','')
            auxVa = VISAAdapter(auxPort)
            try:
                auxName = auxVa.ask("*IDN?")
            except VisaIOError:
                auxName = "Unknown"
            resData['Resource ID'].append(auxIter.split(' : ')[0])
            resData['Port'].append(auxPort)
            #resData['Name'].append(",".join(auxName))
            resData['Name'].append(",".join(auxName.strip().split(',')[0:2]))
        self.Instruments = pd.DataFrame().from_dict(resData)
        print("Done")
        
    def __init__(self):
        self.expId = 0
        self.GetInstruments()