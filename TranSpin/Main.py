# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:29:21 2022

@author: Transport
"""

import sys
from PyQt6 import QtCore, QtWidgets, uic
import pandas as pd
import numpy as np

from windows.InitialWindow import Ui_MainWindow

from Libraries import Experiment
from Libraries import Globals
from Libraries import Instruments

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def HandleWvfOutPushButton(self):
        auxText = self.wvfOutPushButton.text()
        auxChkState = self.wvfOutPushButton.isChecked()
        if auxChkState == True:
            self.wvfOutPushButton.setText("Output OFF")
            self.wvfOutPushButton.setChecked(False)
            Instruments.WvfDisableOutput()
        else:
            self.wvfOutPushButton.setText("Output ON")
            self.wvfOutPushButton.setChecked(True)
            Instruments.WvfEnableOutput()
        
        del auxText
        del auxChkState
        
    
    def SetupInstruments(self):
        print("\nSetting up the active instruments...")
        auxDict = {}
        for auxIter in range(self.instrumentTableWidget.rowCount()):
            auxName = self.instrumentTableWidget.item(auxIter,2).text()
            match auxName:
                case "KEITHLEY INSTRUMENTS INC.,MODEL 6221":
                    from Instrumentation.keithley.keithley6221_mod import Keithley6221
                    Globals.activeInst[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = Keithley6221(self.instrumentTableWidget.item(auxIter,1).text())
                    auxDict[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = auxName
                case "THURLBY THANDAR,TGA1241":
                    from Instrumentation.thurlbythandar.tga1241_mod import TTiTGA1241
                    Globals.activeInst[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = TTiTGA1241(self.instrumentTableWidget.item(auxIter,1).text())
                    auxDict[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = auxName
                case "Stanford_Research_Systems,SR830":
                    from Instrumentation.srs.sr830_mod import SR830
                    Globals.activeInst[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = SR830(self.instrumentTableWidget.item(auxIter,1).text())
                    auxDict[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = auxName
                case "TEKTRONIX,DPO3034":
                    from Instrumentation.tektronix.dpo3034_mod import DPO3034
                    Globals.activeInst[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = DPO3034(self.instrumentTableWidget.item(auxIter,1).text()) 
                    auxDict[self.instrumentTableWidget.cellWidget(auxIter,3).currentText()] = auxName
                case _:
                    print ('\tPort: ',self.instrumentTableWidget.item(auxIter,1).text(),'; Unknown instrument. Ask developers so it can be introduced')
        
        self.waveFormGenLabel.setText(auxDict["Waveform Generator"])
        self.waveFormGenLabel.setStyleSheet("background: green")
        self.waveFormGenLabel.setWordWrap(True)
        self.wfmGenGroupBox.setEnabled(True)
        Instruments.WvfDefaultMode()
        self.lockInLabel.setText(auxDict["Lock In"])
        self.lockInLabel.setStyleSheet("background: green")
        self.lockInLabel.setWordWrap(True)
        self.lockInGroupBox.setEnabled(True)
        self.oscillLabel.setText(auxDict["Oscilloscope"])
        self.oscillLabel.setStyleSheet("background: green")
        self.oscillLabel.setWordWrap(True)
        self.oscillGroupBox.setEnabled(True)
        self.currSourLabel.setText(auxDict["Current Source"])
        self.currSourLabel.setStyleSheet("background: green")
        self.currSourLabel.setWordWrap(True)
        self.oscillGroupBox.setEnabled(True)
        
        
        del auxIter
        del auxName
        del auxDict
    
    def UpdateInstrumentsTable(self):
        self.instrumentTableWidget.clear()
        self.instrumentTableWidget.setColumnCount(Globals.activeExp.Instruments.shape[1]+1)
        self.instrumentTableWidget.setRowCount(Globals.activeExp.Instruments.shape[0])
        self.instrumentTableWidget.setHorizontalHeaderLabels(np.append(np.asarray(Globals.activeExp.Instruments.keys()),"Role"))
        Globals.activeExp.Instruments.reset_index(drop=True)
        for auxIter in range(len(Globals.activeExp.Instruments.keys())):
            for index,row in Globals.activeExp.Instruments.iterrows():
                auxItem = QtWidgets.QTableWidgetItem(row[Globals.activeExp.Instruments.keys()[auxIter]])
                self.instrumentTableWidget.setItem(index, auxIter, auxItem)
                auxComboBox = QtWidgets.QComboBox()
                auxComboBox.addItems(["--- (None) ---","Waveform Generator","Current Source","Lock In","Oscilloscope"])
                self.instrumentTableWidget.setCellWidget(index, Globals.activeExp.Instruments.shape[1], auxComboBox)
        self.instrumentTableWidget.resizeColumnsToContents()
        self.instrumentTableWidget.setColumnHidden(0, True)
        self.instrumentTableWidget.setColumnHidden(1, True)
        
        del index
        del row
        del auxIter
        del auxItem
        del auxComboBox
    
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.showMaximized()
        self.UpdateInstrumentsTable()
        self.setActiveInstrumentsButton.clicked.connect(self.SetupInstruments)
        self.instrumentUpdateButton.clicked.connect(self.UpdateInstrumentsTable)
        self.wvfAmpLineEdit.textChanged.connect(Instruments.SetWvfAmplitude)
        self.wvfFreqLineEdit.textChanged.connect(Instruments.SetWvfFrequency)
        self.wvfOffsetLineEdit.textChanged.connect(Instruments.SetWvfOffset)
        self.wvfOutPushButton.clicked.connect(self.HandleWvfOutPushButton)
        
        
app = QtWidgets.QApplication(sys.argv)

Globals.activeInst = {}
Globals.activeExp = Experiment.Experiment()
Globals.window = MainWindow()

Globals.window.show()

#window.UpdateInstrumentsTable()

app.exec()
