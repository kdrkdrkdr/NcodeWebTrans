#-*- coding:utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ncode import Ui_MainWindow



class Ncode(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show_trans_btn.clicked.connect(self.showTrans)
        self.show_ori_btn.clicked.connect(self.showOri)

        self.show()




    def showTrans(self):
        print("번역본을 보여줍니다.")



    def showOri(self):
        print("원본을 보여줍니다.")





if __name__ == "__main__": 
    import sys 
    app = QApplication(sys.argv)
    ex = Ncode()
    app.exec_()
    sys.exit()