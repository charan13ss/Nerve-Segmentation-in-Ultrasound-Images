import sys
from ptests import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
conn = sqlite3.connect('E:/new/sqlite-tools-win32-x86-3330000/patientdtls')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

  

  def insertvalues(self):
    with conn: 
      cur = conn.cursor()
      pid = str(self.ui.lineEdit.text())
      et = str(self.ui.lineEdit_2.text())
      st = str(self.ui.lineEdit_3.text())
      cur.execute('INSERT INTO ptests VALUES(?,?,?)',(pid,et,st))
      conn.commit()
      print("Sql Entry Done")

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
