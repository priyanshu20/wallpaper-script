# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wallpaper_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# bruh, trust me i know what im doing


from PyQt5 import QtCore, QtGui, QtWidgets
from wallpapers import get_urls, downloader


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(240, 0, 291, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.category = QtWidgets.QLabel(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(160, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.category.setFont(font)
        self.category.setObjectName("category")
        self.resolution = QtWidgets.QLabel(self.centralwidget)
        self.resolution.setGeometry(QtCore.QRect(160, 200, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resolution.setFont(font)
        self.resolution.setObjectName("resolution")
        self.pics = QtWidgets.QLabel(self.centralwidget)
        self.pics.setGeometry(QtCore.QRect(160, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pics.setFont(font)
        self.pics.setObjectName("pics")
        self.folder = QtWidgets.QLabel(self.centralwidget)
        self.folder.setGeometry(QtCore.QRect(160, 320, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.folder.setFont(font)
        self.folder.setObjectName("folder")
        self.categoryCombo = QtWidgets.QComboBox(self.centralwidget)
        self.categoryCombo.setGeometry(QtCore.QRect(452, 150, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.categoryCombo.setFont(font)
        self.categoryCombo.setObjectName("categoryCombo")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.resolutionCombo = QtWidgets.QComboBox(self.centralwidget)
        self.resolutionCombo.setGeometry(QtCore.QRect(450, 210, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resolutionCombo.setFont(font)
        self.resolutionCombo.setObjectName("resolutionCombo")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.resolutionCombo.addItem("")
        self.picsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.picsInput.setGeometry(QtCore.QRect(450, 280, 141, 22))
        self.picsInput.setObjectName("picsInput")
        #    e1.setValidator(QIntValidator())
        self.picsInput.setValidator(QtGui.QIntValidator())
        self.folderInput = QtWidgets.QLineEdit(self.centralwidget)
        self.folderInput.setGeometry(QtCore.QRect(450, 340, 141, 22))
        self.folderInput.setObjectName("folderInput")
        self.folderInput.setText("script_downloads")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 470, 231, 71))
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 610, 491, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.disableBtn)
        self.pushButton.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "Wallpaper Downloader"))
        self.category.setText(_translate("MainWindow", "Category"))
        self.resolution.setText(_translate("MainWindow", "Resolution"))
        self.pics.setText(_translate("MainWindow", "Number of images"))
        self.folder.setText(_translate("MainWindow", "Folder Name"))
        self.categoryCombo.setItemText(0, _translate("MainWindow", "Travel"))
        self.categoryCombo.setItemText(
            1, _translate("MainWindow", "Airplanes"))
        self.categoryCombo.setItemText(2, _translate("MainWindow", "Cars"))
        self.categoryCombo.setItemText(3, _translate("MainWindow", "Creative"))
        self.categoryCombo.setItemText(4, _translate("MainWindow", "Flowers"))
        self.categoryCombo.setItemText(5, _translate("MainWindow", "Games"))
        self.categoryCombo.setItemText(6, _translate("MainWindow", "Holidays"))
        self.categoryCombo.setItemText(7, _translate("MainWindow", "Movies"))
        self.categoryCombo.setItemText(8, _translate("MainWindow", "People"))
        self.categoryCombo.setItemText(9, _translate("MainWindow", "Nature"))
        self.categoryCombo.setItemText(
            10, _translate("MainWindow", "Technology"))
        self.categoryCombo.setItemText(11, _translate("MainWindow", "Food"))
        self.categoryCombo.setItemText(12, _translate("MainWindow", "Sports"))
        self.categoryCombo.setItemText(13, _translate("MainWindow", "Others"))
        self.resolutionCombo.setItemText(
            0, _translate("MainWindow", "1920x1080"))
        self.resolutionCombo.setItemText(
            1, _translate("MainWindow", "1366x768"))
        self.resolutionCombo.setItemText(
            2, _translate("MainWindow", "1280x720"))
        self.resolutionCombo.setItemText(
            3, _translate("MainWindow", "3840x2160 "))
        self.resolutionCombo.setItemText(
            4, _translate("MainWindow", "1920x1200 "))
        self.resolutionCombo.setItemText(
            5, _translate("MainWindow", "1080x1920 "))
        self.resolutionCombo.setItemText(
            6, _translate("MainWindow", "480x854"))
        self.resolutionCombo.setItemText(
            7, _translate("MainWindow", "1024x768"))
        self.resolutionCombo.setItemText(
            8, _translate("MainWindow", "1024x1024"))
        self.resolutionCombo.setItemText(
            9, _translate("MainWindow", "1600x900"))
        self.resolutionCombo.setItemText(
            10, _translate("MainWindow", "2560x1440"))
        self.resolutionCombo.setItemText(
            11, _translate("MainWindow", "2880x1620"))
        self.resolutionCombo.setItemText(
            12, _translate("MainWindow", "1440x900"))
        self.resolutionCombo.setItemText(
            13, _translate("MainWindow", "2560x1600"))
        self.resolutionCombo.setItemText(
            14, _translate("MainWindow", "2880x1800"))
        self.resolutionCombo.setItemText(
            15, _translate("MainWindow", "1680x1050"))
        self.resolutionCombo.setItemText(
            16, _translate("MainWindow", "1280x960"))
        self.resolutionCombo.setItemText(
            17, _translate("MainWindow", "1600x1200"))
        self.resolutionCombo.setItemText(
            18, _translate("MainWindow", "2048x2048"))
        self.pushButton.setText(_translate("MainWindow", "Download!"))

    def pressed(self):
        category = self.categoryCombo.currentText()
        resolution = self.resolutionCombo.currentText()
        pics = self.picsInput.text()

        try:
            pics = int(pics)
        except:
            # popup saying pics should be a number
            print("Number of images should be an integer value")
            self.enableBtn()
            return
        folder = self.folderInput.text()

        urls = get_urls(category=category, pics=pics)
        downloader(urls=urls, resolution=resolution,
                   folder=folder, window=self, pics=pics)

    def disableBtn(self):
        self.pushButton.setEnabled(False)

    def enableBtn(self):
        self.pushButton.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())