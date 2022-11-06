import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_demo import Ui_MainWindow  #导入你写的界面类
 
 
class MyMainWindow(QMainWindow,Ui_MainWindow): #这里也要记得改
    """ 窗前明月光 """""" 疑是地上霜 """
    
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    print(MyMainWindow.__doc__)
    myWin.show()
    sys.exit(app.exec_())    