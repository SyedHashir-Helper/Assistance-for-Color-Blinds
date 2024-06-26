# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QComboBox, QFrame, QHBoxLayout, QLabel, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor, QCursor, QPixmap
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import cv2, imutils
import numpy as np
import webcolors
from PIL import Image



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.myColors =  {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "voilet": (148, 0, 211),  # Violet
        "brown": (165, 42, 42)  ,   # Brown
        "orange": (255, 165, 0)
        # Add more colors as needed
    }
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 1800, 850))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setStyleSheet("border-color: rgb(45, 45, 45);")
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabs.setIconSize(QtCore.QSize(25, 25))
        self.tabs.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabs.setUsesScrollButtons(True)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(True)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self.videoTab = QtWidgets.QWidget()
        self.videoTab.setObjectName("videoTab")
        self.graphicsView = QtWidgets.QGraphicsView(self.videoTab)
        self.graphicsView.setGeometry(QtCore.QRect(80, 100, 640, 360))
        self.graphicsView.setStyleSheet("/*box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );*/\n"
"backdrop-filter: blur( 4px );\n"
"/*-webkit-backdrop-filter: blur( 4px );\n"
"border-radius: 10px;\n"
"border: 1px solid rgba( 255, 255, 255, 0.18 );*/\n"
"background-color: rgb(63, 63, 63);\n"
"border-radius: 10px;")
        self.graphicsView.setObjectName("graphicsView")
        self.btnForward = QtWidgets.QPushButton(self.videoTab)
        self.btnForward.setGeometry(QtCore.QRect(240, 470, 61, 61))
        self.btnForward.setStyleSheet("border-radius:30px;\n"
"image: url(:/forward/fast-forward.png);\n"
"background-color: rgba(0,0,0,200);\n"
"padding:10px;")
        self.btnForward.setText("")
        self.btnForward.setObjectName("btnForward")
        self.btnBackward = QtWidgets.QPushButton(self.videoTab)
        self.btnBackward.setGeometry(QtCore.QRect(80, 470, 61, 61))
        self.btnBackward.setStyleSheet("border-radius:30px;\n"
"image: url(:/forward/fast-backward.png);\n"
"background-color: rgba(0,0,0,200);\n"
"padding:10px;")
        self.btnBackward.setText("")
        self.btnBackward.setObjectName("btnBackward")
        self.btnForward_2 = QtWidgets.QPushButton(self.videoTab)
        self.btnForward_2.setGeometry(QtCore.QRect(160, 470, 61, 61))
        self.btnForward_2.setStyleSheet("border-radius:30px;\n"
"image: url(:/forward/play.png);\n"
"background-color: rgba(0,0,0,200);\n"
"padding:10px;")
        self.btnForward_2.setText("")
        self.btnForward_2.setObjectName("btnForward_2")
        self.btnForward_2.clicked.connect(self.playPauseButton)
        self.horizontalSlider = QtWidgets.QSlider(self.videoTab)
        self.horizontalSlider.setGeometry(QtCore.QRect(110, 430, 581, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.cmbxSpeed = QtWidgets.QComboBox(self.videoTab)
        self.cmbxSpeed.setGeometry(QtCore.QRect(590, 470, 131, 51))
        self.cmbxSpeed.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(56, 56, 56);\n"
"color: rgb(85, 170, 0);")
        self.cmbxSpeed.setEditable(False)
        self.cmbxSpeed.setCurrentText("")
        self.cmbxSpeed.setObjectName("cmbxSpeed")
        self.cmbxSpeed.addItem("0.5x")
        self.cmbxSpeed.addItem("1.0x")
        self.cmbxSpeed.addItem("1.5x")
        self.cmbxSpeed.addItem("2.0x")
        self.gbFile = QtWidgets.QGroupBox(self.videoTab)
        self.gbFile.setGeometry(QtCore.QRect(60, 70, 681, 650))
        self.gbFile.setStyleSheet("border-color: rgb(0, 170, 0);\n"
"border: 2px solid  rgb(57, 57, 57);\n"
"border-radius: 10px;")
        self.gbFile.setObjectName("gbFile")
        self.txtFileName = QtWidgets.QLineEdit(self.videoTab)
        self.txtFileName.setGeometry(QtCore.QRect(60, 29, 551, 31))
        self.txtFileName.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(58, 58, 58);\n"
"color: white;")
        self.txtFileName.setObjectName("txtFileName")
        self.btnBrowse = QtWidgets.QPushButton(self.videoTab)
        self.btnBrowse.clicked.connect(self.openFileDialog)
        self.btnBrowse.setGeometry(QtCore.QRect(620, 30, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(65, 65, 65);\n"
"color: white;")
        self.btnBrowse.setObjectName("btnBrowse")
        self.gbFile.raise_()
        self.graphicsView.raise_()
        self.btnForward.raise_()
        self.btnBackward.raise_()
        self.btnForward_2.raise_()
        self.horizontalSlider.raise_()
        self.cmbxSpeed.raise_()
        self.txtFileName.raise_()
        self.btnBrowse.raise_()
        self.tabs.addTab(self.videoTab, "")
        self.cameraTab = QtWidgets.QWidget()
        self.cameraTab.setObjectName("cameraTab")
        self.graphicsViewCam = QtWidgets.QGraphicsView(self.cameraTab)
        self.graphicsViewCam.setGeometry(QtCore.QRect(80, 70, 640, 360))
        self.graphicsViewCam.setStyleSheet("/*box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );*/\n"
"backdrop-filter: blur( 4px );\n"
"/*-webkit-backdrop-filter: blur( 4px );\n"
"border-radius: 10px;\n"
"border: 1px solid rgba( 255, 255, 255, 0.18 );*/\n"
"background-color: rgb(63, 63, 63);\n"
"border-radius: 10px;")
        self.graphicsViewCam.setObjectName("graphicsViewCam")

        self.graphicsViewDet = QtWidgets.QGraphicsView(self.videoTab)
        self.graphicsViewDet.setGeometry(QtCore.QRect(1050, 200, 480, 270))
        self.graphicsViewDet.setStyleSheet("/*box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );*/\n"
"backdrop-filter: blur( 4px );\n"
"/*-webkit-backdrop-filter: blur( 4px );\n"
"border-radius: 10px;\n"
"border: 1px solid rgba( 255, 255, 255, 0.18 );*/\n"
"background-color: rgb(63, 63, 63);\n"
"border-radius: 10px;")
        self.graphicsViewCam.setObjectName("graphicsViewDet")

        self.gbFile_2 = QtWidgets.QGroupBox(self.cameraTab)
        self.gbFile_2.setGeometry(QtCore.QRect(60, 40, 681, 491))
        self.gbFile_2.setStyleSheet("border-color: rgb(0, 170, 0);\n"
"border: 2px solid  rgb(57, 57, 57);\n"
"border-radius: 10px;")
        self.gbFile_2.setObjectName("gbFile_2")
        self.btnSelect = QtWidgets.QPushButton(self.gbFile_2)
        self.btnSelect.setGeometry(QtCore.QRect(540, 430, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSelect.setFont(font)
        self.btnSelect.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(65, 65, 65);\n"
"color: white;")
        self.cameras = self.get_camera_info()
        self.btnSelect.setObjectName("btnSelect")
        self.btnSelect.clicked.connect(self.openCamera)
        self.cmbxCam = QtWidgets.QComboBox(self.gbFile_2)
        self.cmbxCam.setGeometry(QtCore.QRect(20, 430, 511, 31))
        self.cmbxCam.setAutoFillBackground(False)
        self.cmbxCam.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"border-radius: 10px;\n"
"color:white;\n"
"text-alignment:left;")

###
        self.video_source_color_button = QtWidgets.QPushButton("Source", self.videoTab )
        self.video_source_color_button.setGeometry(QtCore.QRect(80, 535, 61, 61))
        self.video_target_color_button = QtWidgets.QPushButton("Target", self.videoTab )
        self.video_target_color_button.setGeometry(QtCore.QRect(160, 535, 61, 61))
        self.convert_video_button = QPushButton("Convert", self.videoTab )
        self.convert_video_button.setGeometry(QtCore.QRect(650, 535, 61, 61))

        self.video_source_color_button.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(58, 58, 58);\n"
"color: white;")
        
        self.video_target_color_button.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(58, 58, 58);\n"
