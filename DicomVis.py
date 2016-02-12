# TODO: podpiac suwaki do callbacka
# TODO: ustawiz dobre zakresy na suwakach okienkowania
# TODO: opakowac w zewnetrzny interfejs
# TODO: rozkminic metode na kolorowanie przedzialow
# TODO: flip YZ
# TODO: dobrze sie bawic

__author__ = 'MKozuch'

from PyQt4 import QtGui, QtCore
from DicomVis_ui import Ui_Form
import vtk

try:
    from lib import StudyData as StudyData
    from lib import VisuAnalysisWidget
except(ImportError):
    class VisuAnalysisWidget(QtGui.QWidget):
        pass


class DicomVis(VisuAnalysisWidget):

    def __init__(self, parent = None):

        self.reader = vtk.vtkDICOMImageReader()
        self.dataExtent = []
        self.dataDimensions = []
        self.dataRange = ()

        # initialize GUI
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.WindowCenterSlider.setRange(0, 1000)
        self.ui.WindowWidthSlider.setRange(0, 1000)

        # define viewers
        [self.viewerXY, self.viewerYZ, self.viewerXZ] = [vtk.vtkResliceImageViewer() for x in range(3)]

        self.viewerXY.SetRenderWindow(self.ui.XYPlaneWidget.GetRenderWindow())
        # self.ui.XYPlaneWidget.SetRenderWindow(self.viewerXY.GetRenderWindow())
        # self.ui.XYPlaneWidget.GetRenderWindow().SetupInteractor(self.viewerXY.GetInteractor())

        self.viewerXY.SetupInteractor(self.ui.XYPlaneWidget.GetRenderWindow().GetInteractor())
        self.viewerYZ.SetupInteractor(self.ui.YZPlaneWidget)
        self.viewerXZ.SetupInteractor(self.ui.XZPlaneWidget)

        self.viewerYZ.SetRenderWindow(self.ui.YZPlaneWidget.GetRenderWindow())
        self.viewerXZ.SetRenderWindow(self.ui.XZPlaneWidget.GetRenderWindow())

        # set slicing orientation for viewers
        self.viewerXY.SetSliceOrientationToXZ()
        self.viewerYZ.SetSliceOrientationToYZ()
        self.viewerXZ.SetSliceOrientationToXY()


    def updateData(self, studydata):
        self.load_study_from_path(studydata.getPath())


    def load_study_from_path(self, studyPath):

        # Update reader
        self.reader.SetDirectoryName(studyPath)
        self.reader.Update()

        self.xyMapper = vtk.vtk

        # # Setup transformation
        # self.transform.RotateWXYZ(180, 1, 1, 0)
        # self.transformFilter.SetTransform(self.transform)
        # self.transformFilter.SetInputConnection(self.reader.GetOutputPort())

        # Get data dimensionality
        self.dataExtent = self.reader.GetDataExtent()
        dataDimensionX = self.dataExtent[1]-self.dataExtent[0]
        dataDimensionY = self.dataExtent[3]-self.dataExtent[2]
        dataDimensionZ = self.dataExtent[5]-self.dataExtent[4]
        self.dataDimensions = [dataDimensionX, dataDimensionY, dataDimensionZ]

        # Calculate index of middle slice
        midslice1 = int((self.dataExtent[1]-self.dataExtent[0])/2 + self.dataExtent[0])
        midslice2 = int((self.dataExtent[3]-self.dataExtent[2])/2 + self.dataExtent[2])
        midslice3 = int((self.dataExtent[5]-self.dataExtent[4])/2 + self.dataExtent[4])

        # Calculate enter
        center = [midslice1, midslice2, midslice3]

        # Get data range
        self.dataRange = self.reader.GetOutput().GetPointData().GetArray("DICOMImage").GetRange()

        # Set current slice to the middle one
        for pair in zip([self.viewerXY, self.viewerYZ, self.viewerXZ], [midslice1, midslice2, midslice3]):
            pair[0].SetInputData(self.reader.GetOutput())
            pair[0].SetSlice(pair[1])
            pair[0].Render()
        pass

        # Set range and proper value for slice sliders
        for pair in zip([self.ui.XYSlider, self.ui.YZSlider, self.ui.XZSlider,], self.dataDimensions, [midslice1, midslice2, midslice3]):
            pair[0].setRange(0, pair[1])
            pair[0].setValue(pair[2])

        # Set range and value for windowing sliders
        self.ui.WindowCenterSlider.setRange(int(self.dataRange[0]), int(self.dataRange[1]))
        self.ui.WindowWidthSlider.setRange(1, int(self.dataRange[1]))


    # setup slots for slicing sliders
    @QtCore.pyqtSlot(int)
    def on_XYSlider_valueChanged(self, value):
        self.viewerXY.SetSlice(value)

    @QtCore.pyqtSlot(int)
    def on_YZSlider_valueChanged(self, value):
        self.viewerYZ.SetSlice(value)

    @QtCore.pyqtSlot(int)
    def on_XZSlider_valueChanged(self, value):
        self.viewerXZ.SetSlice(value)


    # Setup slots for windowing sliders
    @QtCore.pyqtSlot(int)
    def on_WindowCenterSlider_valueChanged(self, value):
        for x in [self.viewerXY, self.viewerXZ, self.viewerYZ]:
            x.SetColorLevel(value)
            x.Render()
        print(value)

    @QtCore.pyqtSlot(int)
    def on_WindowWidthSlider_valueChanged(self, value):
        for x in [self.viewerXY, self.viewerXZ, self.viewerYZ]:
            x.SetColorWindow(value)
            x.Render()
        print(value)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = DicomVis()
    print(type(window))
    window.show()

    studyPath = "C:\\DICOM_resources\\BRAINIX\\T1-3D-FFE-C - 801"
    window.load_study_from_path(studyPath)
    exitStatus = app.exec_()
    #del(window)
    sys.exit(exitStatus)
