from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

import maya.cmds as cmds

# Creating a mini-car in maya
def car_creator():
    cmds.polyCube(d=7, h=5, w=5)

    wheel1 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel1)
    cmds.rotate(0, 0, 90)
    cmds.move(3, -2, 2.5)

    wheel2 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel2)
    cmds.rotate(0, 0, 90)
    cmds.move(-3, -2, -2.5)

    wheel3 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel3)
    cmds.rotate(0, 0, 90)
    cmds.move(3, -2, -2.5)

    wheel4 = cmds.polyCylinder(r=2, h=1, sa=10)
    cmds.select(wheel4)
    cmds.rotate(0, 0, 90)
    cmds.move(-3, -2, 2.5)

# Get a reference to the main Maya application window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

class MyMayaWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyMayaWidget, self).__init__(*args, **kwargs)

        # Parent widget under Maya main window
        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)

        # Set the UI display title and size
        self.setWindowTitle('Random Geo Generator')
        self.setGeometry(50, 50, 250, 150)

        # Create and place buttons
        self.carButton = QPushButton('Car', self)
        self.carButton.move(5, 25)

        self.cubeButton = QPushButton('Cube', self)
        self.cubeButton.move(5, 0)

        # When the button is clicked, connect a signal to run
        # the function below
        self.carButton.clicked.connect(self.carButton_onClicked)
        self.cubeButton.clicked.connect(self.cubeButton_onClicked)

    def carButton_onClicked(self):
        car_creator()
        print("Clicked!")

    def cubeButton_onClicked(self):
        cmds.polyCube()
        cmds.move(10, 0, 0)
        print("Clicked!")


my_widget = MyMayaWidget()
my_widget.show()