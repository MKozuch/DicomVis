#!/usr/bin/env python

__author__ = 'MKozuch'

from PyQt4 import QtCore, QtGui
from DicomVis import DicomVis
from MainWindow_ui import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dicomVisWidget = DicomVis()
        self.ui.verticalLayout.insertWidget(0, self.dicomVisWidget)

        studypath = "C:\\DICOM_resources\\BRAINIX\\T1-3D-FFE-C - 801"
        self.dicomVisWidget.load_study_from_path(studypath)

    @QtCore.pyqtSlot()
    def on_loadStudyBtn_clicked(self):
        dicompath = str(QtGui.QFileDialog.getExistingDirectory(None, "Open Directory", "/home", QtGui.QFileDialog.ShowDirsOnly))
        try:
            self.dicomVisWidget.load_study_from_path(dicompath)
        except:
            infobox = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error", "Ups! Something went wrong")
            infobox.exec_()


    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        infobox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "About", "by: MKozuch")
        infobox.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exitCode = app.exec_()
    sys.exit(exitCode)


