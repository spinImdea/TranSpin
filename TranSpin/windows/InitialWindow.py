# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1557, 1049)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setActiveInstrumentsButton = QtWidgets.QPushButton(self.centralwidget)
        self.setActiveInstrumentsButton.setGeometry(QtCore.QRect(190, 620, 231, 24))
        self.setActiveInstrumentsButton.setObjectName("setActiveInstrumentsButton")
        self.instGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.instGroupBox.setGeometry(QtCore.QRect(10, 200, 421, 451))
        self.instGroupBox.setObjectName("instGroupBox")
        self.instrumentUpdateButton = QtWidgets.QPushButton(self.instGroupBox)
        self.instrumentUpdateButton.setGeometry(QtCore.QRect(10, 420, 161, 24))
        self.instrumentUpdateButton.setObjectName("instrumentUpdateButton")
        self.instrumentTableWidget = QtWidgets.QTableWidget(self.instGroupBox)
        self.instrumentTableWidget.setGeometry(QtCore.QRect(10, 30, 401, 381))
        self.instrumentTableWidget.setShowGrid(True)
        self.instrumentTableWidget.setColumnCount(0)
        self.instrumentTableWidget.setObjectName("instrumentTableWidget")
        self.instrumentTableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(441, 161, 1091, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.wfmGenGroupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.wfmGenGroupBox.setEnabled(False)
        self.wfmGenGroupBox.setObjectName("wfmGenGroupBox")
        self.waveFormGenLabel = QtWidgets.QLabel(self.wfmGenGroupBox)
        self.waveFormGenLabel.setGeometry(QtCore.QRect(10, 20, 271, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveFormGenLabel.sizePolicy().hasHeightForWidth())
        self.waveFormGenLabel.setSizePolicy(sizePolicy)
        self.waveFormGenLabel.setObjectName("waveFormGenLabel")
        self.wvfOutPushButton = QtWidgets.QPushButton(self.wfmGenGroupBox)
        self.wvfOutPushButton.setGeometry(QtCore.QRect(380, 230, 143, 24))
        self.wvfOutPushButton.setAutoFillBackground(False)
        self.wvfOutPushButton.setStyleSheet("bacground: rgb(255, 0, 4);\n"
"font: 700 9pt \"Segoe UI\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/buttonOFF.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("Icons/buttonOn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.wvfOutPushButton.setIcon(icon)
        self.wvfOutPushButton.setCheckable(True)
        self.wvfOutPushButton.setObjectName("wvfOutPushButton")
        self.layoutWidget1 = QtWidgets.QWidget(self.wfmGenGroupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(180, 110, 336, 108))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wvfFuncLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.wvfFuncLabel.setObjectName("wvfFuncLabel")
        self.gridLayout_2.addWidget(self.wvfFuncLabel, 0, 0, 1, 1)
        self.wvfFuncReadLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfFuncReadLineEdit.setEnabled(False)
        self.wvfFuncReadLineEdit.setObjectName("wvfFuncReadLineEdit")
        self.gridLayout_2.addWidget(self.wvfFuncReadLineEdit, 0, 1, 1, 1)
        self.wvfFuncComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.wvfFuncComboBox.setEditable(False)
        self.wvfFuncComboBox.setObjectName("wvfFuncComboBox")
        self.wvfFuncComboBox.addItem("")
        self.wvfFuncComboBox.addItem("")
        self.wvfFuncComboBox.addItem("")
        self.gridLayout_2.addWidget(self.wvfFuncComboBox, 0, 2, 1, 1)
        self.wvfAmpLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.wvfAmpLabel.setObjectName("wvfAmpLabel")
        self.gridLayout_2.addWidget(self.wvfAmpLabel, 1, 0, 1, 1)
        self.wvfFreqReadLineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfFreqReadLineEdit_2.setEnabled(False)
        self.wvfFreqReadLineEdit_2.setObjectName("wvfFreqReadLineEdit_2")
        self.gridLayout_2.addWidget(self.wvfFreqReadLineEdit_2, 1, 1, 1, 1)
        self.wvfAmpLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfAmpLineEdit.setObjectName("wvfAmpLineEdit")
        self.gridLayout_2.addWidget(self.wvfAmpLineEdit, 1, 2, 1, 1)
        self.wvfFreqLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.wvfFreqLabel.setObjectName("wvfFreqLabel")
        self.gridLayout_2.addWidget(self.wvfFreqLabel, 2, 0, 1, 1)
        self.wvfOffsetReadLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfOffsetReadLineEdit.setEnabled(False)
        self.wvfOffsetReadLineEdit.setObjectName("wvfOffsetReadLineEdit")
        self.gridLayout_2.addWidget(self.wvfOffsetReadLineEdit, 2, 1, 1, 1)
        self.wvfFreqLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfFreqLineEdit.setObjectName("wvfFreqLineEdit")
        self.gridLayout_2.addWidget(self.wvfFreqLineEdit, 2, 2, 1, 1)
        self.wvfOffsetLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.wvfOffsetLabel.setObjectName("wvfOffsetLabel")
        self.gridLayout_2.addWidget(self.wvfOffsetLabel, 3, 0, 1, 1)
        self.wvfAmpReadLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfAmpReadLineEdit.setEnabled(False)
        self.wvfAmpReadLineEdit.setObjectName("wvfAmpReadLineEdit")
        self.gridLayout_2.addWidget(self.wvfAmpReadLineEdit, 3, 1, 1, 1)
        self.wvfOffsetLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.wvfOffsetLineEdit.setObjectName("wvfOffsetLineEdit")
        self.gridLayout_2.addWidget(self.wvfOffsetLineEdit, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.wfmGenGroupBox, 0, 0, 1, 1)
        self.oscillGroupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.oscillGroupBox.setObjectName("oscillGroupBox")
        self.oscillLabel = QtWidgets.QLabel(self.oscillGroupBox)
        self.oscillLabel.setGeometry(QtCore.QRect(10, 20, 271, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oscillLabel.sizePolicy().hasHeightForWidth())
        self.oscillLabel.setSizePolicy(sizePolicy)
        self.oscillLabel.setObjectName("oscillLabel")
        self.gridLayout.addWidget(self.oscillGroupBox, 1, 1, 1, 1)
        self.lockInGroupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.lockInGroupBox.setObjectName("lockInGroupBox")
        self.lockInLabel = QtWidgets.QLabel(self.lockInGroupBox)
        self.lockInLabel.setGeometry(QtCore.QRect(10, 20, 271, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lockInLabel.sizePolicy().hasHeightForWidth())
        self.lockInLabel.setSizePolicy(sizePolicy)
        self.lockInLabel.setObjectName("lockInLabel")
        self.gridLayout.addWidget(self.lockInGroupBox, 1, 0, 1, 1)
        self.currSourGroupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.currSourGroupBox.setEnabled(False)
        self.currSourGroupBox.setObjectName("currSourGroupBox")
        self.currSourLabel = QtWidgets.QLabel(self.currSourGroupBox)
        self.currSourLabel.setGeometry(QtCore.QRect(10, 20, 271, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currSourLabel.sizePolicy().hasHeightForWidth())
        self.currSourLabel.setSizePolicy(sizePolicy)
        self.currSourLabel.setObjectName("currSourLabel")
        self.wvfOutPushButton_2 = QtWidgets.QPushButton(self.currSourGroupBox)
        self.wvfOutPushButton_2.setGeometry(QtCore.QRect(360, 140, 143, 24))
        self.wvfOutPushButton_2.setAutoFillBackground(False)
        self.wvfOutPushButton_2.setStyleSheet("bacground: rgb(255, 0, 4);\n"
"font: 700 9pt \"Segoe UI\";")
        self.wvfOutPushButton_2.setIcon(icon)
        self.wvfOutPushButton_2.setCheckable(True)
        self.wvfOutPushButton_2.setObjectName("wvfOutPushButton_2")
        self.widget = QtWidgets.QWidget(self.currSourGroupBox)
        self.widget.setGeometry(QtCore.QRect(150, 140, 197, 80))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.currSourAmpLineEdit = QtWidgets.QLineEdit(self.widget)
        self.currSourAmpLineEdit.setObjectName("currSourAmpLineEdit")
        self.gridLayout_3.addWidget(self.currSourAmpLineEdit, 0, 1, 1, 1)
        self.currSourFreqLineEdit = QtWidgets.QLineEdit(self.widget)
        self.currSourFreqLineEdit.setObjectName("currSourFreqLineEdit")
        self.gridLayout_3.addWidget(self.currSourFreqLineEdit, 1, 1, 1, 1)
        self.currSourFreqLabel = QtWidgets.QLabel(self.widget)
        self.currSourFreqLabel.setObjectName("currSourFreqLabel")
        self.gridLayout_3.addWidget(self.currSourFreqLabel, 1, 0, 1, 1)
        self.currSourAmpLabel = QtWidgets.QLabel(self.widget)
        self.currSourAmpLabel.setObjectName("currSourAmpLabel")
        self.gridLayout_3.addWidget(self.currSourAmpLabel, 0, 0, 1, 1)
        self.currSourOffsetLabel = QtWidgets.QLabel(self.widget)
        self.currSourOffsetLabel.setObjectName("currSourOffsetLabel")
        self.gridLayout_3.addWidget(self.currSourOffsetLabel, 2, 0, 1, 1)
        self.currSourOffsetLineEdit = QtWidgets.QLineEdit(self.widget)
        self.currSourOffsetLineEdit.setObjectName("currSourOffsetLineEdit")
        self.gridLayout_3.addWidget(self.currSourOffsetLineEdit, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.currSourGroupBox, 0, 1, 1, 1)
        self.layoutWidget.raise_()
        self.instGroupBox.raise_()
        self.setActiveInstrumentsButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1557, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setActiveInstrumentsButton.setText(_translate("MainWindow", "Set Active instruments"))
        self.instGroupBox.setTitle(_translate("MainWindow", "Instrumentation"))
        self.instrumentUpdateButton.setText(_translate("MainWindow", "Update Intruments"))
        self.wfmGenGroupBox.setTitle(_translate("MainWindow", "Waveform Generator"))
        self.waveFormGenLabel.setText(_translate("MainWindow", "..."))
        self.wvfOutPushButton.setText(_translate("MainWindow", "Output OFF"))
        self.wvfFuncLabel.setText(_translate("MainWindow", "Function"))
        self.wvfFuncComboBox.setItemText(0, _translate("MainWindow", "SINE"))
        self.wvfFuncComboBox.setItemText(1, _translate("MainWindow", "SQUARE"))
        self.wvfFuncComboBox.setItemText(2, _translate("MainWindow", "COS"))
        self.wvfAmpLabel.setText(_translate("MainWindow", "Amplitude"))
        self.wvfFreqLabel.setText(_translate("MainWindow", "Frequency"))
        self.wvfOffsetLabel.setText(_translate("MainWindow", "Offset"))
        self.oscillGroupBox.setTitle(_translate("MainWindow", "Oscilloscope"))
        self.oscillLabel.setText(_translate("MainWindow", "..."))
        self.lockInGroupBox.setTitle(_translate("MainWindow", "Lock In"))
        self.lockInLabel.setText(_translate("MainWindow", "..."))
        self.currSourGroupBox.setTitle(_translate("MainWindow", "Current Source"))
        self.currSourLabel.setText(_translate("MainWindow", "..."))
        self.wvfOutPushButton_2.setText(_translate("MainWindow", "Output OFF"))
        self.currSourFreqLabel.setText(_translate("MainWindow", "Frequency"))
        self.currSourAmpLabel.setText(_translate("MainWindow", "Amplitude"))
        self.currSourOffsetLabel.setText(_translate("MainWindow", "Offset"))
