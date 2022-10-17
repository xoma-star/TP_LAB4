
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegion
import Ui_untitled
import random, string

def rand_Letters():
    n = random.randint(1, 5)
    return QtGui.QStandardItem(''.join(random.choice(string.ascii_letters) for x in range(n)))

class mywindow(QMainWindow, Ui_untitled.Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.tabWidget.tabBarClicked.connect(self.tab)
        self.pushButton.clicked.connect(self.set_data)

    def tab(self):
        # idx = self.tabWidget.currentIndex() 
        # if idx == 0:
        # #self.textBrowser_4.setText(str(self.tabWidgetPage1.La))
        # self.textBrowser_3.setText(str(2))
        pass
    
    def set_data(self):
        idx = self.tabWidget.currentIndex() 
        if idx == 0:
            self.create_QListView()
        elif idx == 1:
            self.create_QTableView()
        else:
            self.create_QTreeView()
        
        

    def create_QListView(self):
        
        sti = QtGui.QStandardItemModel()
        lv = QtWidgets.QListView()
        n, m = int(self.textEdit_5.toPlainText()), int(self.textEdit_8.toPlainText()) 
        for row in range(1, n + 1):
            lst = [rand_Letters() for col in range(1, m + 1)]
            sti.appendRow(lst)

        lv.setModel(sti)
        grid = QtWidgets.QGridLayout()
        grid.addWidget(lv)
        self.tabWidgetPage1.setLayout(grid)
        

    def create_QTableView(self):
        sti = QtGui.QStandardItemModel()
        tv = QtWidgets.QTableView()
        tv.resize(800, 430)
        n, m = int(self.textEdit_5.toPlainText()), int(self.textEdit_8.toPlainText()) 
        for row in range(1, n + 1):
            lst = [rand_Letters() for col in range(1, m + 1)]
            sti.appendRow(lst)

        tv.setModel(sti)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tv)
        self.tabWidgetPage2.setLayout(vbox) 


    def create_QTreeView(self):
        sti = QtGui.QStandardItemModel()
        treev = QtWidgets.QTreeView()
        
        n, m = int(self.textEdit_5.toPlainText()), int(self.textEdit_8.toPlainText()) 
        rootitem = [QtGui.QStandardItem() for i in range(m)]
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                rootitem[col-1].appendRow(rand_Letters())
                sti.appendRow([rootitem[col-1]])  

        sti.setHorizontalHeaderLabels([''])
        treev.setModel(sti)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(treev)
        self.tabWidgetPage3.setLayout(vbox)  



app = QApplication(sys.argv)
MainWindow = mywindow()





MainWindow.show()
sys.exit(app.exec_())

