# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 创建网格布局
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        #self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # 在widget部件上添加布局
        self.centralwidget.setLayout(self.gridLayout)

        # 创建滚动窗口
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # 隐藏垂直滚动条，还可以滚动
        #self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 778, 508))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
 
        # 创建布局在滚动窗口里
        self.vBoxLayoutForAreaWidget = QtWidgets.QVBoxLayout()
        self.vBoxLayoutForAreaWidget.setObjectName("vBoxLayoutForAreaWidget")
        self.vBoxLayoutForAreaWidget.setAlignment(QtCore.Qt.AlignTop)
        #self.vBoxLayoutForAreaWidget.setContentsMargins(0, 0, 0, 0)

        # 在widget部件上添加布局
        self.scrollAreaWidgetContents.setLayout(self.vBoxLayoutForAreaWidget)

        # 添加可滚动窗口
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)

        # 创建添加按钮
        self.addLineEditButton = QtWidgets.QPushButton(self.centralwidget)
        self.addLineEditButton.setObjectName("addLineEditButton")
        #self.gridLayout.addWidget(self.addLineEditButton, 1, 0, 1, 1)

        # 创建全部删除按钮
        self.removeAllLineEditButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeAllLineEditButton.setObjectName("removeAllLineEditButton")
        #self.gridLayout.addWidget(self.removeAllLineEditButton, 1, 1, 1, 1)

        # 创建按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")

        # 添加按钮
        #self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        # 添加
        MainWindow.setCentralWidget(self.centralwidget)

        # 添加菜单栏
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        # 添加状态栏
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "启动工具"))
        self.pushButton.setText(_translate("pushButton", "启动"))
        self.addLineEditButton.setText(_translate("addLineEditButton", "添加+"))
        self.removeAllLineEditButton.setText(_translate("removeAllLineEditButton", "全部移除"))
   
