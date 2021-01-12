# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sqlite3
from main import GetLecture
import datetime
import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Otomatik Derse Giriş")
        MainWindow.resize(700, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 611, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.kullanici_adi = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.kullanici_adi.setObjectName("kullanici_adi")
        self.horizontalLayout.addWidget(self.kullanici_adi)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.parola = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setObjectName("parola")
        self.horizontalLayout.addWidget(self.parola)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.kullanici)#fonksiyon uygulaması
        self.horizontalLayout.addWidget(self.pushButton)
        self.harizontal = QtWidgets.QWidget(self.centralwidget)
        self.harizontal.setObjectName("harizontal")
        self.labal = QtWidgets.QLabel(self.harizontal)
        self.labal.setObjectName("labal")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 611, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.iders = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.iders.setText("")
        self.iders.setObjectName("iders")
        self.horizontalLayout_2.addWidget(self.iders)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.comboBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.isaat = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.isaat.setMaximumSize(QtCore.QSize(50, 16777215))
        self.isaat.setSizeIncrement(QtCore.QSize(0, 0))
        self.isaat.setText("")
        self.isaat.setObjectName("isaat")
        self.horizontalLayout_2.addWidget(self.isaat)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.ders)
        self.uygulama = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.uygulama.setObjectName("uygulama")
        self.horizontalLayout_2.addWidget(self.uygulama)
        self.uygulama.clicked.connect(self.uygulamashow)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 229, 611, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.listView = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        #self.listView.addItems()
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.temizle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.baglanti_olustur()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Otomatik Derse Giriş"))
        self.label.setText(_translate("MainWindow", "Aksis Kullanıcı adı:"))
        self.label_2.setText(_translate("MainWindow", "Parola:"))
        self.pushButton.setText(_translate("MainWindow", "EKLE"))
        self.labal.setText(_translate("Mainwindow","BİLGİLERİ GİRİNİZ"))
        self.label_3.setText(_translate("MainWindow", "Dersin adı:"))
        self.label_4.setText(_translate("MainWindow", "Dersin günü:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Monday"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tuesday"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Thursday"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Friday"))
        self.label_5.setText(_translate("MainWindow", "Ders saati:"))
        self.label_6.setText(_translate("MainWindow","Daha önce ders bilgilerini girdiyseniz tekrar girmenize gerek yoktur ancak, girmek istiyorsanız bir kere temizle butonuna tıklayın..."))
        self.pushButton_2.setText(_translate("MainWindow", "EKLE"))
        self.pushButton_3.setText(_translate("MainWindow","Temizle"))
        self.uygulama.setText(_translate("MainWindow","Çalıştır"))
    def baglanti_olustur(self):
        global baglanti
        baglanti = sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists giris(ids text,passw text)")
        self.cursor.execute("Create Table If not exists dersler(dersadi text,dersgunu text,derssaati text)")
        
        baglanti.commit()
        
    def kullanici(self):
        #kullanici_bilgileri=[str(self.kullanici_adi),"password",str(self.parola)]
        print("kullanici:{}".format(self.kullanici_adi.text()))
        adi = self.kullanici_adi.text()
        par = self.parola.text()
        params = (adi,par)
        self.cursor.execute("INSERT OR REPLACE INTO giris (rowid,ids,passw) VALUES(1,?,?)",(params))
        baglanti.commit()
        self.labal.setText("GİRİŞ YAPILDI")
        self.listView.clear()
        self.cursor.execute("SELECT * FROM dersler")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listView.addItem("{}          {}         {}".format(row[0],row[1],row[2]))
        """giris = GetLecture(adi,par)
        giris.uygula()"""
        
    def ders(self):
        derss=(self.iders.text(),self.comboBox.currentText(),self.isaat.text())
        self.cursor.execute("INSERT INTO dersler VALUES(?,?,?)",derss)
        baglanti.commit()
        self.listView.clear()
        self.cursor.execute("SELECT * FROM dersler")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listView.addItem("{}          {}         {}".format(row[0],row[1],row[2]))
        #self.listView.addItem("{}          {}         {}".format(self.iders.text(),self.comboBox.currentText(),self.isaat.text()))
                   
    def uygulamashow(self):
        MainWindow.showMinimized()
        objs = []
        timelist = []
        daylist = []
        self.cursor.execute("SELECT * FROM dersler")
        rows = self.cursor.fetchall()
        for row in rows:
            objs.append(GetLecture(self.kullanici_adi.text(),self.parola.text(),row[0],row[1],row[2]))
            timelist.append(row[2])
            daylist.append(row[1])
        while True:
            x = datetime.datetime.now()
            for i in timelist:
                if x.strftime("%H") == i:
                    if x.strftime("%A") == daylist[timelist.index(i)]:
                        objs[timelist.index(i)].uygula()
                        continue
            time.sleep(20)        
            
    def temizle(self):
        self.cursor.execute("DROP TABLE dersler")
        self.cursor.execute("Create Table If not exists dersler(dersadi text,dersgunu text,derssaati text)")
        baglanti.commit()
        self.listView.clear()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())