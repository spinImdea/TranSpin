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
    if float(amp) <= 6:
        Globals.activeInst["Waveform Generator"].amplitude = float(amp)
        Globals.window.wvfAmpLineEdit.setText("{:.2f}".format(amp))
    else:
        Globals.activeInst["Waveform Generator"].amplitude = 0.0
        Globals.window.wvfAmpLineEdit.setText("0.0")
        
def SetWvfFrequency(freq):
    Globals.activeInst["Waveform Generator"].freq = float(freq)
    Globals.window.wvfFreqLineEdit.setText("{:.2f}".format(freq))
    
def SetWvfOffset(offset):
    Globals.activeInst["Waveform Generator"].dcOffset = float(offset)
    Globals.window.wvfOffsetLineEdit.setText("{:.2f}".format(offset))
    
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
    