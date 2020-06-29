# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_inv_form.ui',
# licensing of 'ventana_inv_form.ui' applies.
#
# Created: Mon Dec  9 13:19:14 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *
import HVmodules.inversionDB as inversionDB

class Ui_Ventana_inversion(QtWidgets.QMdiSubWindow):
    def __init__(self,name,dialog1,dialoginitmod,intype,file="x",data=None):
        super().__init__()
        self.setObjectName("Ventana_inversion")
        #self.resize(1638, 884)
        self.resize(1100, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 125))
        layoutPrincipal = QtWidgets.QGridLayout()
        widgetPrincipal = QtWidgets.QWidget()
        self.setWidget(widgetPrincipal)
        widgetPrincipal.setLayout(layoutPrincipal)
        self.groupBox = QtWidgets.QGroupBox()
        layoutPrincipal.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox.setGeometry(QtCore.QRect(9, 30, 154, 154))
        #(10, 201, 681, 674)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(10, 125))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_pinversion = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_pinversion.setObjectName("pushButton_pinversion")
        self.gridLayout.addWidget(self.pushButton_pinversion, 0, 1, 1, 1)
        self.pushButton_guardarinv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_guardarinv.setObjectName("pushButton_guardarinv")
        self.gridLayout.addWidget(self.pushButton_guardarinv, 2, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.pushButton_ini_inv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ini_inv.setObjectName("pushButton_ini_inv")
        self.gridLayout.addWidget(self.pushButton_ini_inv, 2, 1, 1, 1)
        self.progressBar_inv = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_inv.setProperty("value", 0)
        self.progressBar_inv.setObjectName("progressBar_inv")
        self.gridLayout.addWidget(self.progressBar_inv, 2, 2, 1, 2)
        self.pushButton_minicial = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_minicial.setObjectName("pushButton_minicial")
        self.gridLayout.addWidget(self.pushButton_minicial, 1, 1, 1, 1)
        #self.checkBox_minicial = QtWidgets.QCheckBox(self.groupBox)
        #self.checkBox_minicial.setText("")
        #self.checkBox_minicial.setObjectName("checkBox_minicial")
        #self.gridLayout.addWidget(self.checkBox_minicial, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.pushButton_cargarHV = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cargarHV.setObjectName("pushButton_cargarHV")
        self.gridLayout.addWidget(self.pushButton_cargarHV, 0, 5, 1, 1)
        self.pushButton_convergencia = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_convergencia.setCheckable(True)
        self.pushButton_convergencia.setObjectName("pushButton_convergencia")
        self.gridLayout.addWidget(self.pushButton_convergencia, 1, 5, 1, 1)
        self.mdiArea_inv = QtWidgets.QMdiArea()
        layoutPrincipal.addWidget(self.mdiArea_inv, 1, 1, 1, 1)
        self.mdiArea_inv.setGeometry(QtCore.QRect(700, 201, 931, 674))
        self.mdiArea_inv.setMinimumSize(QtCore.QSize(10, 10))
        self.mdiArea_inv.setMaximumSize(QtCore.QSize(931, 16777215))
        self.mdiArea_inv.setObjectName("mdiArea_inv")
        self.mdiArea_inv.layout = QtWidgets.QVBoxLayout()
        self.mdiArea_inv.setLayout(self.mdiArea_inv.layout)
        self.mdiArea_HV = QtWidgets.QMdiArea()
        layoutPrincipal.addWidget(self.mdiArea_HV, 1, 0, 1, 1)
        self.mdiArea_HV.setGeometry(QtCore.QRect(10, 201, 681, 674))
        self.mdiArea_HV.setObjectName("mdiArea_HV")
        self.mdiArea_HV.layout = QtWidgets.QVBoxLayout()
        self.mdiArea_HV.setLayout(self.mdiArea_HV.layout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        #self.name=name
        self.inversion = inversionDB.inver_DB(name)
        self.dialog1 = dialog1
        self.dialoginitmod = dialoginitmod
        self.parametros = 0
        self.conexiones()
        self.default()
        try:
            self.path=file
            self.read_HV(self.path)
        except:
            print("Archivos V.A....")


    def default(self):
        self.inversion.pmin = 0.33
        self.inversion.pmax= 0.45
        self.inversion.smin= 125.0
        self.inversion.smax= 400.0
        self.inversion.dmin= 1000.0
        self.inversion.dmax= 3000.0
        self.inversion.ncapas= 16
        self.inversion.prof= 100.0
        self.inversion.firstthick= 2.0
        self.inversion.iter = 50.0
        self.inversion.parts = 15
        self.inversion.Wini = 2
        self.inversion.Wamor = 0.8
        self.inversion.Vmax = 0.5
        self.inversion.C1 = 2.0
        self.inversion.C2 = 2.0
        self.inversion.df = 0.01
        self.inversion.vsgrad = 0.009
        self.inversion.vpgrad = 0.0001
        self.inversion.dengrad = 0.02
        self.inversion.basement = 1

    def setFini(self,val):
        self.inversion.fini = val


    def conexiones(self):
        self.pushButton_pinversion.pressed.connect(self.dialog1.open)
        self.pushButton_minicial.clicked.connect(self.init_model)
        #self.pushButton_ini_inv.clicked.connect(self.doInversion)
        self.pushButton_convergencia.clicked.connect(self.switchplot)
        self.pushButton_guardarinv.clicked.connect(self.results)
        self.pushButton_cargarHV.clicked.connect(self.loadHV)

    def loadHV(self):
        filename = QFileDialog.getOpenFileName(None, "Abrir H/V", os.getcwd(), "Text files (*.txt *.dat *.hv *.HV *.DAT *TXT)")
        self.read_HV(filename[0])

    def read_HV(self,filename):
        try:
            f=open(filename,'r')
            line = []
            encabs = 0
            line.append(f.readline())
            jj=0
            while line[jj].startswith('#'):
                line.append(f.readline())
                encabs += 1
                jj += 1
            self.inversion.HV = pd.read_csv(filename, skiprows=encabs, sep="\s+", header=None)
            #self.inversion.HV200 = self.inversion.HV
            self.setFini(self.inversion.HV.iloc[0,0])
            #HV200=self.inversion.HV
            #HV200.to_csv("actualHV.txt", index=None,sep='\t', columns=[0,1], header=None)
            #self.showHV()

            #print(self.inversion.HV.iloc[0,0])
            #print(self.inversion.HV.iloc[-1,0])
            fnew1=np.linspace(self.inversion.HV.iloc[0,0], self.inversion.HV.iloc[-1,0], 200, endpoint=True)
            HVnew1=self.resample_by_interpolation(self.inversion.HV.iloc[:,1], len(self.inversion.HV.iloc[:,1]), 200)
            df=pd.DataFrame({0:fnew1, 1:HVnew1})
            self.inversion.HV200 = df
            HV200 = self.inversion.HV200
            HV200.to_csv(os.path.join(os.path.join("HVmodules", "Inversion"), 'actualHV.txt'), index=None, sep='\t', columns=[0, 1], header=None)
            HV200.to_csv("actualHV.txt", index=None, sep='\t', columns=[0, 1], header=None)
            self.showHV()

            #print(df.head())
            #print()
            #print(self.inversion.HV.head())
            #self.inversion.HV200=
            #print(fnew1)
            #print(self.inversion.HV.iloc[:,0])
            #print()
            #print(HVnew1)
            #print(self.inversion.HV.iloc[:,1])

            #plt.plot(fnew1,HVnew1, "b")
            #plt.plot(self.inversion.HV.iloc[:,0], self.inversion.HV.iloc[:,1], "r")
            #plt.show()
            #print("termina")


        except:
            pass

    def resample_by_interpolation(self, senal, input_fs, output_fs):

        scale = output_fs / input_fs
        # calculate new length of sample
        n = round(len(senal) * scale)

        # use linear interpolation
        # endpoint keyword means than linspace doesn't go all the way to 1.0
        # If it did, there are some off-by-one errors
        # e.g. scale=2.0, [1,2,3] should go to [1,1.5,2,2.5,3,3]
        # but with endpoint=True, we get [1,1.4,1.8,2.2,2.6,3]
        # Both are OK, but since resampling will often involve
        # exact ratios (i.e. for 44100 to 22050 or vice versa)
        # using endpoint=False gets less noise in the resampled sound
        resampled_signal = np.interp(
            np.linspace(0.0, 1.0, n, endpoint=False),  # where to interpret
            np.linspace(0.0, 1.0, len(senal), endpoint=False),  # known positions
            senal,  # known data points
        )
        return resampled_signal

    def results(self):
        result = pd.DataFrame({"PROF":self.InvRes.iloc[:,0], "VP":self.InvRes.iloc[:,4], "VS":self.InvRes.iloc[:,2], "DEN":self.InvRes.iloc[:,3], "POISSON":self.InvRes.iloc[:,1]})
        filename = QtWidgets.QFileDialog.getSaveFileName(None, "Salvar Inversión", os.getcwd(), "Text files (*.txt)")
        try:
            result.to_csv(filename[0], index=False, sep='\t', header=True, columns=["PROF", "VP", "VS", "DEN", "POISSON"])
        except:
            print("Error en salvar inversión")


    def actualHV(self,HV,HV200):
        self.inversion.HV = HV
        self.inversion.HV200 = HV200
        #self.inversion.setHV(self.inversion.HV, self.inversion.HV200)

    def init_model(self):
        self.dialoginitmod.open()

    def switchplot(self):
        if self.pushButton_convergencia.isChecked():
            fig = Figure()
            p = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_HV.layout.count())):
                self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_HV.layout.addWidget(p)
            self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_HV))
            self.mdiArea_HV.plotsis = p.figure
            #fig.suptitle('Convergencia de Inversión '+ self.inversion.nombre)
            self.inversion.plotConvergence(self.mdiArea_HV.plotsis)
        else:
            fig = Figure()
            p = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_HV.layout.count())):
                self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_HV.layout.addWidget(p)
            self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_HV))
            self.mdiArea_HV.plotsis = p.figure
            #fig.suptitle('Ajuste de Modelo Invertido ' + self.inversion.nombre)
            self.inversion.plotModel(self.mdiArea_HV.plotsis)

    def doInversion(self):
        self.inversion.invertido = True
        fig = Figure()
        p = FigureCanvas(fig)
        for i in reversed(range(self.mdiArea_inv.layout.count())):
            self.mdiArea_inv.layout.itemAt(i).widget().setParent(None)
        self.mdiArea_inv.layout.addWidget(p)
        self.mdiArea_inv.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_inv))
        self.mdiArea_inv.plotsis = p.figure
        fig.suptitle('Modelo Invertido HV ' + self.inversion.nombre)
        fig2 = Figure()
        p2 = FigureCanvas(fig2)
        for i in reversed(range(self.mdiArea_HV.layout.count())):
            self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
        self.mdiArea_HV.layout.addWidget(p2)
        self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p2, self.mdiArea_HV))
        self.mdiArea_HV.plotsis = p2.figure
        #fig2.suptitle('Ajuste de Modelo Invertido ' + self.inversion.nombre)
        self.progressBar_inv.setValue(5)
        self.inversion.printParams(self.progressBar_inv, self.mdiArea_HV.plotsis, self.mdiArea_inv.plotsis)
        self.parametros= self.inversion.parametros_process()
        self.InvRes = self.inversion.results
        self.InvAdjust = self.inversion.adjust
        self.Conv = self.inversion.conv
        self.progressBar_inv.setValue(100)

    def showHV(self):
        fig= Figure()
        p = FigureCanvas(fig)
        for i in reversed(range(self.mdiArea_HV.layout.count())):
            self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
        self.mdiArea_HV.layout.addWidget(p)
        self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_HV))
        self.mdiArea_HV.plotsis = p.figure
        #fig.suptitle('H/V de estación ' + self.inversion.nombre)
        self.inversion.showHV(self.mdiArea_HV.plotsis)
        pass

    def setSmax(self, val):
        self.inversion.changeSmax(val)

    def setSmin(self, val):
        self.inversion.changeSmin(val)

    def setPmin(self,val):
        self.inversion.changePmin(val)

    def setPmax(self, val):
        self.inversion.changePmax(val)

    def setDmin(self, val):
        self.inversion.changeDmin(val)

    def setDmax(self, val):
        self.inversion.changeDmax(val)

    def setProf(self, val):
        self.inversion.changeProf(val)

    def setFirstThick(self, val):
        self.inversion.changefirstthick(val)

    def set_basement(self, val):
        if val==0:
            self.inversion.basement = 0
        else:
            self.inversion.basement = 1

    def setNcapas(self,val):
        self.inversion.changeNcapas(val)

    def setIter(self,val):
        self.inversion.changeIter(val)

    def setParts(self,val):
        self.inversion.changeParts(val)

    def setWini(self,val):
        self.inversion.changeWini(val)

    def setWamor(self,val):
        self.inversion.changeWamor(val)

    def setC1(self,val):
        self.inversion.changeC1(val)

    def setC2(self,val):
        self.inversion.changeC2(val)

    def setVmax(self,val):
        self.inversion.changeVmax(val)

    def setVpgrad(self,val):
        self.inversion.changeVpgrad(val)

    def setVsgrad(self,val):
        self.inversion.changeVsgrad(val)

    def setDengrad(self,val):
        self.inversion.changeDengrad(val)


    def retranslateUi(self, Ventana_inversion):
        Ventana_inversion.setWindowTitle(QtWidgets.QApplication.translate("Ventana_inversion", "Ventana de inversión", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Ventana_inversion", "", None, -1))
        self.pushButton_pinversion.setText(QtWidgets.QApplication.translate("Ventana_inversion", "Parámetros de inversión", None, -1))
        self.pushButton_guardarinv.setText(QtWidgets.QApplication.translate("Ventana_inversion", "Guardar inversión", None, -1))
        self.pushButton_ini_inv.setText(QtWidgets.QApplication.translate("Ventana_inversion", "Invertir", None, -1))
        self.pushButton_minicial.setText(QtWidgets.QApplication.translate("Ventana_inversion", "Cargar modelo Inicial", None, -1))
        self.pushButton_convergencia.setText(QtWidgets.QApplication.translate("Ventana_inversion", "Convergencia", None,-1))
        self.pushButton_cargarHV.setText(QtWidgets.QApplication.translate("Ventana_inversion", "Cargar H/V", None, -1))

