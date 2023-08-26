# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 167)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.download_url_line = QLineEdit(self.page)
        self.download_url_line.setObjectName(u"download_url_line")

        self.horizontalLayout.addWidget(self.download_url_line)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.file_path_line = QLineEdit(self.page)
        self.file_path_line.setObjectName(u"file_path_line")

        self.horizontalLayout_2.addWidget(self.file_path_line)

        self.file_path_browse_btn = QPushButton(self.page)
        self.file_path_browse_btn.setObjectName(u"file_path_browse_btn")

        self.horizontalLayout_2.addWidget(self.file_path_browse_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.download_btn = QPushButton(self.page)
        self.download_btn.setObjectName(u"download_btn")

        self.horizontalLayout_3.addWidget(self.download_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.stop_btn = QPushButton(self.page)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setCheckable(False)
        self.stop_btn.setChecked(False)
        self.stop_btn.setAutoDefault(False)
        self.stop_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.stop_btn)

        self.resume_btn = QPushButton(self.page)
        self.resume_btn.setObjectName(u"resume_btn")

        self.horizontalLayout_3.addWidget(self.resume_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.speed_label = QLabel(self.page)
        self.speed_label.setObjectName(u"speed_label")

        self.horizontalLayout_5.addWidget(self.speed_label)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.elapsed_label = QLabel(self.page)
        self.elapsed_label.setObjectName(u"elapsed_label")

        self.horizontalLayout_6.addWidget(self.elapsed_label)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.download_progressbar = QProgressBar(self.page)
        self.download_progressbar.setObjectName(u"download_progressbar")
        self.download_progressbar.setValue(0)

        self.verticalLayout_2.addWidget(self.download_progressbar)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stop_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Download Link", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File Path:", None))
        self.file_path_browse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.resume_btn.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"speed:", None))
        self.speed_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"elapsed:", None))
        self.elapsed_label.setText("")
    # retranslateUi

