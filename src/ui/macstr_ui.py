import sys
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # loading in the JSON data
        with open("../../notebooks/test_image_coords.json", "r") as contents:
            image_data = yaml.safe_load(contents)
            print(image_data["cell_image_1.tiff"])

        # creating main GUI window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ------------------------------
        # setting up image canvas
        # ------------------------------
        self.image1 = QtWidgets.QLabel(self.centralwidget)
        self.image1.setGeometry(QtCore.QRect(30, 10, 221, 191))
        self.image1.setText("")
        self.image1.setPixmap(
            QtGui.QPixmap("7-stunning-cell-images-from-2017-294838-640x360.jpg")
        )
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")

        self.image2 = QtWidgets.QLabel(self.centralwidget)
        self.image2.setGeometry(QtCore.QRect(280, 10, 221, 191))
        self.image2.setText("")
        self.image2.setPixmap(
            QtGui.QPixmap("7-stunning-cell-images-from-2017-294838-640x360.jpg")
        )
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")

        self.image3 = QtWidgets.QLabel(self.centralwidget)
        self.image3.setGeometry(QtCore.QRect(530, 10, 221, 191))
        self.image3.setText("")
        self.image3.setPixmap(
            QtGui.QPixmap("7-stunning-cell-images-from-2017-294838-640x360.jpg")
        )
        self.image3.setScaledContents(True)
        self.image3.setObjectName("image3")

        self.image4 = QtWidgets.QLabel(self.centralwidget)
        self.image4.setGeometry(QtCore.QRect(30, 260, 221, 191))
        self.image4.setText("")
        self.image4.setPixmap(
            QtGui.QPixmap("7-stunning-cell-images-from-2017-294838-640x360.jpg")
        )
        self.image4.setScaledContents(True)
        self.image4.setObjectName("image4")

        self.image5 = QtWidgets.QLabel(self.centralwidget)
        self.image5.setGeometry(QtCore.QRect(280, 260, 221, 191))
        self.image5.setText("")
        self.image5.setPixmap(
            QtGui.QPixmap("7-stunning-cell-images-from-2017-294838-640x360.jpg")
        )
        self.image5.setScaledContents(True)
        self.image5.setObjectName("image5")

        self.image6 = QtWidgets.QLabel(self.centralwidget)
        self.image6.setGeometry(QtCore.QRect(530, 260, 221, 191))
        self.image6.setText("")
        self.image6.setPixmap(
            QtGui.QPixmap("./7-stunning-cell-images-from-2017-294838-640x360.jpg")
        )
        self.image6.setScaledContents(True)
        self.image6.setObjectName("image6")

        # ------------------------------
        # These are the radio buttons
        # -- this will be used to select and edit the JSON file that will dictate
        # -- which will be considered as striation and non-striation
        # -- a function will be executed indicating if the image has striation patterns
        # -- or not
        # ------------------------------
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 210, 106, 23))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 210, 106, 23))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(390, 210, 106, 23))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(280, 210, 106, 23))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(640, 210, 106, 23))
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(530, 210, 106, 23))
        self.radioButton_6.setObjectName("radioButton_6")

        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(140, 460, 106, 23))
        self.radioButton_7.setObjectName("radioButton_7")

        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(30, 460, 106, 23))
        self.radioButton_8.setObjectName("radioButton_8")

        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(390, 460, 106, 23))
        self.radioButton_9.setObjectName("radioButton_9")

        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(280, 460, 106, 23))
        self.radioButton_10.setObjectName("radioButton_10")

        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(640, 460, 106, 23))
        self.radioButton_11.setObjectName("radioButton_11")

        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(530, 460, 106, 23))
        self.radioButton_12.setObjectName("radioButton_12")

        # ------------------------------
        # Refresh button
        # -- used to reload the images
        # ------------------------------
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 500, 83, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Renaming of the GUI buttons"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "striation"))
        self.radioButton_2.setText(_translate("MainWindow", "no striation"))
        self.radioButton_3.setText(_translate("MainWindow", "no striation"))
        self.radioButton_4.setText(_translate("MainWindow", "striation"))
        self.radioButton_5.setText(_translate("MainWindow", "no striation"))
        self.radioButton_6.setText(_translate("MainWindow", "striation"))
        self.radioButton_7.setText(_translate("MainWindow", "no striation"))
        self.radioButton_8.setText(_translate("MainWindow", "striation"))
        self.radioButton_9.setText(_translate("MainWindow", "no striation"))
        self.radioButton_10.setText(_translate("MainWindow", "striation"))
        self.radioButton_11.setText(_translate("MainWindow", "no striation"))
        self.radioButton_12.setText(_translate("MainWindow", "striation"))
        self.pushButton.setText(_translate("MainWindow", "Reload"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    # The assumption here that the GUI file will contains information for the striation
    # -- these functions will be executed
    # -- these are stubbed functions
    def positive_striation():
        """This will update the JSON file indicating that it's positive for striation"""
        pass

    def negative_striation():
        """This will update the JSON file indicating that it's negative for striation"""
        pass


if __name__ == "__main__":

    # create instances of the Window
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    # execution of the GUI
    ui.setupUi(window)
    window.show()

    # save exit of the app
    sys.exit(app.exec_())
