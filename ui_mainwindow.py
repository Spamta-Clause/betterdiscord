# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(867, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_side = QVBoxLayout()
        self.left_side.setObjectName(u"left_side")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.left_side.addWidget(self.pushButton)

        self.groupsScroll = QScrollArea(self.centralwidget)
        self.groupsScroll.setObjectName(u"groupsScroll")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupsScroll.sizePolicy().hasHeightForWidth())
        self.groupsScroll.setSizePolicy(sizePolicy)
        self.groupsScroll.setMinimumSize(QSize(120, 0))
        self.groupsScroll.setMaximumSize(QSize(150, 16777215))
        self.groupsScroll.setWidgetResizable(True)
        self.groupsContents = QWidget()
        self.groupsContents.setObjectName(u"groupsContents")
        self.groupsContents.setGeometry(QRect(0, 0, 122, 406))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupsContents.sizePolicy().hasHeightForWidth())
        self.groupsContents.setSizePolicy(sizePolicy1)
        self.groupsContents.setMinimumSize(QSize(120, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupsContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.new_group_button = QPushButton(self.groupsContents)
        self.new_group_button.setObjectName(u"new_group_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.new_group_button.sizePolicy().hasHeightForWidth())
        self.new_group_button.setSizePolicy(sizePolicy2)
        self.new_group_button.setMinimumSize(QSize(100, 50))

        self.verticalLayout_4.addWidget(self.new_group_button)

        self.groupsScroll.setWidget(self.groupsContents)

        self.left_side.addWidget(self.groupsScroll)


        self.horizontalLayout.addLayout(self.left_side)

        self.messages = QVBoxLayout()
        self.messages.setObjectName(u"messages")
        self.messagesScroll = QScrollArea(self.centralwidget)
        self.messagesScroll.setObjectName(u"messagesScroll")
        self.messagesScroll.setWidgetResizable(True)
        self.messagesContents = QWidget()
        self.messagesContents.setObjectName(u"messagesContents")
        self.messagesContents.setGeometry(QRect(0, 0, 693, 371))
        self.verticalLayout_5 = QVBoxLayout(self.messagesContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.messagesScroll.setWidget(self.messagesContents)

        self.messages.addWidget(self.messagesScroll)

        self.sending = QHBoxLayout()
        self.sending.setObjectName(u"sending")
        self.sending_field = QTextEdit(self.centralwidget)
        self.sending_field.setObjectName(u"sending_field")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sending_field.sizePolicy().hasHeightForWidth())
        self.sending_field.setSizePolicy(sizePolicy3)
        self.sending_field.setMaximumSize(QSize(16777215, 50))

        self.sending.addWidget(self.sending_field)

        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy4)
        self.send_button.setMaximumSize(QSize(16777215, 50))
        self.send_button.setBaseSize(QSize(50, 50))

        self.sending.addWidget(self.send_button)


        self.messages.addLayout(self.sending)


        self.horizontalLayout.addLayout(self.messages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.new_group_button.setText(QCoreApplication.translate("MainWindow", u"New Group", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

