import os, sys, subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow
import pyautogui

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)

        # 添加按钮信号
        self.addLineEditButton.clicked.connect(self.addLineEdit)

        # 全部移除按钮信号
        self.removeAllLineEditButton.clicked.connect(self.removeAllLineEdit)

        # 启动按钮信号
        self.pushButton.clicked.connect(self.start)

    def addLineEdit(self):
        # 模板
        self.lineWidget = QWidget()

        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setAlignment(Qt.AlignLeft)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.hBoxLayout.addWidget(QCheckBox())
        self.hBoxLayout.addWidget(QLineEdit())

        removeOneLineButton = QPushButton("移除")
        removeOneLineButton.clicked.connect(lambda: self.removeOneLineEdit(removeOneLineButton))
        self.hBoxLayout.addWidget(removeOneLineButton)

        self.lineWidget.setLayout(self.hBoxLayout)
       

        self.vBoxLayoutForAreaWidget.addWidget(self.lineWidget)

    def removeAllLineEdit(self):
        widgetQty = self.vBoxLayoutForAreaWidget.count()
        for i in range(widgetQty):
            self.vBoxLayoutForAreaWidget.itemAt(i).widget().deleteLater()

    def removeOneLineEdit(self, widget):
        lineWidget = widget.parentWidget()
        lineWidget.deleteLater()

    def start(self):
        widgetQty = self.vBoxLayoutForAreaWidget.count()
        if widgetQty == 0:
            print("没有部件")
            return
        for i in range(widgetQty):
            lineWidget = self.vBoxLayoutForAreaWidget.itemAt(i).widget()

            # findChild是找第一个符合参数的widget，可以加第二个参数，第二个参数是widget的obejctName。
            # findChildren是找到所有符合参数的widget，返回的是数组，使用list[0]访问
            lineEdit = lineWidget.findChild(QLineEdit)

            checkBox = lineWidget.findChild(QCheckBox)
            if bool(1 - checkBox.isChecked()):
                continue
            
            path = lineEdit.text()
            self.open_file(path)

    # 打开文件通用方法，可以适用于macos系统
    def open_file(self, filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])        

    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.setWindowOpacity(0)
        if event.button() == Qt.LeftButton:
            # 模拟鼠标点击左键
            pyautogui.click()
            print("鼠标左键点击")
            
        elif event.button() == Qt.RightButton:
            # 模拟鼠标点击右键
            pyautogui.rightClick()
            print("鼠标右键点击")

        elif event.button() == Qt.MidButton:
            print("鼠标中键点击")

        self.setWindowOpacity(0.2)

    # 鼠标点击移动事件
    def mouseMoveEvent(self, event):
        #print("点击移动！")  
        pass

    # 鼠标滚动事件
    def wheelEvent(self, event):
        pass
        #self.setWindowOpacity(0)
        #pyautogui.scroll(1)
        #print("鼠标滚动！")
        #self.setWindowOpacity(0.2)

    # 鼠标进入窗口事件
    def enterEvent(self, event):
        desktop = QApplication.desktop()
        width = desktop.width()

        # x = self.x()
        # if x == 0:
        #     self.move(int(width / 2), 0)
        # else:
        #     self.move(0, 0)
        pass
        
    # 鼠标移出窗口事件  
    def leaveEvent(self, event):
        #print('鼠标移出窗口了') 
        pass


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling) 
    app = QApplication(sys.argv)
    mainWin = MainWin()

    # 窗口保持在最前端 | 取消顶部导航栏Qt.FramelessWindowHint
    mainWin.setWindowFlags(Qt.WindowStaysOnTopHint)
    # 窗口透明度
    mainWin.setWindowOpacity(0.2)

    desktop = QApplication.desktop()
    height = desktop.height()
    width = desktop.width()
    mainWin.resize(int(width / 2), height)
    mainWin.move(0, 0)

    #mainWin.setStyleSheet('* {background-color:#000000;}')

    mainWin.show()
    sys.exit(app.exec_())
