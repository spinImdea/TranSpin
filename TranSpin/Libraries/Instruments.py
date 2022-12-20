# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:56:41 2022

@author: Transport
"""

from Libraries import Globals


def GetWvfFunction():
    return Globals.activeInst["Waveform Generator"].waveForm

def GetWvfAmplitude():
    return Globals.activeInst["Waveform Generator"].amplitude

def GetWvfFrequency():
    return Globals.activeInst["Waveform Generator"].freq

def GetWvfOffset():
    return Globals.activeInst["Waveform Generator"].dcOffset
            
            
def SetWvfFunction(func):
    Globals.activeInst["Waveform Generator"].waveForm = func
    
def SetWvfAmplitude(amp):
    
    try: 
        auxAmp = float(amp)
    except:
        pass
    
    if abs(auxAmp) <= 6:
        Globals.activeInst["Waveform Generator"].amplitude = auxAmp
        Globals.window.wvfAmpLineEdit.setText("{:.2f}".format(auxAmp))
    else:
        Globals.activeInst["Waveform Generator"].amplitude = 0.0
        Globals.window.wvfAmpLineEdit.setText("0.0")
        
def SetWvfFrequency(freq):
    try: 
        auxFreq = float(freq)
    except:
        pass
   
    Globals.activeInst["Waveform Generator"].freq = auxFreq
    Globals.window.wvfFreqLineEdit.setText("{:.2f}".format(auxFreq))
    
def SetWvfOffset(offset):
    try: 
        auxOffset = float(offset)
    except:
        pass
   
    Globals.activeInst["Waveform Generator"].dcOffset = auxOffset
    Globals.window.wvfOffsetLineEdit.setText("{:.2f}".format(auxOffset))
    
def WvfEnableOutput():
    Globals.activeInst["Waveform Generator"].waveform_start()
    return

def WvfDisableOutput():
    Globals.activeInst["Waveform Generator"].shutdown()
    return

def WvfSafeMode():
    SetWvfAmplitude(0.0)
    SetWvfOffset(0.0)
    Globals.activeInst["Waveform Generator"].shutdown()

def WvfDefaultMode():
    #Globals.activeInst["Waveform Generator"].waveForm = "SINE"
    SetWvfAmplitude(3.0)
    SetWvfFrequency(3.71)
    SetWvfOffset(0.0)
    Globals.activeInst["Waveform Generator"].shutdown()
    
def SetCurrSourPhaseMarker():
    Globals.activeInst["Current Source"].waveform_use_phasemarker = True
    Globals.activeInst["Current Source"].waveform_phasemarker_channel = 1
    
def SetCurrSourAmplitude(amp):
    try: 
        auxAmp = float(amp)
    except:
        pass
    
    if abs(auxAmp) <= 6:
        Globals.activeInst["Current Source"].source_current = auxAmp
        Globals.window.currSourAmpLineEdit.setText("{:.2f}".format(auxAmp))
    else:
        Globals.activeInst["Current Source"].source_current = 0.0
        Globals.window.currSourAmpLineEdit.setText("0.0")
        
def SetCurrSourFrequency(freq):
    try: 
        auxFreq = float(freq)
    except:
        pass
   
    Globals.activeInst["Current Source"].waveform_frequency = auxFreq
    Globals.window.currSourFreqLineEdit.setText("{:.2f}".format(auxFreq))
    
def SetCurrSourOffset(offset):
    try: 
        auxOffset = float(offset)
    except:
        pass
    
    if abs(auxOffset) <= 6e-3:
        Globals.activeInst["Current Source"].waveform_offset = auxOffset
        Globals.window.currSourOffsetLineEdit.setText("{:.2f}".format(auxOffset))
    else:
        Globals.activeInst["Current Source"].waveform_offset = 0.0
        Globals.window.currSourOffsetLineEdit.setText("0.0")

def SetCurrSourRange(currRange):
    try:
        auxCurrRange = float(currRange)
    except:
        pass
    
    Globals.activeInst["Current Source"].source_range = currRange

def CurrSourEnableOutput():
    Globals.activeInst["Current Source"].waveform_arm()
    Globals.activeInst["Current Source"].waveform_start()
    return

def CurrSourDisableOutput():
    Globals.activeInst["Current Source"].waveform_abort()
    Globals.activeInst["Current Source"].disable_source()
    return

def CurrSourSafeMode():
    SetCurrSourAmplitude(0.0)
    SetCurrSourFrequency(10000)
    SetCurrSourOffset(0.0)
    
def CurrSourDefaultMode():
    SetCurrSourRange(6e-3)
    SetCurrSourAmplitude(3.0e-3)
    SetCurrSourFrequency(13333)
    SetCurrSourOffset(0.0)
    CurrSourDisableOutput()
    