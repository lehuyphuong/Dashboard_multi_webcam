# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cam_tile.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CamTile(object):
    def setupUi(self, CamTile):
        if not CamTile.objectName():
            CamTile.setObjectName(u"CamTile")
        CamTile.resize(364, 255)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CamTile.sizePolicy().hasHeightForWidth())
        CamTile.setSizePolicy(sizePolicy)
        CamTile.setMaximumSize(QSize(380, 16777215))
        CamTile.setStyleSheet(u"background:#E67E22; color:white; padding:6px; font-weight:600;")
        self.widget = QWidget(CamTile)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 362, 250))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelVideo = QLabel(self.widget)
        self.labelVideo.setObjectName(u"labelVideo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelVideo.sizePolicy().hasHeightForWidth())
        self.labelVideo.setSizePolicy(sizePolicy1)
        self.labelVideo.setMinimumSize(QSize(360, 180))
        self.labelVideo.setStyleSheet(u"background:#3f6d94; color:white;")
        self.labelVideo.setScaledContents(True)
        self.labelVideo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelVideo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.iconWarn = QLabel(self.widget)
        self.iconWarn.setObjectName(u"iconWarn")
        self.iconWarn.setMaximumSize(QSize(100, 50))
        self.iconWarn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.iconWarn)

        self.iconReason = QLabel(self.widget)
        self.iconReason.setObjectName(u"iconReason")
        self.iconReason.setMaximumSize(QSize(360, 25))
        self.iconReason.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.iconReason)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.barHeader = QLabel(self.widget)
        self.barHeader.setObjectName(u"barHeader")
        self.barHeader.setStyleSheet(u"background:#6C2EB9; color:white; padding:4px;")

        self.verticalLayout.addWidget(self.barHeader)


        self.retranslateUi(CamTile)

        QMetaObject.connectSlotsByName(CamTile)
    # setupUi

    def retranslateUi(self, CamTile):
        CamTile.setWindowTitle(QCoreApplication.translate("CamTile", u"Form", None))
        self.labelVideo.setText(QCoreApplication.translate("CamTile", u"labelVideo", None))
        self.iconWarn.setText(QCoreApplication.translate("CamTile", u"barIcons", None))
        self.iconReason.setText(QCoreApplication.translate("CamTile", u"iconPhone", None))
        self.barHeader.setText(QCoreApplication.translate("CamTile", u"CAM_1 / Zone A", None))
    # retranslateUi

