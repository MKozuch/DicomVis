#!/usr/bin/env python

''' this script is used to convert Qt *.ui file to PyQt UI class
in order to mae it compatibile with vtk bindings for Python '''


import os
import sys

fileIn = sys.argv[1]

if len(sys.argv) == 3:
    fileOut = sys.argv[2]
elif len(sys.argv) == 2:
    fileOut = sys.argv[1].split('.')[0] + "_ui.py"

fileTemp = '_temp.py'

command = "pyuic4 -o {} {}".format(fileTemp, fileIn)
print('Generating {} from {}'.format(fileOut, fileIn))
print('Executing command: ' + command)
os.system(command)

# Need to do some substitution in generated file to make the UI work in python
# when the QVTKWidget was created to be used in C++

f = open(fileTemp, 'r')
s = f.read()
f.close()

s = s.replace('QVTKWidget','QVTKRenderWindowInteractor')
s = s.replace('from QVTK', 'from vtk.qt4.QVTK')

w = open(fileOut, 'w')
w.write(s)
w.close()

os.remove(fileTemp)

print('Done')
