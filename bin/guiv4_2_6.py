# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv4_2_6.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1635, 1019)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.framePositionButtons = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePositionButtons.sizePolicy().hasHeightForWidth())
        self.framePositionButtons.setSizePolicy(sizePolicy)
        self.framePositionButtons.setMinimumSize(QtCore.QSize(500, 400))
        self.framePositionButtons.setMaximumSize(QtCore.QSize(500, 400))
        self.framePositionButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePositionButtons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.framePositionButtons.setObjectName("framePositionButtons")
        self.motion_grid = QtWidgets.QGridLayout(self.framePositionButtons)
        self.motion_grid.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.motion_grid.setSpacing(5)
        self.motion_grid.setObjectName("motion_grid")
        self.plus180 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus180.setObjectName("plus180")
        self.motion_grid.addWidget(self.plus180, 6, 3, 1, 1)
        self.zeroAll = QtWidgets.QPushButton(self.framePositionButtons)
        self.zeroAll.setMinimumSize(QtCore.QSize(50, 50))
        self.zeroAll.setFlat(False)
        self.zeroAll.setObjectName("zeroAll")
        self.motion_grid.addWidget(self.zeroAll, 1, 1, 1, 1)
        self.plus5 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus5.setObjectName("plus5")
        self.motion_grid.addWidget(self.plus5, 6, 0, 1, 1)
        self.right = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../right.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.right.setIcon(icon1)
        self.right.setIconSize(QtCore.QSize(60, 60))
        self.right.setObjectName("right")
        self.motion_grid.addWidget(self.right, 1, 2, 1, 1)
        self.left = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon2)
        self.left.setIconSize(QtCore.QSize(60, 60))
        self.left.setObjectName("left")
        self.motion_grid.addWidget(self.left, 1, 0, 1, 1)
        self.zero = QtWidgets.QPushButton(self.framePositionButtons)
        self.zero.setObjectName("zero")
        self.motion_grid.addWidget(self.zero, 2, 3, 1, 1)
        self.minus180 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus180.setObjectName("minus180")
        self.motion_grid.addWidget(self.minus180, 5, 3, 1, 1)
        self.minus90 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus90.setObjectName("minus90")
        self.motion_grid.addWidget(self.minus90, 5, 2, 1, 1)
        self.pushButtonSampleIn = QtWidgets.QPushButton(self.framePositionButtons)
        self.pushButtonSampleIn.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleIn.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleIn.setObjectName("pushButtonSampleIn")
        self.motion_grid.addWidget(self.pushButtonSampleIn, 0, 0, 1, 1)
        self.minus15 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus15.setObjectName("minus15")
        self.motion_grid.addWidget(self.minus15, 5, 1, 1, 1)
        self.plus15 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus15.setObjectName("plus15")
        self.motion_grid.addWidget(self.plus15, 6, 1, 1, 1)
        self.buttonSlowOmegaTurn = QtWidgets.QPushButton(self.framePositionButtons)
        self.buttonSlowOmegaTurn.setObjectName("buttonSlowOmegaTurn")
        self.motion_grid.addWidget(self.buttonSlowOmegaTurn, 2, 0, 1, 1)
        self.plusMinus3600 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plusMinus3600.setObjectName("plusMinus3600")
        self.motion_grid.addWidget(self.plusMinus3600, 0, 3, 1, 1)
        self.plus90 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus90.setObjectName("plus90")
        self.motion_grid.addWidget(self.plus90, 6, 2, 1, 1)
        self.minus5 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus5.setObjectName("minus5")
        self.motion_grid.addWidget(self.minus5, 5, 0, 1, 1)
        self.buttonFastOmegaTurn = QtWidgets.QPushButton(self.framePositionButtons)
        self.buttonFastOmegaTurn.setObjectName("buttonFastOmegaTurn")
        self.motion_grid.addWidget(self.buttonFastOmegaTurn, 2, 2, 1, 1)
        self.pushButtonSampleOut = QtWidgets.QPushButton(self.framePositionButtons)
        self.pushButtonSampleOut.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSampleOut.sizePolicy().hasHeightForWidth())
        self.pushButtonSampleOut.setSizePolicy(sizePolicy)
        self.pushButtonSampleOut.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleOut.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleOut.setAutoDefault(False)
        self.pushButtonSampleOut.setDefault(False)
        self.pushButtonSampleOut.setFlat(False)
        self.pushButtonSampleOut.setObjectName("pushButtonSampleOut")
        self.motion_grid.addWidget(self.pushButtonSampleOut, 0, 2, 1, 1)
        self.up = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy)
        self.up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../up.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.up.setIcon(icon3)
        self.up.setIconSize(QtCore.QSize(60, 60))
        self.up.setObjectName("up")
        self.motion_grid.addWidget(self.up, 0, 1, 1, 1)
        self.down = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.down.sizePolicy().hasHeightForWidth())
        self.down.setSizePolicy(sizePolicy)
        self.down.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../down.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.down.setIcon(icon4)
        self.down.setIconSize(QtCore.QSize(60, 60))
        self.down.setAutoRepeat(False)
        self.down.setAutoExclusive(False)
        self.down.setObjectName("down")
        self.motion_grid.addWidget(self.down, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.framePositionButtons, 3, 0, 1, 1)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 2, 2, 1, 1)
        self.oav_stream = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oav_stream.sizePolicy().hasHeightForWidth())
        self.oav_stream.setSizePolicy(sizePolicy)
        self.oav_stream.setMinimumSize(QtCore.QSize(0, 0))
        self.oav_stream.setMaximumSize(QtCore.QSize(2012, 1518))
        self.oav_stream.setSizeIncrement(QtCore.QSize(0, 0))
        self.oav_stream.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.oav_stream.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oav_stream.setText("")
        self.oav_stream.setPixmap(QtGui.QPixmap("../icon.png"))
        self.oav_stream.setScaledContents(True)
        self.oav_stream.setAlignment(QtCore.Qt.AlignCenter)
        self.oav_stream.setObjectName("oav_stream")
        self.gridLayout.addWidget(self.oav_stream, 0, 0, 2, 3)
        self.frameFineControl = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameFineControl.sizePolicy().hasHeightForWidth())
        self.frameFineControl.setSizePolicy(sizePolicy)
        self.frameFineControl.setMinimumSize(QtCore.QSize(400, 300))
        self.frameFineControl.setMaximumSize(QtCore.QSize(400, 300))
        self.frameFineControl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFineControl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameFineControl.setObjectName("frameFineControl")
        self.readback_grid = QtWidgets.QGridLayout(self.frameFineControl)
        self.readback_grid.setObjectName("readback_grid")
        self.gony_rbv = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gony_rbv.sizePolicy().hasHeightForWidth())
        self.gony_rbv.setSizePolicy(sizePolicy)
        self.gony_rbv.setMaximumSize(QtCore.QSize(90, 16777215))
        self.gony_rbv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gony_rbv.setObjectName("gony_rbv")
        self.readback_grid.addWidget(self.gony_rbv, 4, 2, 1, 1)
        self.labZoom = QtWidgets.QLabel(self.frameFineControl)
        self.labZoom.setObjectName("labZoom")
        self.readback_grid.addWidget(self.labZoom, 0, 0, 1, 1)
        self.currentZoom = QtWidgets.QLabel(self.frameFineControl)
        self.currentZoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currentZoom.setAlignment(QtCore.Qt.AlignCenter)
        self.currentZoom.setObjectName("currentZoom")
        self.readback_grid.addWidget(self.currentZoom, 0, 1, 1, 1)
        self.exposure_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.exposure_rbv.setMinimumSize(QtCore.QSize(50, 0))
        self.exposure_rbv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exposure_rbv.setAlignment(QtCore.Qt.AlignCenter)
        self.exposure_rbv.setObjectName("exposure_rbv")
        self.readback_grid.addWidget(self.exposure_rbv, 1, 1, 1, 1)
        self.gain_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.gain_rbv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gain_rbv.setAlignment(QtCore.Qt.AlignCenter)
        self.gain_rbv.setObjectName("gain_rbv")
        self.readback_grid.addWidget(self.gain_rbv, 2, 1, 1, 1)
        self.sliderGain = QtWidgets.QSlider(self.frameFineControl)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGain.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderGain.setTickInterval(5)
        self.sliderGain.setObjectName("sliderGain")
        self.readback_grid.addWidget(self.sliderGain, 2, 2, 1, 1)
        self.stagez_rbv = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stagez_rbv.sizePolicy().hasHeightForWidth())
        self.stagez_rbv.setSizePolicy(sizePolicy)
        self.stagez_rbv.setMaximumSize(QtCore.QSize(90, 16777215))
        self.stagez_rbv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stagez_rbv.setObjectName("stagez_rbv")
        self.readback_grid.addWidget(self.stagez_rbv, 3, 2, 1, 1)
        self.sliderExposure = QtWidgets.QSlider(self.frameFineControl)
        self.sliderExposure.setMinimum(1)
        self.sliderExposure.setMaximum(100)
        self.sliderExposure.setProperty("value", 4)
        self.sliderExposure.setOrientation(QtCore.Qt.Horizontal)
        self.sliderExposure.setInvertedAppearance(False)
        self.sliderExposure.setInvertedControls(False)
        self.sliderExposure.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderExposure.setTickInterval(5)
        self.sliderExposure.setObjectName("sliderExposure")
        self.readback_grid.addWidget(self.sliderExposure, 1, 2, 1, 1)
        self.labExposure = QtWidgets.QLabel(self.frameFineControl)
        self.labExposure.setObjectName("labExposure")
        self.readback_grid.addWidget(self.labExposure, 1, 0, 1, 1)
        self.labGain = QtWidgets.QLabel(self.frameFineControl)
        self.labGain.setObjectName("labGain")
        self.readback_grid.addWidget(self.labGain, 2, 0, 1, 1)
        self.gonz_rbv = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gonz_rbv.sizePolicy().hasHeightForWidth())
        self.gonz_rbv.setSizePolicy(sizePolicy)
        self.gonz_rbv.setMaximumSize(QtCore.QSize(90, 16777215))
        self.gonz_rbv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gonz_rbv.setObjectName("gonz_rbv")
        self.readback_grid.addWidget(self.gonz_rbv, 5, 2, 1, 1)
        self.omega_rbv = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.omega_rbv.sizePolicy().hasHeightForWidth())
        self.omega_rbv.setSizePolicy(sizePolicy)
        self.omega_rbv.setMaximumSize(QtCore.QSize(90, 16777215))
        self.omega_rbv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.omega_rbv.setObjectName("omega_rbv")
        self.readback_grid.addWidget(self.omega_rbv, 7, 2, 1, 1)
        self.sliderZoom = QtWidgets.QSlider(self.frameFineControl)
        self.sliderZoom.setMinimum(1)
        self.sliderZoom.setMaximum(5)
        self.sliderZoom.setPageStep(1)
        self.sliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.sliderZoom.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderZoom.setObjectName("sliderZoom")
        self.readback_grid.addWidget(self.sliderZoom, 0, 2, 1, 1)
        self.labstageZ = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labstageZ.sizePolicy().hasHeightForWidth())
        self.labstageZ.setSizePolicy(sizePolicy)
        self.labstageZ.setAlignment(QtCore.Qt.AlignCenter)
        self.labstageZ.setObjectName("labstageZ")
        self.readback_grid.addWidget(self.labstageZ, 3, 0, 1, 2)
        self.labY = QtWidgets.QLabel(self.frameFineControl)
        self.labY.setAlignment(QtCore.Qt.AlignCenter)
        self.labY.setObjectName("labY")
        self.readback_grid.addWidget(self.labY, 4, 0, 1, 2)
        self.labZ = QtWidgets.QLabel(self.frameFineControl)
        self.labZ.setAlignment(QtCore.Qt.AlignCenter)
        self.labZ.setObjectName("labZ")
        self.readback_grid.addWidget(self.labZ, 5, 0, 1, 2)
        self.labOmega = QtWidgets.QLabel(self.frameFineControl)
        self.labOmega.setAlignment(QtCore.Qt.AlignCenter)
        self.labOmega.setObjectName("labOmega")
        self.readback_grid.addWidget(self.labOmega, 7, 0, 1, 2)
        self.gridLayout.addWidget(self.frameFineControl, 3, 2, 1, 1)
        self.tabWidget_robot_laser = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_robot_laser.sizePolicy().hasHeightForWidth())
        self.tabWidget_robot_laser.setSizePolicy(sizePolicy)
        self.tabWidget_robot_laser.setMinimumSize(QtCore.QSize(240, 710))
        self.tabWidget_robot_laser.setMaximumSize(QtCore.QSize(240, 710))
        self.tabWidget_robot_laser.setAccessibleName("")
        self.tabWidget_robot_laser.setObjectName("tabWidget_robot_laser")
        self.tab_robot = QtWidgets.QWidget()
        self.tab_robot.setObjectName("tab_robot")
        self.frameRobot = QtWidgets.QFrame(self.tab_robot)
        self.frameRobot.setGeometry(QtCore.QRect(0, 0, 235, 671))
        self.frameRobot.setAutoFillBackground(False)
        self.frameRobot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRobot.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameRobot.setLineWidth(1)
        self.frameRobot.setObjectName("frameRobot")
        self.robot_grid = QtWidgets.QGridLayout(self.frameRobot)
        self.robot_grid.setObjectName("robot_grid")
        self.labBeamlineSafe = QtWidgets.QLabel(self.frameRobot)
        self.labBeamlineSafe.setAlignment(QtCore.Qt.AlignCenter)
        self.labBeamlineSafe.setObjectName("labBeamlineSafe")
        self.robot_grid.addWidget(self.labBeamlineSafe, 8, 0, 1, 1)
        self.indicatorGonioSensor = QtWidgets.QLabel(self.frameRobot)
        self.indicatorGonioSensor.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorGonioSensor.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorGonioSensor.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorGonioSensor.setText("")
        self.indicatorGonioSensor.setScaledContents(False)
        self.indicatorGonioSensor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.indicatorGonioSensor.setObjectName("indicatorGonioSensor")
        self.robot_grid.addWidget(self.indicatorGonioSensor, 1, 1, 1, 1)
        self.labRobotActive = QtWidgets.QLabel(self.frameRobot)
        self.labRobotActive.setAlignment(QtCore.Qt.AlignCenter)
        self.labRobotActive.setObjectName("labRobotActive")
        self.robot_grid.addWidget(self.labRobotActive, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.robot_grid.addItem(spacerItem2, 7, 0, 1, 2)
        self.goHomeRobot = QtWidgets.QPushButton(self.frameRobot)
        self.goHomeRobot.setObjectName("goHomeRobot")
        self.robot_grid.addWidget(self.goHomeRobot, 10, 1, 1, 1)
        self.currentSamp = QtWidgets.QLabel(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentSamp.sizePolicy().hasHeightForWidth())
        self.currentSamp.setSizePolicy(sizePolicy)
        self.currentSamp.setAutoFillBackground(False)
        self.currentSamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentSamp.setObjectName("currentSamp")
        self.robot_grid.addWidget(self.currentSamp, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.dry = QtWidgets.QPushButton(self.frameRobot)
        self.dry.setObjectName("dry")
        self.robot_grid.addWidget(self.dry, 12, 1, 1, 1)
        self.load = QtWidgets.QPushButton(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy)
        self.load.setObjectName("load")
        self.robot_grid.addWidget(self.load, 11, 0, 1, 1)
        self.indicatorBeamlineSafe = QtWidgets.QLabel(self.frameRobot)
        self.indicatorBeamlineSafe.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorBeamlineSafe.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorBeamlineSafe.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorBeamlineSafe.setText("")
        self.indicatorBeamlineSafe.setObjectName("indicatorBeamlineSafe")
        self.robot_grid.addWidget(self.indicatorBeamlineSafe, 8, 1, 1, 1)
        self.spinToLoad = QtWidgets.QSpinBox(self.frameRobot)
        self.spinToLoad.setProperty("showGroupSeparator", False)
        self.spinToLoad.setMinimum(1)
        self.spinToLoad.setMaximum(16)
        self.spinToLoad.setObjectName("spinToLoad")
        self.robot_grid.addWidget(self.spinToLoad, 11, 1, 1, 1)
        self.resetRobot = QtWidgets.QPushButton(self.frameRobot)
        self.resetRobot.setObjectName("resetRobot")
        self.robot_grid.addWidget(self.resetRobot, 10, 0, 1, 1)
        self.unload = QtWidgets.QPushButton(self.frameRobot)
        self.unload.setObjectName("unload")
        self.robot_grid.addWidget(self.unload, 12, 0, 1, 1)
        self.labCurrentSamp = QtWidgets.QLabel(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labCurrentSamp.sizePolicy().hasHeightForWidth())
        self.labCurrentSamp.setSizePolicy(sizePolicy)
        self.labCurrentSamp.setAlignment(QtCore.Qt.AlignCenter)
        self.labCurrentSamp.setObjectName("labCurrentSamp")
        self.robot_grid.addWidget(self.labCurrentSamp, 0, 0, 1, 1)
        self.indicatorRobotActive = QtWidgets.QLabel(self.frameRobot)
        self.indicatorRobotActive.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorRobotActive.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorRobotActive.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorRobotActive.setText("")
        self.indicatorRobotActive.setObjectName("indicatorRobotActive")
        self.robot_grid.addWidget(self.indicatorRobotActive, 9, 1, 1, 1)
        self.labGonioSensor = QtWidgets.QLabel(self.frameRobot)
        self.labGonioSensor.setAlignment(QtCore.Qt.AlignCenter)
        self.labGonioSensor.setObjectName("labGonioSensor")
        self.robot_grid.addWidget(self.labGonioSensor, 1, 0, 1, 1)
        self.snapshot = QtWidgets.QPushButton(self.frameRobot)
        self.snapshot.setObjectName("snapshot")
        self.robot_grid.addWidget(self.snapshot, 3, 0, 1, 2)
        self.AutoCenter = QtWidgets.QPushButton(self.frameRobot)
        self.AutoCenter.setObjectName("AutoCenter")
        self.robot_grid.addWidget(self.AutoCenter, 4, 0, 1, 2)
        self.tabWidget_robot_laser.addTab(self.tab_robot, "")
        self.tab_laser = QtWidgets.QWidget()
        self.tab_laser.setObjectName("tab_laser")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_laser)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBoxDivider = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxDivider.setMinimum(1)
        self.spinBoxDivider.setMaximum(1000)
        self.spinBoxDivider.setObjectName("spinBoxDivider")
        self.gridLayout_2.addWidget(self.spinBoxDivider, 4, 0, 1, 1)
        self.pushButtonStartupLaser = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonStartupLaser.setObjectName("pushButtonStartupLaser")
        self.gridLayout_2.addWidget(self.pushButtonStartupLaser, 11, 0, 1, 1)
        self.labLaserStatus = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labLaserStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labLaserStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labLaserStatus.setObjectName("labLaserStatus")
        self.gridLayout_2.addWidget(self.labLaserStatus, 9, 0, 1, 2)
        self.pushButtonSetAttenuator = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonSetAttenuator.setObjectName("pushButtonSetAttenuator")
        self.gridLayout_2.addWidget(self.pushButtonSetAttenuator, 7, 1, 1, 1)
        self.labAtenuator = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labAtenuator.setAlignment(QtCore.Qt.AlignCenter)
        self.labAtenuator.setObjectName("labAtenuator")
        self.gridLayout_2.addWidget(self.labAtenuator, 6, 0, 1, 1)
        self.pushButtonDisableLaser = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonDisableLaser.setObjectName("pushButtonDisableLaser")
        self.gridLayout_2.addWidget(self.pushButtonDisableLaser, 1, 1, 1, 1)
        self.labDividerRBV = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labDividerRBV.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labDividerRBV.setAlignment(QtCore.Qt.AlignCenter)
        self.labDividerRBV.setObjectName("labDividerRBV")
        self.gridLayout_2.addWidget(self.labDividerRBV, 3, 1, 1, 1)
        self.pushButtonSetDivider = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonSetDivider.setObjectName("pushButtonSetDivider")
        self.gridLayout_2.addWidget(self.pushButtonSetDivider, 4, 1, 1, 1)
        self.pushButtonStandbyLaser = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonStandbyLaser.setObjectName("pushButtonStandbyLaser")
        self.gridLayout_2.addWidget(self.pushButtonStandbyLaser, 11, 1, 1, 1)
        self.labAttenuatorRBV = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labAttenuatorRBV.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labAttenuatorRBV.setAlignment(QtCore.Qt.AlignCenter)
        self.labAttenuatorRBV.setObjectName("labAttenuatorRBV")
        self.gridLayout_2.addWidget(self.labAttenuatorRBV, 6, 1, 1, 1)
        self.labOUTPUT = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labOUTPUT.setAutoFillBackground(False)
        self.labOUTPUT.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labOUTPUT.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labOUTPUT.setScaledContents(False)
        self.labOUTPUT.setAlignment(QtCore.Qt.AlignCenter)
        self.labOUTPUT.setIndent(-1)
        self.labOUTPUT.setObjectName("labOUTPUT")
        self.gridLayout_2.addWidget(self.labOUTPUT, 0, 0, 1, 1)
        self.doubleSpinBoxAttenuator = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxAttenuator.setDecimals(1)
        self.doubleSpinBoxAttenuator.setMinimum(0.1)
        self.doubleSpinBoxAttenuator.setProperty("value", 10.0)
        self.doubleSpinBoxAttenuator.setObjectName("doubleSpinBoxAttenuator")
        self.gridLayout_2.addWidget(self.doubleSpinBoxAttenuator, 7, 0, 1, 1)
        self.labDivider = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labDivider.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labDivider.setAlignment(QtCore.Qt.AlignCenter)
        self.labDivider.setObjectName("labDivider")
        self.gridLayout_2.addWidget(self.labDivider, 3, 0, 1, 1)
        self.pushButtonEnableLaser = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonEnableLaser.setObjectName("pushButtonEnableLaser")
        self.gridLayout_2.addWidget(self.pushButtonEnableLaser, 1, 0, 1, 1)
        self.labEMISSION = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labEMISSION.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labEMISSION.setAlignment(QtCore.Qt.AlignCenter)
        self.labEMISSION.setObjectName("labEMISSION")
        self.gridLayout_2.addWidget(self.labEMISSION, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 8, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 10, 0, 1, 2)
        self.tabWidget_robot_laser.addTab(self.tab_laser, "")
        self.gridLayout.addWidget(self.tabWidget_robot_laser, 3, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1635, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuIOCs = QtWidgets.QMenu(self.menuBar)
        self.menuIOCs.setObjectName("menuIOCs")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_log = QtWidgets.QAction(MainWindow)
        self.actionSave_log.setObjectName("actionSave_log")
        self.actionRestart_OAV_IOC = QtWidgets.QAction(MainWindow)
        self.actionRestart_OAV_IOC.setObjectName("actionRestart_OAV_IOC")
        self.actionRestart_Robot_IOC = QtWidgets.QAction(MainWindow)
        self.actionRestart_Robot_IOC.setObjectName("actionRestart_Robot_IOC")
        self.actionRestart_Gonio_IOC = QtWidgets.QAction(MainWindow)
        self.actionRestart_Gonio_IOC.setObjectName("actionRestart_Gonio_IOC")
        self.actionRestartLaserIOC = QtWidgets.QAction(MainWindow)
        self.actionRestartLaserIOC.setObjectName("actionRestartLaserIOC")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionSave_log)
        self.menuIOCs.addAction(self.actionRestart_OAV_IOC)
        self.menuIOCs.addAction(self.actionRestart_Robot_IOC)
        self.menuIOCs.addAction(self.actionRestart_Gonio_IOC)
        self.menuIOCs.addAction(self.actionRestartLaserIOC)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuIOCs.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_robot_laser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.load, self.unload)
        MainWindow.setTabOrder(self.unload, self.spinToLoad)
        MainWindow.setTabOrder(self.spinToLoad, self.dry)
        MainWindow.setTabOrder(self.dry, self.start)
        MainWindow.setTabOrder(self.start, self.stop)
        MainWindow.setTabOrder(self.stop, self.sliderExposure)
        MainWindow.setTabOrder(self.sliderExposure, self.sliderGain)
        MainWindow.setTabOrder(self.sliderGain, self.up)
        MainWindow.setTabOrder(self.up, self.down)
        MainWindow.setTabOrder(self.down, self.left)
        MainWindow.setTabOrder(self.left, self.right)
        MainWindow.setTabOrder(self.right, self.minus5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aithre v4.2 - I23 Laser Shaping"))
        self.start.setText(_translate("MainWindow", "Start OAV"))
        self.plus180.setText(_translate("MainWindow", "+180"))
        self.zeroAll.setText(_translate("MainWindow", "ZeroAll"))
        self.plus5.setText(_translate("MainWindow", "+5"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.minus180.setText(_translate("MainWindow", "-180"))
        self.minus90.setText(_translate("MainWindow", "-90"))
        self.pushButtonSampleIn.setText(_translate("MainWindow", "Z-"))
        self.minus15.setText(_translate("MainWindow", "-15"))
        self.plus15.setText(_translate("MainWindow", "+15"))
        self.buttonSlowOmegaTurn.setText(_translate("MainWindow", "Slow Turn"))
        self.plusMinus3600.setText(_translate("MainWindow", "+/- 3600"))
        self.plus90.setText(_translate("MainWindow", "+90"))
        self.minus5.setText(_translate("MainWindow", "-5"))
        self.buttonFastOmegaTurn.setText(_translate("MainWindow", "Fast Turn"))
        self.pushButtonSampleOut.setText(_translate("MainWindow", "Z+"))
        self.stop.setText(_translate("MainWindow", "Stop OAV"))
        self.gony_rbv.setText(_translate("MainWindow", "0.12"))
        self.labZoom.setText(_translate("MainWindow", "Zoom"))
        self.currentZoom.setText(_translate("MainWindow", "1"))
        self.exposure_rbv.setText(_translate("MainWindow", "0.04"))
        self.gain_rbv.setText(_translate("MainWindow", "0"))
        self.stagez_rbv.setText(_translate("MainWindow", "0.352"))
        self.labExposure.setText(_translate("MainWindow", "Exposure"))
        self.labGain.setText(_translate("MainWindow", "Gain"))
        self.gonz_rbv.setText(_translate("MainWindow", "0.55"))
        self.omega_rbv.setText(_translate("MainWindow", "0.00"))
        self.labstageZ.setText(_translate("MainWindow", "Stage Z"))
        self.labY.setText(_translate("MainWindow", "Y"))
        self.labZ.setText(_translate("MainWindow", "Z"))
        self.labOmega.setText(_translate("MainWindow", "Omega"))
        self.labBeamlineSafe.setText(_translate("MainWindow", "Beamline Safe"))
        self.labRobotActive.setText(_translate("MainWindow", "Robot Active"))
        self.goHomeRobot.setText(_translate("MainWindow", "Go Home"))
        self.currentSamp.setText(_translate("MainWindow", "0"))
        self.dry.setText(_translate("MainWindow", "Dry"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.resetRobot.setText(_translate("MainWindow", "Reset"))
        self.unload.setText(_translate("MainWindow", "Unload"))
        self.labCurrentSamp.setText(_translate("MainWindow", "Current Sample"))
        self.labGonioSensor.setText(_translate("MainWindow", "Gonio Sensor"))
        self.snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.AutoCenter.setText(_translate("MainWindow", "AutoCenter"))
        self.tabWidget_robot_laser.setTabText(self.tabWidget_robot_laser.indexOf(self.tab_robot), _translate("MainWindow", "Robot"))
        self.pushButtonStartupLaser.setText(_translate("MainWindow", "Startup"))
        self.labLaserStatus.setText(_translate("MainWindow", "Status"))
        self.pushButtonSetAttenuator.setText(_translate("MainWindow", "Set"))
        self.labAtenuator.setText(_translate("MainWindow", "Attenuator"))
        self.pushButtonDisableLaser.setText(_translate("MainWindow", "Disable"))
        self.labDividerRBV.setText(_translate("MainWindow", "10"))
        self.pushButtonSetDivider.setText(_translate("MainWindow", "Set"))
        self.pushButtonStandbyLaser.setText(_translate("MainWindow", "Standby"))
        self.labAttenuatorRBV.setText(_translate("MainWindow", "20"))
        self.labOUTPUT.setText(_translate("MainWindow", "OUTPUT"))
        self.labDivider.setText(_translate("MainWindow", "Divider"))
        self.pushButtonEnableLaser.setText(_translate("MainWindow", "Enable"))
        self.labEMISSION.setText(_translate("MainWindow", "EMISSION"))
        self.tabWidget_robot_laser.setTabText(self.tabWidget_robot_laser.indexOf(self.tab_laser), _translate("MainWindow", "Laser"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuIOCs.setTitle(_translate("MainWindow", "IOCs"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_log.setText(_translate("MainWindow", "Save log"))
        self.actionRestart_OAV_IOC.setText(_translate("MainWindow", "Restart OAV IOC"))
        self.actionRestart_Robot_IOC.setText(_translate("MainWindow", "Restart Robot IOC"))
        self.actionRestart_Gonio_IOC.setText(_translate("MainWindow", "Restart Gonio IOC"))
        self.actionRestartLaserIOC.setText(_translate("MainWindow", "Restart Laser IOC"))