"color: white;")
        
        self.convert_video_button.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(58, 58, 58);\n"
"color: white;")
        
        

        self.yellow = QtWidgets.QPushButton("Yellow", self.videoTab)
        self.yellow.setGeometry(QtCore.QRect(80, 620, 60, 60))
        self.yellow.clicked.connect(lambda: self.setSourceColorQuick("Yellow"))
        self.yellow.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")

        self.blue = QtWidgets.QPushButton("Blue", self.videoTab)
        self.blue.setGeometry(QtCore.QRect(167, 620, 60, 60))
        self.blue.clicked.connect(lambda: self.setSourceColorQuick("Blue"))
        self.blue.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")

        self.green = QtWidgets.QPushButton("Green", self.videoTab)
        self.green.setGeometry(QtCore.QRect(247, 620, 60, 60))
        self.green.clicked.connect(lambda: self.setSourceColorQuick("Green"))
        self.green.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")
        
        self.brown = QtWidgets.QPushButton("Brown", self.videoTab)
        self.brown.setGeometry(QtCore.QRect(327, 620, 60, 60))
        self.brown.clicked.connect(lambda: self.setSourceColorQuick("Brown"))
        self.brown.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")
        
        self.orange = QtWidgets.QPushButton("Orange", self.videoTab)
        self.orange.setGeometry(QtCore.QRect(407, 620, 60, 60))
        self.orange.clicked.connect(lambda: self.setSourceColorQuick("Orange"))
        self.orange.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")

        self.red = QtWidgets.QPushButton("Red", self.videoTab)
        self.red.setGeometry(QtCore.QRect(487, 620, 60, 60))
        self.red.clicked.connect(lambda: self.setSourceColorQuick("Red"))
        self.red.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")

        self.voilet = QtWidgets.QPushButton("Voilet", self.videoTab)
        self.voilet.setGeometry(QtCore.QRect(567, 620, 60, 60))
        self.voilet.clicked.connect(lambda: self.setSourceColorQuick("Voilet"))
        self.voilet.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")

        self.white = QtWidgets.QPushButton("White", self.videoTab)
        self.white.setGeometry(QtCore.QRect(647, 620, 60, 60))
        self.white.clicked.connect(lambda: self.setSourceColorQuick("White"))
