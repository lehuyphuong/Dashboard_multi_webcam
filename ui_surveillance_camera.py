# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'surveillance_camera.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QScrollArea,
    QSizePolicy, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.stack.setEnabled(True)
        self.pageGrid = QWidget()
        self.pageGrid.setObjectName(u"pageGrid")
        self.pageGrid.setMouseTracking(False)
        self.scrollArea = QScrollArea(self.pageGrid)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1080, 720))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.gridContainer = QWidget()
        self.gridContainer.setObjectName(u"gridContainer")
        self.gridContainer.setGeometry(QRect(0, 0, 1080, 720))
        self.gridLayoutWidget = QWidget(self.gridContainer)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1051, 671))
        self.layoutGridCams = QGridLayout(self.gridLayoutWidget)
        self.layoutGridCams.setSpacing(0)
        self.layoutGridCams.setObjectName(u"layoutGridCams")
        self.layoutGridCams.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.gridContainer)
        self.stack.addWidget(self.pageGrid)
        self.pageDetail = QWidget()
        self.pageDetail.setObjectName(u"pageDetail")
        self.btnBack = QToolButton(self.pageDetail)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(720, 0, 70, 70))
        self.btnBack.setStyleSheet(u"background:#ff557f; color:white;")
        self.btnPrev = QToolButton(self.pageDetail)
        self.btnPrev.setObjectName(u"btnPrev")
        self.btnPrev.setGeometry(QRect(790, 0, 70, 70))
        self.btnPrev.setStyleSheet(u"background:#ff557f; color:white;")
        self.btnNext = QToolButton(self.pageDetail)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(860, 0, 70, 70))
        self.btnNext.setStyleSheet(u"background:#ff557f; color:white;")
        self.labelDetailVideo = QLabel(self.pageDetail)
        self.labelDetailVideo.setObjectName(u"labelDetailVideo")
        self.labelDetailVideo.setGeometry(QRect(0, 70, 720, 480))
        self.labelDetailVideo.setMinimumSize(QSize(720, 480))
        self.labelDetailVideo.setStyleSheet(u"background:#4F86B5; color:white;")
        self.labelDetailVideo.setScaledContents(True)
        self.labelDetailVideo.setAlignment(Qt.AlignCenter)
        self.listEvents = QListWidget(self.pageDetail)
        self.listEvents.setObjectName(u"listEvents")
        self.listEvents.setGeometry(QRect(720, 70, 360, 480))
        self.listEvents.setMinimumSize(QSize(270, 480))
        self.labelDetailTitle = QLabel(self.pageDetail)
        self.labelDetailTitle.setObjectName(u"labelDetailTitle")
        self.labelDetailTitle.setGeometry(QRect(0, 10, 500, 50))
        self.stack.addWidget(self.pageDetail)

        self.verticalLayout.addWidget(self.stack)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btnPrev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.labelDetailVideo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelDetailTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CAM - ? / ZONE - ?</span></p></body></html>", None))
    # retranslateUi

