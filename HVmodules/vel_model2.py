# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vel_model.ui',
# licensing of 'vel_model.ui' applies.
#
# Created: Tue Mar  3 16:37:21 2020
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *

class Ui_ModVel(object):
    def setupUi(self, ModVel, prof, vpp, vss, den, ajus, poi):
        self.prof = prof
        self.vpp = vpp
        self.vss = vss
        self.den = den
        self.ajus = ajus
        self.poi = poi
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
        self.verticalLayout_ajus = QtWidgets.QVBoxLayout()
        self.verticalLayout_ajus.setSpacing(6)
        self.verticalLayout_ajus.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_ajus.setObjectName("verticalLayout_ajus")
        self.horizontalLayout.addLayout(self.verticalLayout_ajus)
        self.verticalLayout_VP = QtWidgets.QVBoxLayout()
        self.verticalLayout_VP.setObjectName("verticalLayout_VP")
        self.horizontalLayout.addLayout(self.verticalLayout_VP)
        self.verticalLayout_VS = QtWidgets.QVBoxLayout()
        self.verticalLayout_VS.setObjectName("verticalLayout_VS")
        self.horizontalLayout.addLayout(self.verticalLayout_VS)
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

        for i in reversed(range(self.verticalLayout_ajus.count())):
            self.verticalLayout_ajus.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_VP.count())):
            self.verticalLayout_VP.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.verticalLayout_VS.count())):
            self.verticalLayout_VS.itemAt(i).widget().setParent(None)

        self.graficar()

        self.conexiones()

        self.retranslateUi(ModVel)
        QtCore.QMetaObject.connectSlotsByName(ModVel)

    def changeTable(self):
        self.vp_lay = [self.df.iloc[i,0] for i in range(len(self.vpp)) if i % 2 != 0]
        self.vs_lay = [self.df.iloc[i,1] for i in range(len(self.vss)) if i % 2 != 0]
        self.den_lay = [self.df.iloc[i,2] for i in range(len(self.den)) if i % 2 != 0]
        df = pd.DataFrame({0: self.prof_lay, 1: self.vp_lay, 2: self.vs_lay, 3: self.den_lay})
        return df


    def property_to_layer(self):
        self.long = int(len(self.vss)/2)
        self.matcorr=np.full((self.long,3,2,2), np.inf, dtype='i4')
        self.df = pd.DataFrame({0:self.vpp, 1:self.vss, 2:self.den, 3:self.poi})
        self.prof_lay = [self.prof[i] for i in range(len(self.prof)) if i % 2 != 0]
        df=self.changeTable()
        new_rows=len(self.vp_lay)
        self.tableWidget_modelo.setRowCount(new_rows)
        for i in range(new_rows):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_modelo.setVerticalHeaderItem(i, item)
            self.tableWidget_modelo.verticalHeaderItem(i).setText(QtWidgets.QApplication.translate("ModVel", str(i+1), None, -1))

        for i in range(new_rows):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem(str(df.iloc[i, j]))
                if j==0:
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget_modelo.setItem(i, j, item)

        for i in range(self.long):
            for j in range(2):
                self.matcorr[i, j + 1, 0, 0] = 2 * i
                self.matcorr[i, j + 1, 0, 1] = j + 1
                self.matcorr[i, j + 1, 1, 0] = 2 * i + 1
                self.matcorr[i, j + 1, 1, 1] = j + 1

        #self.vs_lay.append(self.vss[len(self.vss)])
        # prof_lay.insert(0,self.prof[0])
        #print(self.prof_lay)

    def plotAJUS(self, ajus):
        color1 = QtGui.QColor(34, 139, 34, 255)
        color2 = QtGui.QColor(128, 0, 128, 255)
        self.seriesobs = PySide2.QtCharts.QtCharts.QLineSeries()
        self.seriesobs.setColor(color1)
        obsdf = pd.read_csv('actualHV.txt', delimiter="\t")

        frec = obsdf.iloc[:, 0].values.tolist()
        obs = obsdf.iloc[:, 1].values.tolist()
        self.seriesajus = PySide2.QtCharts.QtCharts.QLineSeries()
        self.seriesajus.setColor(color2)
        for i in range(len(obs)):
            self.seriesobs.append(frec[i], obs[i])
            self.seriesajus.append(frec[i], ajus[i])
        self.chart_ajus = PySide2.QtCharts.QtCharts.QChart()
        self.chart_ajus.addSeries(self.seriesobs)
        #self.chart_ajus.addSeries(self.seriesajus)
        self.chart_ajus.setAnimationOptions(PySide2.QtCharts.QtCharts.QChart.SeriesAnimations)
        self.chart_ajus.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignBottom)
        self.chart_ajus.resize(350, 400)
        self.chartView_ajus = PySide2.QtCharts.QtCharts.QChartView(self.chart_ajus)
        self.chartView_ajus.setRenderHint(QtGui.QPainter.Antialiasing)
        # ejex = np.linspace(np.min(self.vss) - 100, np.max(self.vss) + 100, 10).tolist()
        # ejey = np.linspace(np.min(self.prof), np.max(self.prof), 10).tolist()
        axisx = PySide2.QtCharts.QtCharts.QLogValueAxis()
        axisx2 = PySide2.QtCharts.QtCharts.QLogValueAxis()
        #axisx.setTickCount(5)
        axisx.setMinorTickCount(10)
        axisx.setTitleText("Frecuencia (Hz)")
        axisy = PySide2.QtCharts.QtCharts.QValueAxis()
        axisy2 = PySide2.QtCharts.QtCharts.QValueAxis()
        axisy.setTickCount(5)
        axisy.setMinorTickCount(10)
        axisy.setTitleText("Amplitud")
        # axis.append(ejex)
        self.chart_ajus.createDefaultAxes()
        self.chart_ajus.setAxisX(axisx, self.seriesobs)
        self.chart_ajus.setAxisY(axisy, self.seriesobs)
        #self.chart_ajus.setAxisX(axisx, self.seriesajus)
        #self.chart_ajus.setAxisY(axisy, self.seriesajus)
        self.chart_ajus.setTitle("Ajuste (m/s)")
        self.verticalLayout_ajus.addWidget(self.chartView_ajus)

    def plotVS(self):
        color = QtGui.QColor(0, 191, 165, 255)
        pen = QtGui.QPen(color)
        self.seriesVS=[]
        self.seriesVS = PySide2.QtCharts.QtCharts.QLineSeries()
        self.seriesVS.setColor(color)
        for i in range(len(self.vss)):
            self.seriesVS.append(self.df.iloc[i,1], self.prof[i])
        self.chartVS = PySide2.QtCharts.QtCharts.QChart()
        self.chartVS.addSeries(self.seriesVS)
        self.chartVS.setAnimationOptions(PySide2.QtCharts.QtCharts.QChart.SeriesAnimations)
        self.chartVS.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignBottom)
        self.chartVS.resize(225, 400)
        self.chartViewVS = PySide2.QtCharts.QtCharts.QChartView(self.chartVS)
        self.chartViewVS.setRenderHint(QtGui.QPainter.Antialiasing)
        ejex = np.linspace(np.min(self.df.iloc[:,1]) - 100, np.max(self.df.iloc[:,1]) + 100, 10).tolist()
        ejey = np.linspace(np.min(self.prof), np.max(self.prof), 10).tolist()
        axisx = PySide2.QtCharts.QtCharts.QValueAxis()
        axisx.setTickCount(3)
        axisx.setMinorTickCount(7)
        axisx.setTitleText("velocidad")
        axisy = PySide2.QtCharts.QtCharts.QValueAxis()
        axisy.setTickCount(5)
        axisy.setMinorTickCount(7)
        axisy.setTitleText("prof (m)")
        # axis.append(ejex)
        self.chartVS.createDefaultAxes()
        self.chartVS.setAxisX(axisx, self.seriesVS)
        self.chartVS.setAxisY(axisy, self.seriesVS)
        self.chartVS.setTitle("VS (m/s)")
        self.verticalLayout_VS.addWidget(self.chartViewVS)

    def plotVP(self):
        color = QtGui.QColor(230, 81, 0, 255)
        pen = QtGui.QPen(color)
        series = PySide2.QtCharts.QtCharts.QLineSeries()
        series.setColor(color)
        for i in range(len(self.vss)):
            series.append(self.df.iloc[i,0], self.prof[i])
        chart = PySide2.QtCharts.QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(PySide2.QtCharts.QtCharts.QChart.SeriesAnimations)
        chart.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignBottom)
        chart.resize(225, 400)
        chartView = PySide2.QtCharts.QtCharts.QChartView(chart)
        chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        ejex = np.linspace(np.min(self.df.iloc[:,0]) - 100, np.max(self.df.iloc[:,0]) + 100, 10).tolist()
        ejey = np.linspace(np.min(self.prof), np.max(self.prof), 10).tolist()
        axisx = PySide2.QtCharts.QtCharts.QValueAxis()
        axisx.setTickCount(3)
        axisx.setMinorTickCount(7)
        axisx.setTitleText("velocidad")
        axisy = PySide2.QtCharts.QtCharts.QValueAxis()
        axisy.setTickCount(5)
        axisy.setMinorTickCount(7)
        axisy.setTitleText("prof (m)")
        chart.createDefaultAxes()
        chart.setAxisX(axisx, series)
        chart.setAxisY(axisy, series)
        chart.setTitle("VP (m/s)")
        self.verticalLayout_VP.addWidget(chartView)

    def graficar(self):
        self.property_to_layer()
        self.plotVP()
        self.plotVS()
        self.plotAJUS(self.ajus)

    def conexiones(self):
        self.tableWidget_modelo.cellChanged.connect(self.changemodel)
        self.pushButton_savemod.clicked.connect(self.printmodel)

    def changemodel(self,i,j):
        new_val = float(self.tableWidget_modelo.item(i,j).text())
        self.df.iloc[self.matcorr[i, j, 0, 0], j-1] = new_val
        self.df.iloc[self.matcorr[i, j, 1, 0], j-1] = new_val
        df=self.changeTable()
        if j==1:
            for i in reversed(range(self.verticalLayout_VP.count())):
                self.verticalLayout_VP.itemAt(i).widget().setParent(None)
            self.plotVP()
        if j==2:
            for i in reversed(range(self.verticalLayout_VS.count())):
                self.verticalLayout_VS.itemAt(i).widget().setParent(None)
            self.plotVS()


        #self.chartViewVS.repaint()
        #self.chartViewVS.update()

        #self.df.at[i, j] =
        #self.df.at[i,j-1]
        #print(self.df.head(32))


    def printmodel(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(None, "Salvar Modelo", os.getcwd(), "TXT (*.txt)")
        final_df = pd.DataFrame({0:[-1*self.prof[i] for i in range(len(self.prof))], "VP":self.df.iloc[:,0], "VS":self.df.iloc[:,1], "DEN":self.df.iloc[:,2], "POISSON":self.df.iloc[:,3]})
        for i in range(1, len(final_df.iloc[:,0])):
            if final_df.iloc[i,0]==final_df.iloc[i-1,0]:
                final_df.at[i,0]=final_df.iloc[i, 0] + 0.01
        final_df.rename(columns={0: 'PROF'}, inplace=True)
        #final_df = final_df.abs()
        final_df.to_csv(filename[0], sep='\t', index=False, header=True, columns=["PROF", "VP", "VS", "DEN", "POISSON"])

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
    prof=[0.01,15.01,15.01,17.1868,17.1868,19.6795,19.6795,22.5339,22.5339,25.8025,25.8025,29.5455,29.5455,33.8317,\
         33.8317,38.7398,38.7398,44.3603,44.3603,50.7963,50.7963,58.1664,58.1664,66.606,66.606,76.2703,76.2703,87.3372,\
          87.3372,100.01,100.01,110.01]
    import numpy as np
    prof*= np.full(len(prof),-1)
    vpp=[2324.51,2324.51,1951.03,1951.03,1670.24,1670.24,2154.49,2154.49,1047.72,1047.72,965.375,965.375,998.343,998.343,\
         976.948,976.948,2273.39,2273.39,1100.12,1100.12,2267.95,2267.95,1163.73,1163.73,1680.13,1680.13,1114.27,\
         1114.27,2478.66,2478.66,852.836,852.836]
    vss=[660.698,660.698,187.544,187.544,522.259,522.259,258.314,258.314,159.106,159.106,497.187,497.187,559.254,559.254,\
         775.494,775.494,285.256,285.256,379.143,379.143,451.814,451.814,731.741,731.741,655.39,655.39,584.981,584.981,\
         566.556,566.556,69.561,69.561]
    """ajus=[1.78247,1.81553,1.84165,1.86077,1.87459,1.88555,1.89365,1.89378,1.8771,1.83837,1.78373,1.72936,1.68603,1.64797, \
          1.60657,1.56829,1.54366,1.52453,1.49969,1.47665,1.46145,1.44718,1.43595,1.43509,1.44086,1.44936,1.46417,1.4854, \
          1.50787,1.52912,1.55113,1.57544,1.60109,1.62636,1.65086,1.67538,1.70134,1.72976,1.76085,1.7942,1.82901,1.8643, \
          1.89901,1.93237,1.96393,1.99378,2.02247,2.05089,2.07967,2.10968,2.14109,2.17353,2.20641,2.23839,2.2685,2.29604, \
          2.32115,2.34472,2.36789,2.39184,2.41704,2.44302,2.46873,2.49304,2.51541,2.53632,2.55709,2.57921,2.60371,2.63058, \
          2.65951,2.69049,2.7245,2.7635,2.80881,2.85775,2.9018,2.9312,2.94216,2.93704,2.92014,2.89542,2.86558,2.83199, \
          2.79552,2.75689,2.71692,2.67621,2.63516,2.59369,2.55183,2.50989,2.46835,2.42768,2.38796,2.3488,2.3098,2.27078, \
          2.23185,2.19341,2.15581,2.11914,2.08313,2.04743,2.01184,1.97643,1.94146,1.90719,1.87365,1.84066,1.80787,1.77514, \
          1.74253,1.71038,1.67905,1.64876,1.61943,1.59082,1.56265,1.53481,1.5074,1.48063,1.45472,1.42974,1.40565,1.38238,\
          1.35991,1.33836,1.31789,1.29868,1.28085,1.26442,1.24936,1.23561,1.22311,1.21182,1.20174,1.19283,1.18504,1.17827,\
          1.1724,1.16729,1.16285,1.15904,1.15585,1.15331,1.15142,1.15014,1.14945,1.14931,1.14969,1.15058,1.15192,1.15367,1.15576,\
          1.15818,1.16089,1.16388,1.16711,1.17054,1.17415,1.17791,1.18183,1.1859,1.1901,1.19442,1.19886,1.20341,1.20807,1.21285,\
          1.21775,1.22279,1.22798,1.23336,1.23896,1.2448,1.2509,1.25729,1.26401,1.27109,1.27859,1.28651,1.29481,1.30332,\
          1.31185,1.32017,1.32809,1.33548,1.34229,1.34856,1.35432,1.35965,1.3646,1.36923,1.37357,1.37767,1.38156,\
          1.38527,1.38883,1.39226]"""
    ajus = pd.read_csv('actualHV.txt', delimiter="\t")
    ajus = ajus.iloc[:,1].values.tolist()
    ui.setupUi(dialogpinver,prof,vpp,vss,vpp,ajus,vss)
    dialogpinver.show()
    sys.exit(app.exec_())