###
        self.white.setStyleSheet("border-radius: 30px; border: 2px solid black;\n"
"background-color: none;\n"
"color: black;")


        self.timer = QtCore.QTimer(self.videoTab)
        self.timer.timeout.connect(self.update_color)
        self.timer.start(100)

        self.backColor = QLabel(self.videoTab)
        self.backColor.setGeometry(QtCore.QRect(1300, 500, 100, 50))
        self.backColorValue = QLabel(self.videoTab)
        self.backColorValue.setGeometry(QtCore.QRect(1300, 560, 200, 50))


        self.color_mappings = [((0, 0, 255), (255, 0, 0))]
        title = QHBoxLayout()
        source_title = QLabel(self.videoTab)
        source_title.setText(f"Source")
        source_title.setStyleSheet("color: black; font-size:8pt")
        source_title.setAlignment(QtCore.Qt.AlignCenter)
        source_title.setGeometry(QtCore.QRect(800, 50, 61, 50))
        target_title = QLabel(self.videoTab)
        target_title.setText(f"Target")
        target_title.setStyleSheet("color: black; font-size:8pt")
        target_title.setAlignment(QtCore.Qt.AlignCenter)
        # target_title.setGeometry(QtCore.QRect(880, 50, 61, 50))
        button_title = QLabel(self.videoTab)
        button_title.setText(f"Delete")
        button_title.setStyleSheet("color: black; font-size:8pt")
        button_title.setAlignment(QtCore.Qt.AlignCenter)
        title.addWidget(source_title)
        title.addWidget(target_title)
        title.addWidget(button_title)
        layout = QVBoxLayout()
        layout.addLayout(title)
        layout.setAlignment(QtCore.Qt.AlignTop)
        for i, (source_color, target_color) in enumerate(self.color_mappings):
                print(source_color, target_color)
                source_label = QLabel()
                source_label.setText(f"{source_color}")
                source_label.setStyleSheet(f" border-radius: 30px; background-color: rgb{source_color}; color: white;")
                source_label.setAlignment(QtCore.Qt.AlignCenter)

                target_label = QLabel()
                target_label.setText(f"{target_color}")
                target_label.setStyleSheet(f"background-color: rgb{target_color}; color: black;  border-radius: 30px;")
                target_label.setAlignment(QtCore.Qt.AlignCenter)

                delete_button = QPushButton("Delete")
                delete_button.setStyleSheet("border-radius: 30px;\n"
                                                "background-color: rgb(58, 58, 58);\n"
                                                "color: white;")
                delete_button.clicked.connect(lambda _, idx=i: self.deleteColorMapping(idx))

                color_layout = QHBoxLayout()
                color_layout.addWidget(source_label)
                color_layout.addWidget(target_label)
                color_layout.addWidget(delete_button)

                layout.addLayout(color_layout)

        print(self.videoTab.children())
        # Create the frame
        self.frame = QFrame(self.videoTab)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)
        self.frame.setGeometry(QtCore.QRect(800, 20, 200, 700))

        self.frame.setLayout(layout)
 

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

