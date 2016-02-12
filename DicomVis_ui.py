# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DicomVis.ui'
#
# Created: Mon Jan 25 16:29:32 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(647, 480)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, -1, -1, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.XYPlaneWidget = QVTKRenderWindowInteractor(Form)
        self.XYPlaneWidget.setObjectName(_fromUtf8("XYPlaneWidget"))
        self.verticalLayout.addWidget(self.XYPlaneWidget)
        self.XYSlider = QtGui.QSlider(Form)
        self.XYSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XYSlider.setObjectName(_fromUtf8("XYSlider"))
        self.verticalLayout.addWidget(self.XYSlider)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.YZPlaneWidget = QVTKRenderWindowInteractor(Form)
        self.YZPlaneWidget.setObjectName(_fromUtf8("YZPlaneWidget"))
        self.verticalLayout_2.addWidget(self.YZPlaneWidget)
        self.YZSlider = QtGui.QSlider(Form)
        self.YZSlider.setOrientation(QtCore.Qt.Horizontal)
        self.YZSlider.setObjectName(_fromUtf8("YZSlider"))
        self.verticalLayout_2.addWidget(self.YZSlider)
        self.verticalLayout_2.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.XZPlaneWidget = QVTKRenderWindowInteractor(Form)
        self.XZPlaneWidget.setObjectName(_fromUtf8("XZPlaneWidget"))
        self.verticalLayout_3.addWidget(self.XZPlaneWidget)
        self.XZSlider = QtGui.QSlider(Form)
        self.XZSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XZSlider.setObjectName(_fromUtf8("XZSlider"))
        self.verticalLayout_3.addWidget(self.XZSlider)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.VolumeWidget = QVTKRenderWindowInteractor(Form)
        self.VolumeWidget.setObjectName(_fromUtf8("VolumeWidget"))
        self.verticalLayout_5.addWidget(self.VolumeWidget)
        self.verticalLayout_5.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.WindowWidthLabel = QtGui.QLabel(Form)
        self.WindowWidthLabel.setObjectName(_fromUtf8("WindowWidthLabel"))
        self.gridLayout.addWidget(self.WindowWidthLabel, 2, 0, 1, 1)
        self.WindowWidthSlider = QtGui.QSlider(Form)
        self.WindowWidthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.WindowWidthSlider.setObjectName(_fromUtf8("WindowWidthSlider"))
        self.gridLayout.addWidget(self.WindowWidthSlider, 2, 1, 1, 1)
        self.WindowControlLabel = QtGui.QLabel(Form)
        self.WindowControlLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.WindowControlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WindowControlLabel.setObjectName(_fromUtf8("WindowControlLabel"))
        self.gridLayout.addWidget(self.WindowControlLabel, 0, 0, 1, 1)
        self.WindowCenterLabel = QtGui.QLabel(Form)
        self.WindowCenterLabel.setObjectName(_fromUtf8("WindowCenterLabel"))
        self.gridLayout.addWidget(self.WindowCenterLabel, 1, 0, 1, 1)
        self.WindowCenterSlider = QtGui.QSlider(Form)
        self.WindowCenterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.WindowCenterSlider.setObjectName(_fromUtf8("WindowCenterSlider"))
        self.gridLayout.addWidget(self.WindowCenterSlider, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "DICOM Visualizer", None))
        self.label.setText(_translate("Form", "XY slice", None))
        self.label_3.setText(_translate("Form", "YZ slice", None))
        self.label_2.setText(_translate("Form", "XZ slice", None))
        self.label_4.setText(_translate("Form", "Volume ", None))
        self.WindowWidthLabel.setText(_translate("Form", "Window width", None))
        self.WindowControlLabel.setText(_translate("Form", "Window control", None))
        self.WindowCenterLabel.setText(_translate("Form", "Window center", None))

from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
