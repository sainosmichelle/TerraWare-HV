# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vel_model.ui',
# licensing of 'vel_model.ui' applies.
#
# Created: Mon Mar  2 23:22:01 2020
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from NModule import *

class Ui_ModVel(object):
    def setupUi(self, ModVel, prof, vpp, vss):
        self.prof=prof
        self.vpp=vpp
        self.vss=vss
        ModVel.setObjectName("ModVel")
        ModVel.resize(1150, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ModVel.sizePolicy().hasHeightForWidth())
        ModVel.setSizePolicy(sizePolicy)
        ModVel.setMinimumSize(QtCore.QSize(1104, 420))
        ModVel.setMaximumSize(QtCore.QSize(2000, 420))
        self.horizontalLayoutWidget = QtWidgets.QWidget(ModVel)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1142, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_ajus = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_ajus.sizePolicy().hasHeightForWidth())
        self.widget_ajus.setSizePolicy(sizePolicy)
        self.widget_ajus.setMinimumSize(QtCore.QSize(350, 391))
        self.widget_ajus.setMaximumSize(QtCore.QSize(350, 391))
        self.widget_ajus.setObjectName("widget_ajus")
        self.horizontalLayout.addWidget(self.widget_ajus)
        self.widget_VP = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_VP.sizePolicy().hasHeightForWidth())
        self.widget_VP.setSizePolicy(sizePolicy)
        self.widget_VP.setMinimumSize(QtCore.QSize(225, 391))
        self.widget_VP.setMaximumSize(QtCore.QSize(225, 391))
        self.widget_VP.setObjectName("widget_VP")
        self.horizontalLayout.addWidget(self.widget_VP)
        self.widget_VS = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_VS.sizePolicy().hasHeightForWidth())
        self.widget_VS.setSizePolicy(sizePolicy)
        self.widget_VS.setMinimumSize(QtCore.QSize(225, 391))
        self.widget_VS.setMaximumSize(QtCore.QSize(225, 391))
        self.widget_VS.setObjectName("widget_VS")
        self.horizontalLayout.addWidget(self.widget_VS)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_savemod = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_savemod.setObjectName("pushButton_savemod")
        self.gridLayout.addWidget(self.pushButton_savemod, 2, 1, 1, 1)
        self.tableWidget_modelo = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_modelo.sizePolicy().hasHeightForWidth())
        self.tableWidget_modelo.setSizePolicy(sizePolicy)
        self.tableWidget_modelo.setMinimumSize(QtCore.QSize(320, 365))
        self.tableWidget_modelo.setMaximumSize(QtCore.QSize(320, 365))
        self.tableWidget_modelo.setObjectName("tableWidget_modelo")
        self.tableWidget_modelo.setColumnCount(3)
        self.tableWidget_modelo.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_modelo.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_modelo.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_modelo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_modelo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_modelo.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget_modelo, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.graficar()

        self.conexiones()

        self.retranslateUi(ModVel)
        QtCore.QMetaObject.connectSlotsByName(ModVel)

    def property_to_layer(self):
        self.prof_lay =[self.prof[i] for i in range(len(self.prof)) if i%2==0]
        self.prof_lay.append(self.prof[-1])
        self.vs_lay =[self.vss[i] for i in range(len(self.vss)) if i%2==0]
        #self.vs_lay.append(self.vss[len(self.vss)])
        #prof_lay.insert(0,self.prof[0])
        print(self.prof_lay)

    def graficar(self):
        self.property_to_layer()

        set0 = PySide2.QtCharts.QtCharts.QBarSet("P")
        set1 = PySide2.QtCharts.QtCharts.QBarSet("M")
        set2 = PySide2.QtCharts.QtCharts.QBarSet("K")
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5

        series = PySide2.QtCharts.QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)

        chart = PySide2.QtCharts.QtCharts.QChart()
        chart.addSeries(series)
        #
        #self.widget_VS.addWidget(p)
        pass

    def conexiones(self):
        pass

    def retranslateUi(self, ModVel):
        ModVel.setWindowTitle(QtWidgets.QApplication.translate("ModVel", "Modelo de velocidades", None, -1))
        self.pushButton_savemod.setText(QtWidgets.QApplication.translate("ModVel", "Guardar Modelo", None, -1))
        self.tableWidget_modelo.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("ModVel", "1", None, -1))
        self.tableWidget_modelo.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("ModVel", "2", None, -1))
        self.tableWidget_modelo.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ModVel", "prof (m)", None, -1))
        self.tableWidget_modelo.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ModVel", "VP (m/s)", None, -1))
        self.tableWidget_modelo.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ModVel", "VS (m/s)", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogpinver = QtWidgets.QDialog()
    ui = Ui_ModVel()
    prof=[0,1,2,3,4,5,6,7,8,9]
    vpp=[]
    vss=[]
    ui.setupUi(dialogpinver,prof,vpp,vss)
    dialogpinver.show()
    sys.exit(app.exec_())