###
        
        # Add Items in CamBox

        for camera in self.cameras:
                        self.cmbxCam.addItem(camera['name'])

        #
        self.cmbxCam.setObjectName("cmbxCam")
        self.gbFile_2.raise_()
        self.graphicsViewCam.raise_()
        self.tabs.addTab(self.cameraTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.state = "pause"
        self.path = ""
        self.loaded = False
        self.playing = False
        self.video = ""

        self.convert_video_button.clicked.connect(self.addColorsinList)
        self.video_source_color_button.clicked.connect(self.select_video_source_color)
        self.video_target_color_button.clicked.connect(self.select_video_target_color)
    
    def update_color(self):
        cursor = QCursor.pos()  # Get global cursor position
        screen = QApplication.primaryScreen()  # Get primary screen
        pixmap = screen.grabWindow(0, cursor.x(), cursor.y(), 1, 1)  # Grab 1x1 pixel around cursor
        pixel = pixmap.toImage().pixel(0, 0)  # Get pixel color
        color = QColor(pixel)  # Convert to QColor
        self.backColor.setStyleSheet("background-color: %s;" % color.name())  # Set label background color
        self.backColorValue.setText(f"{self.hex_to_color_name(color.name())}" + " - RGB: (%d, %d, %d)" % (color.red(), color.green(), color.blue()))

    def setSourceColorQuick(self, color):
        colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "voilet": (148, 0, 211),  # Violet
        "brown": (165, 42, 42)  ,   # Brown
        "orange": (255, 165, 0)
        # Add more colors as needed
    }

    # Convert color name to lowercase to make the comparison case-insensitive
        color_name = color.lower()

    # Check if the color name exists in the dictionary
        if color_name in colors:
                self.video_source_color = colors[color_name]
                self.video_source_color_button.setStyleSheet("border-radius: 30px;\n"
f"background-color: rgb{self.video_source_color};\n"
"color: white;")

    def addColorsinList(self):
        if self.video_source_color != "" and self.video_target_color != "":
                self.color_mappings.append((self.video_source_color, self.video_target_color))
                self.video_source_color_button.setStyleSheet("border-radius: 30px;\n"
"background-color: rgb(58, 58, 58);\n"
"color: white;")
        
                self.video_target_color_button.setStyleSheet("border-radius: 30px;\n"
        "background-color: rgb(58, 58, 58);\n"
        "color: white;")
                # Remove the existing layout from the frame
                layout = self.frame.layout()
                if layout is not None:
                        QWidget().setLayout(layout)

                # Create a new layout for the frame
                new_layout = QVBoxLayout()
                new_layout.setAlignment(QtCore.Qt.AlignTop)
                self.frame.setLayout(new_layout)

                # Add the title row
                title = QHBoxLayout()
                source_title = QLabel(self.videoTab)
                source_title.setText(f"Source")
                source_title.setStyleSheet("color: black; font-size:8pt")
                source_title.setAlignment(QtCore.Qt.AlignCenter)
                target_title = QLabel(self.videoTab)
                target_title.setText(f"Target")
                target_title.setStyleSheet("color: black; font-size:8pt")
                target_title.setAlignment(QtCore.Qt.AlignCenter)
                button_title = QLabel(self.videoTab)
                button_title.setText(f"Delete")
                button_title.setStyleSheet("color: black; font-size:8pt")
                button_title.setAlignment(QtCore.Qt.AlignCenter)
                title.addWidget(source_title)
                title.addWidget(target_title)
                title.addWidget(button_title)
                new_layout.addLayout(title)

                # Add the remaining color mappings
                for i, (source_color, target_color) in enumerate(self.color_mappings):
                        source_label = QLabel()
                        source_label.setText(f"{source_color}")
                        source_label.setStyleSheet(f" border-radius: 30px; background-color: rgb{source_color}; color: white;")
                        source_label.setAlignment(QtCore.Qt.AlignCenter)
                        target_label = QLabel()
                        target_label.setText(f"{target_color}")
                        target_label.setStyleSheet(f"background-color: rgb{target_color}; color: black; border-radius: 30px;")
                        target_label.setAlignment(QtCore.Qt.AlignCenter)
                        delete_button = QPushButton("Delete")
                        delete_button.setStyleSheet("border-radius: 30px;\n"
                                                "background-color: rgb(58, 58, 58);\n"
                                                "color: white;")
                        delete_button.clicked.connect(lambda _, idx=i: self.deleteColorMapping(idx))
                        color_layout = QHBoxLayout()
                        color_layout.addWidget(source_label)
                        color_layout.addWidget(target_label)
                        color_layout.addWidget(delete_button)
                        new_layout.addLayout(color_layout)

                self.frame.setVisible(True)


    def select_video_source_color(self):
        color_dialog = QColorDialog(self.videoTab)
        color = color_dialog.getColor()
        if color.isValid():
            self.video_source_color = (color.red(), color.green(), color.blue())
            self.video_source_color_button.setStyleSheet("border-radius: 30px;\n"
f"background-color: rgb{self.video_source_color};\n"
"color: white;")
        
        
    def select_video_target_color(self):
        color_dialog = QColorDialog(self.videoTab)
        color = color_dialog.getColor()
        if color.isValid():
            self.video_target_color = (color.red(), color.green(), color.blue())
            self.video_target_color_button.setStyleSheet("border-radius: 30px;\n"
f"background-color: rgb{self.video_target_color};\n"
"color: white;")

    def convert_color_cv(self, image, source_color, target_color):
        # Define the lower and upper bounds for the source color range in BGR
        lower_bound, upper_bound = self.get_color_range_bgr((source_color[2],source_color[1], source_color[0] ))

        # Create a mask for the source color pixels
        mask = cv2.inRange(cv2.cvtColor(image, cv2.COLOR_RGB2BGR) , lower_bound, upper_bound)

        # Get the source color pixel values
        source_pixels = image[mask > 0]

        # Convert source color pixel values to the target color in BGR
        target_pixels = source_pixels.copy()
        target_pixels[:, 0] = target_color[2]  # Set the blue channel
        target_pixels[:, 1] = target_color[1]  # Set the green channel
        target_pixels[:, 2] = target_color[0]  # Set the red channel

        # Replace source color pixels with target color pixels
        image[mask > 0] = target_pixels

        return image

    def get_color_range_bgr(self, color):
        lower_bound = np.array(color) - 20
        upper_bound = np.array(color) + 20
        lower_bound = np.clip(lower_bound, 0, 255)
        upper_bound = np.clip(upper_bound, 0, 255)
        return lower_bound, upper_bound
    
    def hex_to_color_name(self, hex_code):
        try:
                color_name = webcolors.hex_to_name(hex_code)
                return color_name
        except ValueError:
                return "Unknown"





    def deleteColorMapping(self, index):
        del self.color_mappings[index]

        # Remove the existing layout from the frame
        layout = self.frame.layout()
        if layout is not None:
                QWidget().setLayout(layout)

        # Create a new layout for the frame
        new_layout = QVBoxLayout()
        new_layout.setAlignment(QtCore.Qt.AlignTop)
        self.frame.setLayout(new_layout)

        # Add the title row
        title = QHBoxLayout()
        source_title = QLabel(self.videoTab)
        source_title.setText(f"Source")
        source_title.setStyleSheet("color: black; font-size:8pt")
        source_title.setAlignment(QtCore.Qt.AlignCenter)
        target_title = QLabel(self.videoTab)
        target_title.setText(f"Target")
        target_title.setStyleSheet("color: black; font-size:8pt")
        target_title.setAlignment(QtCore.Qt.AlignCenter)
        button_title = QLabel(self.videoTab)
        button_title.setText(f"Delete")
        button_title.setStyleSheet("color: black; font-size:8pt")
        button_title.setAlignment(QtCore.Qt.AlignCenter)
        title.addWidget(source_title)
        title.addWidget(target_title)
        title.addWidget(button_title)
        new_layout.addLayout(title)

        # Add the remaining color mappings
        for i, (source_color, target_color) in enumerate(self.color_mappings):
                source_label = QLabel()
                source_label.setText(f"{source_color}")
                source_label.setStyleSheet(f" border-radius: 30px; background-color: rgb{source_color}; color: white;")
                source_label.setAlignment(QtCore.Qt.AlignCenter)
                target_label = QLabel()
                target_label.setText(f"{target_color}")
                target_label.setStyleSheet(f"background-color: rgb{target_color}; color: black; border-radius: 30px;")
                target_label.setAlignment(QtCore.Qt.AlignCenter)
                delete_button = QPushButton("Delete")
                delete_button.setStyleSheet("border-radius: 30px;\n"
                                        "background-color: rgb(58, 58, 58);\n"
                                        "color: white;")
                delete_button.clicked.connect(lambda _, idx=i: self.deleteColorMapping(idx))
                color_layout = QHBoxLayout()
                color_layout.addWidget(source_label)
                color_layout.addWidget(target_label)
                color_layout.addWidget(delete_button)
                new_layout.addLayout(color_layout)

        self.frame.setVisible(True)

        # Create the frame




    def openCamera(self):
        if self.video != "":
                self.video.release()
        index = self.cmbxCam.currentIndex
        self.video = cv2.VideoCapture(0)
        while self.video.isOpened():
                ret,frame = self.video.read()
                if ret is True:
                        frame = cv2.resize(frame,(640,360))
                        frame = cv2.cvtColor(cv2.COLOR_BGR2RGB)
                        image = QtGui.QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)
                        pixmap = QtGui.QPixmap.fromImage(image) # Replace "image.jpg" with the path to your image file
                        
                        scene = QtWidgets.QGraphicsScene()
                        scene.addPixmap(pixmap)
                        self.graphicsViewCam.setScene(scene)
                        self.graphicsViewCam.show()
                else:
                        break
                key = cv2.waitKey(30) & 0xFF
                if key == ord('q'):
                        break
        self.video.release()


    def get_camera_info(self):
        camera_index = 0
        cameras_info = []

        while True:
                # Try to open the camera
                cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

                # Check if the camera is opened successfully
                if not cap.isOpened():
                        break

                # Get the camera name
                camera_name = f"Camera {camera_index}"

                # Try to get camera properties
                try:
                        # Get the camera width and height
                        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                
                        # Get the camera FPS
                        fps = cap.get(cv2.CAP_PROP_FPS)

                        # Get the camera codec
                        codec = cap.get(cv2.CAP_PROP_FOURCC)

                        # Append camera info to the list
                        cameras_info.append({
                                'index': camera_index,
                                'name': camera_name,
                                'resolution': f"{width}x{height}",
                                'fps': fps,
                                'codec': codec
                        })
                except Exception as e:
                        print(f"Error while retrieving camera info for camera {camera_index}: {str(e)}")

                # Release the camera
                cap.release()

                # Move to the next camera index
                camera_index += 1

        return cameras_info
    
    
    def getLimits(self, color):
        color_hsv = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]
        # Define lower and upper bounds for HSV color with a tolerance of +/- 20 for each channel
        h_min = max(0, color_hsv[0] - 20)
        s_min = max(0, color_hsv[1] - 20)
        v_min = max(0, color_hsv[2] - 20)
        
        h_max = min(179, color_hsv[0] + 20)
        s_max = min(255, color_hsv[1] + 20)
        v_max = min(255, color_hsv[2] + 20)
        
        lower_bound = np.array([h_min, s_min, v_min])
        upper_bound = np.array([h_max, s_max, v_max])
        
        return lower_bound, upper_bound


    def playVideo(self):
        if self.loaded:
                if self.video != "":
                        self.video.release()
                self.state = "play"
                if not self.playing:
                        self.playing = True
                self.video = cv2.VideoCapture(self.path)
                while self.video.isOpened():
                        ret,frame = self.video.read()
                        if ret is True:
                                if self.state == "play":
                                        det = cv2.resize(frame,(480,270))
                                        det = cv2.cvtColor(det, cv2.COLOR_BGR2RGB)

                                        hsvImg = cv2.cvtColor(det, cv2.COLOR_RGB2HSV)
                                        for color, values in self.myColors.items():
                                                lowerLim, UpperLim = self.getLimits((values[2], values[1], values[0]))
                                                mask = cv2.inRange(hsvImg, lowerLim, UpperLim)
                                                mask_ = Image.fromarray(mask)
                                                bbox = mask_.getbbox()
                                                if bbox is not None:
                                                        x1,y1,x2,y2 = bbox
                                                        det = cv2.rectangle(det, (x1, y1), (x2, y2), (0,255,0), 1)
                                                        font = cv2.FONT_HERSHEY_SIMPLEX
                                                        det = cv2.putText(det, color, (x1, y1-10), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

                                        image = QtGui.QImage(det, det.shape[1],det.shape[0],det.strides[0],QtGui.QImage.Format_RGB888)
                                        pixmap = QtGui.QPixmap.fromImage(image) # Replace "image.jpg" with the path to your image file
                                        
                                        scene = QtWidgets.QGraphicsScene()
                                        scene.addPixmap(pixmap)
                                        self.graphicsViewDet.setScene(scene)
                                        self.graphicsViewDet.show()

                                        frame = cv2.resize(frame,(640,360))
                                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                        for i,j in self.color_mappings:
                                                frame = self.convert_color_cv(frame, i,j)
                                        image = QtGui.QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)
                                        pixmap = QtGui.QPixmap.fromImage(image) # Replace "image.jpg" with the path to your image file
                                        
                                        scene = QtWidgets.QGraphicsScene()
                                        scene.addPixmap(pixmap)
                                        self.graphicsView.setScene(scene)
                                        self.graphicsView.show()
                        else:
                                break
                        key = cv2.waitKey(30) & 0xFF
                        if self.state == "pause":
                                while True:
                                        key = cv2.waitKey(0) & 0xFF
                                        # Press 'r' to resume the video
                                        if self.state == "play":
                                                break
                        if key == ord('q'):
                                break
                self.btnForward_2.setStyleSheet("border-radius:30px;\n"
                "image: url(:/forward/play.png);\n"
                "background-color: rgba(0,0,0,200);\n"
        "padding:10px;")
                self.btnForward_2.setStyleSheet("border-radius:30px;\n"
        "image: url(:/forward/play.png);\n"
        "background-color: rgba(0,0,0,200);\n"
"padding:10px;")
                self.state = "pause"
                self.playing = False
                print("aya")
        #         self.graphicsView = QtWidgets.QGraphicsView(self.videoTab)
        #         self.graphicsView.setGeometry(QtCore.QRect(80, 100, 640, 360))
        #         self.graphicsView.setStyleSheet("/*box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );*/\n"
        # "backdrop-filter: blur( 4px );\n"
        # "/*-webkit-backdrop-filter: blur( 4px );\n"
        # "border-radius: 10px;\n"
        # "border: 1px solid rgba( 255, 255, 255, 0.18 );*/\n"
        # "background-color: rgb(63, 63, 63);\n"
        # "border-radius: 10px;")
        #         self.graphicsView.setObjectName("graphicsView")
        

    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName(self.videoTab,"Open Video File", "", "Video Files (*.mp4 *.avi *.mov *.mkv)")
        if filename:
                self.txtFileName.setText(str(filename[0]))
                name = str(filename[0]).split('/')
                self.gbFile.setTitle(name[len(name)-1])
                self.path = (str(filename[0]))
                self.loaded = True
                self.btnForward_2.setStyleSheet("border-radius:30px;\n"
        "image: url(:/forward/play.png);\n"
        "background-color: rgba(0,0,0,200);\n"
"padding:10px;")
                self.state = "pause"
                self.playing = False
                if self.video != "":
                        self.video.release()

    def playPauseButton(self):
                if 'play.png' in str(self.btnForward_2.styleSheet()):
                        self.state = "play"
                        self.btnForward_2.setStyleSheet("border-radius:30px;\n"
        "image: url(:/forward/pause.png);\n"
        "background-color: rgba(0,0,0,200);\n"   
"padding:10px;")
                        
                else:
                        self.btnForward_2.setStyleSheet("border-radius:30px;\n"
        "image: url(:/forward/play.png);\n"
        "background-color: rgba(0,0,0,200);\n"
"padding:10px;")
                        self.state = "pause"

                if not self.playing:
                        self.playVideo()
                # self.player = QMediaPlayer()
                # self.video_widget = QVideoWidget()
                # self.player.setVideoOutput(self.video_widget)

                # self.scene.addWidget(self.video_widget)


                # self.media = QMediaContent(QtCore.QUrl.fromLocalFile("hashir.mp4"))
                # self.player.setMedia(self.media)
                # self.player.play()

                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabs.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Video</span></p></body></html>"))
        self.gbFile.setTitle(_translate("MainWindow", "FileName"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.tabs.setTabText(self.tabs.indexOf(self.videoTab), _translate("MainWindow", "Video"))
        self.gbFile_2.setTitle(_translate("MainWindow", "Cam"))
        self.btnSelect.setText(_translate("MainWindow", "Select"))
        self.tabs.setTabText(self.tabs.indexOf(self.cameraTab), _translate("MainWindow", "Camera"))
import res__rc

app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(200,200,801,581)
window.setWindowTitle("Falcon Video Player")

win = Ui_MainWindow()
win.setupUi(window)

window.show()
sys.exit(app.exec_())
