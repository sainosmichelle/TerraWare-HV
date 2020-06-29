# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ventana_process_form2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *
import HVmodules.processDB as process


class Ui_Ventana_procesamiento(QtWidgets.QMdiSubWindow):


    def __init__(self, currentIndex,dialogfilter,intype,file="x",data=None):
        super().__init__()
        #font = QtGui.QFont("MS Shell Dlg 2", 10)
        self.setObjectName("Ventana_procesamiento")
        #self.resize(1638, 884)
        self.resize(1100, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 125))
        #self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox = QtWidgets.QGroupBox()

        #self.groupBox.setFont(font)



        layoutPrincipal=QtWidgets.QGridLayout()
        #self.setLayout(layoutPrincipal)
        #layoutPrincipal.addWidget(self.groupBox, 0,0,2,1)

        widgetPrincipal = QtWidgets.QWidget()
        self.setWidget(widgetPrincipal)
        widgetPrincipal.setLayout(layoutPrincipal)
        layoutPrincipal.addWidget(self.groupBox, 0,0,1,2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.groupBox.setLayout(self.gridLayout)


        self.gridLayout.setObjectName("gridLayout")

        #self.setWidget(widgetPrincipal)
        self.groupBox.setGeometry(QtCore.QRect(9, 30, 1618, 165))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(10, 125))
        self.groupBox.setObjectName("groupBox")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        self.label_norm = QtWidgets.QLabel(self.groupBox)
        #self.label_norm.setFont(font)
        self.label_norm.setObjectName("label_norm")
        self.gridLayout.addWidget(self.label_norm, 0, 0, 1, 1)
        self.label_tap = QtWidgets.QLabel(self.groupBox)
        self.label_tap.setObjectName("label_tap")
        self.gridLayout.addWidget(self.label_tap, 1, 0, 1, 1)
        self.label_fhv = QtWidgets.QLabel(self.groupBox)
        self.label_fhv.setObjectName("label_fhv")
        self.gridLayout.addWidget(self.label_fhv, 0, 12, 1, 3)
        self.label_trasl = QtWidgets.QLabel(self.groupBox)
        self.label_trasl.setObjectName("label_trasl")
        self.gridLayout.addWidget(self.label_trasl, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 15, 1, 1)
        self.doubleSpinBox_dt = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_dt.setDecimals(4)
        self.doubleSpinBox_dt.setMaximum(1.0)
        self.doubleSpinBox_dt.setObjectName("doubleSpinBox_dt")
        self.gridLayout.addWidget(self.doubleSpinBox_dt, 0, 7, 1, 1)
        self.label_dt = QtWidgets.QLabel(self.groupBox)
        self.label_dt.setObjectName("label_dt")
        self.gridLayout.addWidget(self.label_dt, 0, 6, 1, 1)
        self.label_konno = QtWidgets.QLabel(self.groupBox)
        self.label_konno.setObjectName("label_konno")
        self.gridLayout.addWidget(self.label_konno, 1, 9, 1, 1)
        self.comboBox_norm = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_norm.setObjectName("comboBox_norm")
        self.comboBox_norm.addItem("")
        self.comboBox_norm.addItem("")
        self.comboBox_norm.addItem("")
        self.comboBox_norm.addItem("")
        self.gridLayout.addWidget(self.comboBox_norm, 0, 1, 1, 1)
        self.comboBox_tap = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_tap.setObjectName("comboBox_tap")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")
        self.comboBox_tap.addItem("")  #boxcar
        self.comboBox_tap.addItem("")  # nutall
        self.gridLayout.addWidget(self.comboBox_tap, 1, 1, 1, 1)

        self.doubleSpinBox_konno = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_konno.setMaximum(90.0)
        self.doubleSpinBox_konno.setObjectName("doubleSpinBox_konno")
        self.gridLayout.addWidget(self.doubleSpinBox_konno, 1, 10, 1, 1)
        self.pushButton_saveHV = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_saveHV.setObjectName("pushButton_saveHV")
        self.gridLayout.addWidget(self.pushButton_saveHV, 2, 19, 1, 1)
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout.addWidget(self.pushButton_reset, 1, 19, 1, 1)
        self.doubleSpinBox_taper = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_taper.setDecimals(3)
        self.doubleSpinBox_taper.setMaximum(1.0)
        self.doubleSpinBox_taper.setObjectName("doubleSpinBox_taper")
        self.gridLayout.addWidget(self.doubleSpinBox_taper, 1, 4, 1, 1)
        self.label_df = QtWidgets.QLabel(self.groupBox)
        self.label_df.setObjectName("label_df")
        self.gridLayout.addWidget(self.label_df, 1, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 18, 1, 1)
        self.pushButton_ini_process = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ini_process.setObjectName("pushButton_ini_process")

        self.gridLayout.addWidget(self.pushButton_ini_process, 3, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 11, 1, 1)
        self.label_ffin = QtWidgets.QLabel(self.groupBox)
        self.label_ffin.setObjectName("label_ffin")
        self.gridLayout.addWidget(self.label_ffin, 2, 12, 1, 1)

        self.pushButton_filtroButter = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_filtroButter.setObjectName("pushButton_filtroButter")
        self.gridLayout.addWidget(self.pushButton_filtroButter, 0, 16, 1, 2)
        self.pushButton_HVdir = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_HVdir.setObjectName("pushButton_HVdir")
        self.pushButton_HVdir.setCheckable(True)
        self.gridLayout.addWidget(self.pushButton_HVdir, 1, 16, 1, 2)
        self.pushButton_savehvdir = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_savehvdir.setObjectName("pushButton_savehvdir")
        self.gridLayout.addWidget(self.pushButton_savehvdir, 2, 16, 1, 2)
        self.pushButton_save_esp = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_save_esp.setObjectName("pushButton_save_esp")
        self.gridLayout.addWidget(self.pushButton_save_esp, 3, 16, 1, 2)
        # self.label_butter = QtWidgets.QLabel(self.groupBox)
        # self.label_butter.setObjectName("label_butter")
        # self.gridLayout.addWidget(self.label_butter, 0, 16, 1, 2)
        #self.label_wini = QtWidgets.QLabel(self.groupBox)
        #self.label_wini.setObjectName("label_wini")
        #self.gridLayout.addWidget(self.label_wini, 1, 16, 1, 1)
        #self.doubleSpinBox_wini = QtWidgets.QDoubleSpinBox(self.groupBox)
        #self.doubleSpinBox_wini.setDecimals(3)
        #self.doubleSpinBox_wini.setObjectName("doubleSpinBox_wini")
        #self.gridLayout.addWidget(self.doubleSpinBox_wini, 1, 17, 1, 1)
        # self.label_wfin = QtWidgets.QLabel(self.groupBox)
        # self.label_wfin.setObjectName("label_wfin")
        # self.gridLayout.addWidget(self.label_wfin, 2, 16, 1, 1)
        #self.doubleSpinBox_wfin = QtWidgets.QDoubleSpinBox(self.groupBox)
        #self.doubleSpinBox_wfin.setDecimals(3)
        #self.doubleSpinBox_wfin.setObjectName("doubleSpinBox_wfin")
        #self.gridLayout.addWidget(self.doubleSpinBox_wfin, 2, 17, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.gridLayout.addWidget(self.progressBar, 3, 1, 1, 2)

        self.doubleSpinBox_ffin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_ffin.setDecimals(3)
        self.doubleSpinBox_ffin.setObjectName("doubleSpinBox_ffin")
        self.gridLayout.addWidget(self.doubleSpinBox_ffin, 2, 13, 1, 1)
        self.doubleSpinBox_df = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_df.setDecimals(4)
        self.doubleSpinBox_df.setMaximum(1.0)
        self.doubleSpinBox_df.setObjectName("doubleSpinBox_df")
        self.gridLayout.addWidget(self.doubleSpinBox_df, 1, 7, 1, 1)
        self.label_svents = QtWidgets.QLabel(self.groupBox)
        self.label_svents.setObjectName("label_svents")
        self.gridLayout.addWidget(self.label_svents, 0, 9, 1, 1)
        self.doubleSpinBox_fini = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_fini.setDecimals(3)
        self.doubleSpinBox_fini.setObjectName("doubleSpinBox_fini")
        self.gridLayout.addWidget(self.doubleSpinBox_fini, 1, 13, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 8, 1, 1)
        self.label_fini = QtWidgets.QLabel(self.groupBox)
        self.label_fini.setObjectName("label_fini")
        self.gridLayout.addWidget(self.label_fini, 1, 12, 1, 1)
        self.spinBox_svents = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_svents.setMaximum(100000)
        self.spinBox_svents.setObjectName("spinBox_svents")
        self.gridLayout.addWidget(self.spinBox_svents, 0, 10, 1, 1)
        self.checkBox_onebit = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_onebit.setObjectName("checkBox_onebit")
        self.gridLayout.addWidget(self.checkBox_onebit, 2, 0, 1, 1)
        self.checkBox_baseline = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_baseline.setObjectName("checkBox_baseline")
        self.gridLayout.addWidget(self.checkBox_baseline, 2, 1, 1, 1)
        self.label_taper = QtWidgets.QLabel(self.groupBox)
        self.label_taper.setObjectName("label_taper")
        self.gridLayout.addWidget(self.label_taper, 1, 3, 1, 1)
        self.pushButton_spectra = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_spectra.setObjectName("pushButton_spectra")
        self.pushButton_spectra.setCheckable(True)
        self.gridLayout.addWidget(self.pushButton_spectra, 0, 19, 1, 1)
        self.doubleSpinBox_trasl = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_trasl.setMaximum(100.0)
        self.doubleSpinBox_trasl.setObjectName("doubleSpinBox_trasl")
        self.gridLayout.addWidget(self.doubleSpinBox_trasl, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 11, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 2, 1, 1)
        self.label_vents = QtWidgets.QLabel(self.groupBox)
        self.label_vents.setObjectName("label_vents")
        self.gridLayout.addWidget(self.label_vents, 3, 3, 1, 1)
        self.lcdNumber_vents = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_vents.setDigitCount(6)
        self.lcdNumber_vents.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_vents.setObjectName("lcdNumber_vents")
        self.gridLayout.addWidget(self.lcdNumber_vents, 3, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 18, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 18, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 15, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 15, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 2, 11, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 8, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 0, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 0, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 3, 2, 1, 1)
        self.mdiArea_vents = QtWidgets.QMdiArea()
        layoutPrincipal.addWidget(self.mdiArea_vents, 1, 0, 1, 1)
        self.mdiArea_vents.setGeometry(QtCore.QRect(9, 201, 931, 674))
        self.mdiArea_vents.setMinimumSize(QtCore.QSize(10, 10))
        self.mdiArea_vents.setMaximumSize(QtCore.QSize(931, 16777215))
        self.mdiArea_vents.setObjectName("mdiArea_vents")
        self.mdiArea_vents.layout = QtWidgets.QVBoxLayout()
        self.mdiArea_vents.setLayout(self.mdiArea_vents.layout)
        self.mdiArea_HV = QtWidgets.QMdiArea()
        layoutPrincipal.addWidget(self.mdiArea_HV, 1, 1, 1, 1)
        self.mdiArea_HV.setGeometry(QtCore.QRect(946, 201, 681, 674))
        self.mdiArea_HV.setMinimumSize(QtCore.QSize(40, 10))
        self.mdiArea_HV.setMaximumSize(QtCore.QSize(681, 16777215))
        self.mdiArea_HV.setObjectName("mdiArea_HV")
        self.mdiArea_HV.layout = QtWidgets.QVBoxLayout()
        self.mdiArea_HV.setLayout(self.mdiArea_HV.layout)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.HV=0

        name_HVSR_one = file.split('/')#(os.path.sep)
        self.path = file#os.path.sep.join(name_HVSR_one[0:-1])
        self.currentIndex = currentIndex
        if intype==0:
            self.procesamientoDB = process.process_DB(currentIndex,file)
            self.crudo = pd.DataFrame({'VE':self.procesamientoDB.VE,
                                   'NS':self.procesamientoDB.NS,
                                   'EW':self.procesamientoDB.EW})
            self.procesamientoDB.name = name_HVSR_one[-1]
            self.setWindowTitle("Procesamiento de estación " + self.procesamientoDB.name)
            self.dialogfilter= dialogfilter
            fig = Figure()
            p = FigureCanvas(fig)
            self.mdiArea_vents.layout.addWidget(p)
            self.mdiArea_vents.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_vents))
            self.mdiArea_vents.plotsis = p.figure
            self.procesamientoDB.registros_plot_single(self.mdiArea_vents.plotsis)
            self.parametros=0
            self.setDefaultValues()
            self.procesamientoDB.processParamsDefault()
            self.conexiones()
        elif intype ==2:
            print ("Abriendo Proyecto...")
            self.procesamientoDB = process.process_DB(self.currentIndex)
            self.procesamientoDB.nombre = data[self.currentIndex]["name"]
            print( data[self.currentIndex]["VE"].split(","))
            self.procesamientoDB.VE = [float(x) for x in data[self.currentIndex]["VE"].split(",")]
            self.procesamientoDB.NS = [float(x) for x in data[self.currentIndex]["VE"].split(",")]
            self.procesamientoDB.EW = [float(x) for x in data[self.currentIndex]["VE"].split(",")]
            print(self.procesamientoDB.VE)
            self.crudo = pd.DataFrame({'VE': self.procesamientoDB.VE,
                                       'NS': self.procesamientoDB.NS,
                                       'EW': self.procesamientoDB.EW})
            self.setWindowTitle("Procesamiento de estación " + data[self.currentIndex]["name"])
            self.dialogfilter = dialogfilter
            fig = Figure()
            p = FigureCanvas(fig)
            self.mdiArea_vents.layout.addWidget(p)
            self.mdiArea_vents.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_vents))
            self.mdiArea_vents.plotsis = p.figure
            try:
                self.procesamientoDB.dt = float(data[self.currentIndex]["new_dt"])
            except:
                self.procesamientoDB.dt = 0.005
            self.procesamientoDB.tini= datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
            nmues=len(self.procesamientoDB.VE)
            self.parametros = 0
            self.procesamientoDB.tfin = self.procesamientoDB.tini + datetime.timedelta(seconds=nmues * self.procesamientoDB.dt - self.procesamientoDB.dt)
            self.nombre=data[self.currentIndex]["name"]
            self.procesamientoDB.registros_plot_single(self.mdiArea_vents.plotsis)
            self.setDefaultValues()
            self.procesamientoDB.processParamsDefault()
            self.conexiones()
        else:
            print("Archivos de H/V")
            self.procesamientoDB = process.process_DB(self.currentIndex)

    def conexiones(self):
        self.doubleSpinBox_konno.valueChanged.connect(self.procesamientoDB.konnoValueChanged)
        self.doubleSpinBox_taper.valueChanged.connect(self.procesamientoDB.taperValueChanged)
        self.checkBox_onebit.stateChanged.connect(self.procesamientoDB.onebitStateChanged)
        self.checkBox_baseline.stateChanged.connect(self.procesamientoDB.baselineStateChanged)
        self.comboBox_norm.currentIndexChanged.connect(self.procesamientoDB.selectioNormChanged)
        self.comboBox_tap.currentIndexChanged.connect(self.procesamientoDB.selectionTapChanged)
        self.spinBox_svents.valueChanged.connect(self.procesamientoDB.sventValueChanged)
        self.doubleSpinBox_trasl.valueChanged.connect(self.procesamientoDB.trasValueChanged)
        #self.doubleSpinBox_wini.valueChanged.connect(self.procesamientoDB.winiValueChanged)
        #self.doubleSpinBox_wfin.valueChanged.connect(self.procesamientoDB.wfinValueChanged)
        self.doubleSpinBox_fini.valueChanged.connect(self.procesamientoDB.finiValueChanged)
        self.doubleSpinBox_ffin.valueChanged.connect(self.procesamientoDB.ffinValueChanged)
        self.doubleSpinBox_dt.valueChanged.connect(self.procesamientoDB.dtValueChanged)
        self.doubleSpinBox_df.valueChanged.connect(self.procesamientoDB.dfValueChanged)
        self.pushButton_reset.clicked.connect(self.setDefaultValues)  # self.procesamientoDB.processParamsDefault)
        #self.pushButton_ini_process.clicked.connect(self.startProcessing)
        self.pushButton_saveHV.clicked.connect(self.saveHV)
        self.pushButton_savehvdir.clicked.connect(self.saveDIRHV)
        self.pushButton_spectra.clicked.connect(self.switchplot)
        self.pushButton_filtroButter.clicked.connect(self.showfiltro)
        self.pushButton_HVdir.clicked.connect(self.switchplot_HVDIR)
        self.pushButton_save_esp.clicked.connect(self.save_esp)

    def showfiltro(self):
        self.dialogfilter.open()

    def save_esp(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(None, "Salvar Espectros de Amplitud", os.getcwd(), "Text files (*.txt)")
        self.procesamientoDB.guardar_esp_ampl(filename)

    def switchplot(self):
        if self.pushButton_spectra.isChecked():
            fig = Figure()
            p = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_vents.layout.count())):
                self.mdiArea_vents.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_vents.layout.addWidget(p)
            self.mdiArea_vents.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_vents))
            self.mdiArea_vents.plotsis = p.figure
            self.procesamientoDB.espectros_plot(self.mdiArea_vents.plotsis)
        else:
            fig = Figure()
            p = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_vents.layout.count())):
                self.mdiArea_vents.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_vents.layout.addWidget(p)
            self.mdiArea_vents.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_vents))
            self.mdiArea_vents.plotsis = p.figure
            self.procesamientoDB.ventanas_plot(self.mdiArea_vents.plotsis)

    def switchplot_HVDIR(self):
        print("Entra a switchplot_HVDIR")
        if self.pushButton_HVdir.isChecked():
            print("entra al if")
            fig = Figure()
            p = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_HV.layout.count())):
                self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_HV.layout.addWidget(p)
            self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_HV))
            self.mdiArea_HV.plotsis = p.figure
            print("entra al HVDIR_plot")
            self.procesamientoDB.HVDIR_plot(self.mdiArea_HV.plotsis)
        else:
            print("entra al else")
            fig = Figure()
            p = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_HV.layout.count())):
                self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_HV.layout.addWidget(p)
            self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_HV))
            self.mdiArea_HV.plotsis = p.figure
            print("entra al HV_plot")
            self.procesamientoDB.HV_plot(self.mdiArea_HV.plotsis)

    def saveHV(self):
        filename=QtWidgets.QFileDialog.getSaveFileName(None, "Salvar H/V", os.getcwd(), "Text files (*.txt)")
        self.procesamientoDB.guardar_HV(filename)

    def saveDIRHV(self):
        filename=QtWidgets.QFileDialog.getSaveFileName(None, "Salvar H/V direccionales", os.getcwd(), "Text files (*.txt)")
        self.procesamientoDB.guardar_DIRHV(filename)

    def startProcessing(self):
        self.procesamientoDB.procesado=True
        fmax = 1 / (2 * self.procesamientoDB.new_dt)
        Nyq = int(fmax / self.procesamientoDB.new_df + 1)  # ?
        Nespec = (Nyq - 1) * 2  # ?
        # vini = [];  vfin = []
        NSfilt, EWfilt, VEfilt = self.procesamientoDB.butterf()
        win_samples = int(self.procesamientoDB.svent / self.procesamientoDB.new_dt)
        Ntras = int(floor(self.procesamientoDB.tras / 100.0 * win_samples))
        self.progressBar.setValue(5)
        try:
            length = len(VEfilt)
            good_length = int(length / 2 + 1)
            self.procesamientoDB.vi = np.arange(0, length, (win_samples - Ntras) + 1, dtype=int)
            self.procesamientoDB.vf = self.procesamientoDB.vi + win_samples
            cambmax = [i for i in range(len(self.procesamientoDB.vf)) if self.procesamientoDB.vf[i] > length]
            if len(cambmax) != 0:
                self.procesamientoDB.vf[cambmax] = length
            longit = self.procesamientoDB.vf - self.procesamientoDB.vi + np.ones(len(self.procesamientoDB.vi))
            tvent = np.array([[self.procesamientoDB.vi], [self.procesamientoDB.vf], [longit]])
            M = len(self.procesamientoDB.vi)
            # Correccion de lineabase y taper por ventana
            self.procesamientoDB.NSvif = np.zeros(length)
            self.procesamientoDB.EWvif = np.zeros(length)
            self.procesamientoDB.VEvif = np.zeros(length)
            for ll in range(M):
                self.procesamientoDB.NSvif[self.procesamientoDB.vi[ll]:self.procesamientoDB.vf[ll]] = \
                    self.procesamientoDB.baseline_taper(NSfilt[self.procesamientoDB.vi[ll]:self.procesamientoDB.vf[ll]])
                self.procesamientoDB.EWvif[self.procesamientoDB.vi[ll]:self.procesamientoDB.vf[ll]] = \
                    self.procesamientoDB.baseline_taper(EWfilt[self.procesamientoDB.vi[ll]:self.procesamientoDB.vf[ll]])
                self.procesamientoDB.VEvif[self.procesamientoDB.vi[ll]:self.procesamientoDB.vf[ll]] = \
                    self.procesamientoDB.baseline_taper(VEfilt[self.procesamientoDB.vi[ll]:self.procesamientoDB.vf[ll]])
            self.progressBar.setValue(10)
            # Elimina las ventanas mas energeticas de señal
            self.procesamientoDB.wincleantot = np.zeros(M)
            #print("Entra a picos")
            self.progressBar.setValue(15)
            wincleanNS = self.procesamientoDB.picos(self.procesamientoDB.NSvif)
            wincleanEW = self.procesamientoDB.picos(self.procesamientoDB.EWvif)
            wincleanZ = self.procesamientoDB.picos(self.procesamientoDB.VEvif)
            self.progressBar.setValue(25)
            #print("Sale de picos")
            # ventanas coincidentes en las tres direcciones
            #print ("wincleanNS %s"%wincleanNS)
            #print("wincleanEW %s" %wincleanEW)
            #print("wincleanZ %s" %wincleanZ)
            self.procesamientoDB.wincleantot = wincleanNS * wincleanEW * wincleanZ
            #print("winclean")
            Nvent = int(sum(self.procesamientoDB.wincleantot))
            #print("Nvent")
            self.lcdNumber_vents.display(Nvent)
            #print("Ventanas")
            self.progressBar.setValue(30)
            if int(tvent[2][0][-1]) < win_samples:
                self.procesamientoDB.wincleantot[-1] = 0
            fig = Figure()
            p = FigureCanvas(fig)
            self.progressBar.setValue(35)
            for i in reversed(range(self.mdiArea_vents.layout.count())):
                self.mdiArea_vents.layout.itemAt(i).widget().setParent(None)
            self.progressBar.setValue(40)
            self.mdiArea_vents.layout.addWidget(p)
            self.mdiArea_vents.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_vents))
            self.mdiArea_vents.plotsis = p.figure
            self.progressBar.setValue(45)
            #fig.suptitle('Ventanas de Estación ' + self.procesamientoDB.nombre)
            self.procesamientoDB.ventanas_plot(self.mdiArea_vents.plotsis)
            self.progressBar.setValue(50)
            fig = Figure()
            q = FigureCanvas(fig)
            for i in reversed(range(self.mdiArea_HV.layout.count())):
                self.mdiArea_HV.layout.itemAt(i).widget().setParent(None)
            self.mdiArea_HV.layout.addWidget(q)
            self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(q, self.mdiArea_HV))
            self.mdiArea_HV.plotsis = q.figure
            #fig.suptitle('H/V de estación ' + self.procesamientoDB.nombre)
            freq, Hv = self.procesamientoDB.espectros(self.mdiArea_HV.plotsis, M, Nespec, fmax)
            self.HV = pd.DataFrame({'f': freq,
                                    'HVSR': Hv})
            self.HV200 = self.procesamientoDB.HV200
            #print(self.HV.head(10))
            ####self.HV200 = self.procesamientoDB.df_200
            self.parametros=self.procesamientoDB.parametros_process()
            self.procesamientoDB.saveTmp()
            self.progressBar.setValue(100)
        except:
            print("Error en procesamiento de %s" % self.procesamientoDB.currentIndex)
            pass
            self.progressBar.setValue(0)

    def setDefaultValues(self):
        self.doubleSpinBox_konno.setValue(30.0)
        self.doubleSpinBox_taper.setValue(0.05)
        self.checkBox_onebit.setChecked(0)
        self.checkBox_baseline.setChecked(0)
        self.comboBox_norm.setCurrentIndex(1)
        self.comboBox_tap.setCurrentIndex(0)
        self.spinBox_svents.setValue(80)
        self.doubleSpinBox_trasl.setValue(0.0)
        #self.doubleSpinBox_wini.setValue(0.5)
        #self.doubleSpinBox_wfin.setValue(10.0)
        self.doubleSpinBox_fini.setValue(0.1)
        self.doubleSpinBox_ffin.setValue(15.0)
        self.doubleSpinBox_dt.setValue(self.procesamientoDB.dt)
        #self.doubleSpinBox_dt.setValue(0.005)
        self.doubleSpinBox_df.setValue(0.01)
        self.procesamientoDB.processParamsDefault()


    def retranslateUi(self, Ventana_procesamiento):
        _translate = QtCore.QCoreApplication.translate
        Ventana_procesamiento.setWindowTitle(_translate("Ventana_procesamiento", "Ventana_procesamiento"))
        self.groupBox.setTitle(_translate("Ventana_procesamiento", "Parámetros de procesamiento de H/V"))
        self.label_norm.setText(_translate("Ventana_procesamiento", "Normalización:"))
        self.label_tap.setText(_translate("Ventana_procesamiento", "Ventana de taper:"))
        self.label_fhv.setText(_translate("Ventana_procesamiento", "Frecuencias para H/V:"))
        self.label_trasl.setText(_translate("Ventana_procesamiento", "Traslape (%)"))
        self.label_dt.setText(_translate("Ventana_procesamiento", "muestreo tiempo (dt)"))
        self.label_konno.setText(_translate("Ventana_procesamiento", "Konno-Ohmachi:"))
        self.comboBox_norm.setItemText(0, _translate("Ventana_procesamiento", "Energías Unitarias"))
        self.comboBox_norm.setItemText(1, _translate("Ventana_procesamiento", "Suma de Energías"))
        self.comboBox_norm.setItemText(2, _translate("Ventana_procesamiento", "Spectral Whitening"))
        self.comboBox_norm.setItemText(3, _translate("Ventana_procesamiento", "Envolvente en tiempo"))

        self.comboBox_tap.setItemText(0, _translate("Ventana_procesamiento", "Tukey"))
        self.comboBox_tap.setItemText(1, _translate("Ventana_procesamiento", "Hann"))
        self.comboBox_tap.setItemText(2, _translate("Ventana_procesamiento", "Blackman"))
        self.comboBox_tap.setItemText(3, _translate("Ventana_procesamiento", "Triangular"))
        self.comboBox_tap.setItemText(4, _translate("Ventana_procesamiento", "Coseno"))
        self.comboBox_tap.setItemText(5, _translate("Ventana_procesamiento", "Hamming"))
        self.comboBox_tap.setItemText(6, _translate("Ventana_procesamiento", "Flat-top"))
        self.comboBox_tap.setItemText(7, _translate("Ventana_procesamiento", "Cuadrada"))
        self.comboBox_tap.setItemText(8, _translate("Ventana_procesamiento", "Blackman-Harris"))

        self.pushButton_saveHV.setText(_translate("Ventana_procesamiento", "Guardar H/V"))
        self.pushButton_reset.setText(_translate("Ventana_procesamiento", "Reset"))
        self.pushButton_savehvdir.setText(_translate("Ventana_procesamiento", "Guardar direccionales"))
        self.pushButton_HVdir.setText(_translate("Ventana_procesamiento",  "H/V direccionales"))
        self.pushButton_save_esp.setText(_translate("Ventana_procesamiento",  "Guardar espectros"))
        self.label_df.setText(_translate("Ventana_procesamiento", "muestreo frecuencia (df)"))
        self.pushButton_ini_process.setText(_translate("Ventana_procesamiento", "Procesar"))
        self.pushButton_filtroButter.setText(_translate("Ventana_procesamiento", "Filtro de Butterworth"))
        # self.label_butter.setText(_translate("Ventana_procesamiento", " Frecuencias de Butterworth:"))
        # self.label_wini.setText(_translate("Ventana_procesamiento", "<html><head/><body><p align=\"center\">w inicial</p></body></html>"))
        # self.label_wfin.setText(_translate("Ventana_procesamiento", "<html><head/><body><p align=\"center\">w final</p></body></html>"))
        self.label_ffin.setText(_translate("Ventana_procesamiento", "<html><head/><body><p align=\"center\">f final</p></body></html>"))
        self.label_svents.setText(_translate("Ventana_procesamiento", "Segundos de la ventana:"))
        self.label_fini.setText(_translate("Ventana_procesamiento", "<html><head/><body><p align=\"center\">f inicial</p></body></html>"))
        self.checkBox_onebit.setText(_translate("Ventana_procesamiento", "OneBit"))
        self.checkBox_baseline.setText(_translate("Ventana_procesamiento", "Quitar tendencia"))
        self.label_taper.setText(_translate("Ventana_procesamiento", "Factor de Tukey: "))
        self.pushButton_spectra.setText(_translate("Ventana_procesamiento", "Espectros"))
        self.label_vents.setText(_translate("Ventana_procesamiento", "Número de ventanas:"))

