from HVmodules.NModule import *
import HVmodules.GUI_form as GUI_form
import HVmodules.ventana_process_form2 as ventana_process_form2
import HVmodules.ventana_inv_form as ventana_inv_form
import HVmodules.Project as Project
import HVmodules.dialog_invertype as dialog_invertype
import HVmodules.dialog_initialmodel2 as dialog_initialmodel2
import HVmodules.dialog_pvents as dialog_pvents
import HVmodules.dialog_filtertype as dialog_filtertype

import HVmodules.processDB as processDB
import HVmodules.konno_ohmachi as konno
import HVmodules.inversionDB as inversionDB
import HVmodules.dialog_pinver as dialog_pinver

class MainWindow_EXEC():

    def __init__(self):
        #app.QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = GUI_form.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        #-----------------------------------
        open('last_params.txt', 'w').close()
        open(os.path.join(os.path.join("HVmodules","Inversion"),'last_params.txt'),'w').close()
        open('actualHV.txt', 'w').close()
        open(os.path.join(os.path.join("HVmodules", "Inversion"), 'actualHV.txt'), 'w').close()
        open("ConvergenceETotal.txt", 'w').close()
        open("ConvergenceEGrad.txt", 'w').close()
        open("ConvergenceEData.txt", 'w').close()
        open("DataHVSR.dat", 'w').close()
        open("parametros_inv.txt", 'w').close()
        open(os.path.join(os.path.join("HVmodules", "Inversion"), 'parametros_inv.txt'), 'w').close()
        open("InvertModelHVSR.dat", "w").close()
        open("InitialModelHVSR.dat", "w").close()
        open("Models100HVSR.dat", "w").close()
        open("Ajustes100HVSR.dat", "w").close()
        self.ui.actionAbrir_V_A.triggered.connect(self.cargar_VA)
        self.ui.actionAbrir_HVSR.triggered.connect(self.cargar_HV)
        self.currentIndex = -1
        self.ui.treeWidget_project.itemDoubleClicked.connect(self.seleccionar_estacion)
        self.dialog1 = QtWidgets.QDialog()
        self.ui.invertype = dialog_invertype.Ui_dialoginvtype()
        self.ui.invertype.setupUi(self.dialog1)

        self.dialoginitmod = QtWidgets.QDialog()
        self.ui.initmod = dialog_initialmodel2.Ui_ModeloInicial()
        self.ui.initmod.setupUi(self.dialoginitmod)

        self.dialogvents = QtWidgets.QDialog()
        self.ui.ventsparams = dialog_pvents.Ui_dialogVents()
        self.ui.ventsparams.setupUi(self.dialogvents)

        self.dialogfilter = QtWidgets.QDialog()
        self.ui.filtertype = dialog_filtertype.Ui_Filtrobutter()
        self.ui.filtertype.setupUi(self.dialogfilter)

        self.ui.actionGuardarproyecto.triggered.connect(self.saveProject)
        self.ui.actionAbrirProyectoTW.triggered.connect(self.openProject)
        #-----------------------------------
        MainWindow.show()
        sys.exit(app.exec_())

    def cargar_VA(self):
        self.proy=Project.proyecto()
        filename=QFileDialog.getOpenFileNames(None,"Abrir archivos de V.A.",os.getcwd(),"Text files (*.saf *.SAF)")
        l1 = QTreeWidgetItem(["Proyecto V.A."])

        for file in filename[0]:
            name_HVSR_one=file.split('/')#(os.path.sep)
            name_HVSR_one = name_HVSR_one[-1]
            l1_child=QTreeWidgetItem([name_HVSR_one])
            l1.addChild(l1_child)
            #pathlist.append(files)
            self.ui.treeWidget_project.addTopLevelItem(l1)
            sub_sismogramas = ventana_process_form2.Ui_Ventana_procesamiento(self.proy.archi,self.dialogfilter,0,file=file)
            sub_inversion = ventana_inv_form.Ui_Ventana_inversion(name_HVSR_one, self.dialog1, self.dialoginitmod,0)
            self.ui.mdiArea_INV.addSubWindow(sub_inversion)
            self.ui.mdiArea.addSubWindow(sub_sismogramas)
            self.proy.archi += 1
            self.proy.crudos.append(sub_sismogramas.crudo)
            self.proy.CwindowsP.append(sub_sismogramas)
            self.proy.CwindowsI.append(sub_inversion)
            self.proy.procesados.append(sub_sismogramas.procesamientoDB.procesado)
            self.proy.invertidos.append(sub_inversion.inversion.invertido)
            self.proy.names.append(name_HVSR_one)
            self.conexiones(self.proy.archi-1)
        self.proy.setarchi()
        #self.dialog1.hide()

    """    """

    def cargar_HV(self):
        self.proy=Project.proyecto()
        filename = QFileDialog.getOpenFileNames(None, "Abrir archivos de H/V", os.getcwd(),
                                                "Text files (*.txt *.dat *.hv *.HV *.DAT *TXT)")
        l1 = QTreeWidgetItem(["Proyecto H/V"])
        for file in filename[0]:
            print("entra a los archivos")
            name_HVSR_one=file.split('/')#(os.path.sep)
            name_HVSR_one = name_HVSR_one[-1]
            l1_child=QTreeWidgetItem([name_HVSR_one])
            l1.addChild(l1_child)
            #pathlist.append(files)
            self.ui.treeWidget_project.addTopLevelItem(l1)

            sub_sismogramas = ventana_process_form2.Ui_Ventana_procesamiento(self.proy.archi,self.dialogfilter,1)
            sub_inversion = ventana_inv_form.Ui_Ventana_inversion(name_HVSR_one, self.dialog1, self.dialoginitmod,1,file=file)
            self.ui.mdiArea_INV.addSubWindow(sub_inversion)
            self.ui.mdiArea.addSubWindow(sub_sismogramas)
            self.proy.archi += 1
            try:
                self.proy.crudos.append(sub_sismogramas.crudo)
                self.proy.CwindowsP.append(sub_sismogramas)
                self.proy.CwindowsI.append(sub_inversion)
            except:
                pass
            self.proy.procesados.append(sub_sismogramas.procesamientoDB.procesado)
            self.proy.invertidos.append(sub_inversion.inversion.invertido)
            self.proy.names.append(name_HVSR_one)
            self.conexiones(self.proy.archi - 1)
        self.proy.setarchi()

    def changeInvParams(self, index):
        print("Sondeo "+ str(index))
        try:
            data = pd.read_csv("last_params.txt", header=None)
            self.ui.mdiArea_INV.subWindowList()[index].inversion.prof = data[0][0]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.firstthick = data[0][1]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.ncapas = data[0][2]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.pmin = data[0][3]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.pmax = data[0][4]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.smin = data[0][5]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.smax = data[0][6]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.dmin = data[0][7]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.dmax = data[0][8]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.iter = data[0][9]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.parts = data[0][10]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.Wini = data[0][11]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.Wamor = data[0][12]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.C1 = data[0][13]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.C2 = data[0][14]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.Vmax = data[0][15]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.df = data[0][16]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.fini = data[0][17]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.vsgrad = data[0][18]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.vpgrad = data[0][19]
            self.ui.mdiArea_INV.subWindowList()[index].inversion.dengrad = data[0][20]
        except:
            print("No hay archivo de parametros anteriores (last params)")

    def seleccionar_estacion(self, item):
        currentIndex = self.ui.treeWidget_project.topLevelItem(0).indexOfChild(item)
        self.currentIndex= currentIndex
        self.changeInvParams(currentIndex)
        self.ui.mdiArea.subWindowList()[currentIndex].showMaximized()
        self.ui.mdiArea_INV.subWindowList()[currentIndex].showMaximized()
        self.proy.whichIndex(currentIndex)

    def conexiones(self,index):
        # Interacciones con otras ventanas
        self.ui.initmod.pushButton_loadmodel.clicked.connect(self.loadinitmodel)
        self.ui.actionParamsVents.triggered.connect(self.showVentsMenu)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_konno.valueChanged.connect(self.proy.changeKonnoAll)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_taper.valueChanged.connect(self.proy.changeTapperAll)
        self.ui.mdiArea.subWindowList()[index].checkBox_onebit.stateChanged.connect(self.proy.changeOnebitAll)
        self.ui.mdiArea.subWindowList()[index].checkBox_baseline.stateChanged.connect(self.proy.changeBLAll)
        self.ui.mdiArea.subWindowList()[index].comboBox_norm.currentIndexChanged.connect(self.proy.changeNormIndex)
        self.ui.mdiArea.subWindowList()[index].comboBox_tap.currentIndexChanged.connect(self.proy.changeTapIndex)
        self.ui.mdiArea.subWindowList()[index].spinBox_svents.valueChanged.connect(self.proy.changeSventAll)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_trasl.valueChanged.connect(self.proy.changeTrasAll)
        #self.ui.mdiArea.subWindowList()[currentIndex].doubleSpinBox_wini.valueChanged.connect(self.proy.changeWiniAll)
        #self.ui.mdiArea.subWindowList()[currentIndex].doubleSpinBox_wfin.valueChanged.connect(self.proy.changeWfinAll)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_fini.valueChanged.connect(self.proy.changeFiniAll)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_ffin.valueChanged.connect(self.proy.changeFfinAll)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_dt.valueChanged.connect(self.proy.changeDtAll)
        self.ui.mdiArea.subWindowList()[index].doubleSpinBox_df.valueChanged.connect(self.proy.changeDfAll)
        self.ui.mdiArea.subWindowList()[index].pushButton_ini_process.clicked.connect(self.startProcess)
        #self.ui.mdiArea.subWindowList()[currentIndex].pushButton_saveHV.clicked.connect(self.saveHV)
        #self.ui.mdiArea_INV.subWindowList()[currentIndex].pushButton_guardarinv.clicked.connect(self.save_inverDB)
        self.ui.mdiArea_INV.subWindowList()[index].pushButton_ini_inv.clicked.connect(self.startInv)
        self.ui.initmod.doubleSpinBox_smax.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setSmax)
        self.ui.initmod.doubleSpinBox_smin.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setSmin)
        self.ui.initmod.doubleSpinBox_pmin.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setPmin)
        self.ui.initmod.doubleSpinBox_pmax.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setPmax)
        self.ui.initmod.doubleSpinBox_dmin.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setDmin)
        self.ui.initmod.doubleSpinBox_dmax.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setDmax)
        self.ui.initmod.doubleSpinBox_prof.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setProf)
        self.ui.initmod.doubleSpinBox_firstthick.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setFirstThick)
        self.ui.initmod.checkBox_bsm.stateChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].set_basement)
        self.ui.initmod.spinBox_ncapas.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setNcapas)
        self.ui.invertype.inverparams.spinBox_iter.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setIter)
        self.ui.invertype.inverparams.spinBox_parts.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setParts)
        self.ui.invertype.inverparams.doubleSpinBox_wini.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setWini)
        self.ui.invertype.inverparams.doubleSpinBox_wa.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setWamor)
        self.ui.invertype.inverparams.doubleSpinBox_c1.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setC1)
        self.ui.invertype.inverparams.doubleSpinBox_velmax.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setVmax)
        self.ui.invertype.inverparams.doubleSpinBox_vpgrad.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setVpgrad)
        self.ui.invertype.inverparams.doubleSpinBox_vsgrad.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setVsgrad)
        self.ui.invertype.inverparams.doubleSpinBox_dengrad.valueChanged.connect(
            self.ui.mdiArea_INV.subWindowList()[index].setDengrad)
        self.ui.ventsparams.spinBox_iter.valueChanged.connect(
             self.ui.mdiArea.subWindowList()[index].procesamientoDB.smaxChanged)  # smax
        #self.ui.ventsparams.spinBox_parts.valueChanged.connect(
        #    self.ui.mdiArea.subWindowList()[index].procesamientoDB.tltaChanged)  # tlta
        self.ui.ventsparams.doubleSpinBox_wini.valueChanged.connect(
            self.ui.mdiArea.subWindowList()[index].procesamientoDB.porc1Changed)  # porc1
        self.ui.ventsparams.doubleSpinBox_wa.valueChanged.connect(
            self.ui.mdiArea.subWindowList()[index].procesamientoDB.porc2Changed)  # porc2
        self.ui.filtertype.pasaBandas.doubleSpinBox_wini.valueChanged.connect(
            self.ui.mdiArea.subWindowList()[index].procesamientoDB.winiValueChanged)
        self.ui.filtertype.pasaBandas.doubleSpinBox_wfin.valueChanged.connect(
            self.ui.mdiArea.subWindowList()[index].procesamientoDB.wfinValueChanged)
        self.ui.filtertype.pasaAltas.doubleSpinBox_wini.valueChanged.connect(
            self.ui.mdiArea.subWindowList()[index].procesamientoDB.wPasaAltas)
        self.ui.filtertype.pasaBajas.doubleSpinBox_wfin.valueChanged.connect(
            self.ui.mdiArea.subWindowList()[index].procesamientoDB.wPasaBajas)

    def startInv(self):
        self.ui.mdiArea_INV.subWindowList()[self.currentIndex].doInversion()
        self.proy.setinv()
        self.proy.Inver[self.proy.currentIndex] = self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].InvRes
        self.proy.Ajuste[self.proy.currentIndex] = self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].InvAdjust
        self.proy.Convergence[self.proy.currentIndex] = self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].Conv
        self.proy.inverparams[self.proy.currentIndex] = self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].parametros

    def startProcess(self):
        self.ui.mdiArea.subWindowList()[self.currentIndex].startProcessing()
        self.proy.setproc()
        self.set_fini(self.proy.currentIndex)
        self.proy.processparams[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[self.proy.currentIndex].parametros
        self.proy.HV[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[self.proy.currentIndex].HV
        self.proy.HV200[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[self.proy.currentIndex].HV200
        self.proy.meankN[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[
                self.proy.currentIndex].procesamientoDB.meankN
        self.proy.meankE[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[
                self.proy.currentIndex].procesamientoDB.meankE
        self.proy.meankV[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[
                self.proy.currentIndex].procesamientoDB.meankV
        self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].actualHV(self.proy.HV[self.proy.currentIndex],
                                                                             self.proy.HV200[self.proy.currentIndex])
        self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].showHV()


    def showVentsMenu(self):
        self.dialogvents.open()

    def saveProject(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(None, "Salvar Proyecto", os.getcwd(), "JSON (*.json)")
        self.proy.guardarProyecto(filename[0])

    def openProject(self):
        self.proy = Project.proyecto()
        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Abrir Proyecto", os.getcwd(), "JSON (*.json)")
        data = self.proy.leerProyecto(filename[0])
        proy_name=filename[0].split("/")
        l1 = QTreeWidgetItem(["Proyecto "+proy_name[-1]])
        for i in range(self.proy.archi):
            l1_child = QTreeWidgetItem([self.proy.names[i]])
            l1.addChild(l1_child)
            self.ui.treeWidget_project.addTopLevelItem(l1)
            sub_sismogramas = ventana_process_form2.Ui_Ventana_procesamiento(i, self.dialogfilter, 2, data=data)
            sub_inversion = ventana_inv_form.Ui_Ventana_inversion(self.proy.names[i], self.dialog1, self.dialoginitmod,2)
            self.ui.mdiArea.addSubWindow(sub_sismogramas)
            self.ui.mdiArea_INV.addSubWindow(sub_inversion)
            self.proy.crudos.append(sub_sismogramas.crudo)
            self.proy.CwindowsP.append(sub_sismogramas)
            self.proy.CwindowsI.append(sub_inversion)
            self.proy.procesados.append(sub_sismogramas.procesamientoDB.procesado)
            self.proy.invertidos.append(sub_inversion.inversion.invertido)
            #self.proy.names.append(name_HVSR_one)
            self.conexiones(i)
        self.proy.setarchi()


    def set_fini(self,index):
        self.ui.mdiArea_INV.subWindowList()[index].setFini(self.ui.mdiArea.subWindowList()[index].procesamientoDB.fini)


    def loadinitmodel(self):
        filename=QFileDialog.getOpenFileName(None,"Abrir modelo inicial",os.getcwd(),"Text files (*.txt *.dat)")
        try:
            f=open(filename[0],'r')
            line=[]
            for jj  in range(10):
                line.append(f.readline())
                if (line[jj].startswith('Prof')):
                    profundidad = line[jj].split(':')
                    profundidad = float(profundidad[1].strip())
                    self.ui.initmod.doubleSpinBox_prof.setValue(profundidad)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setProf(profundidad)
                if (line[jj].startswith('Num')):
                    ncapas = line[jj].split(':')
                    ncapas = int(ncapas[1].strip())
                    self.ui.initmod.spinBox_ncapas.setValue(ncapas)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setNcapas(ncapas)
                if (line[jj].startswith('Espesor')):
                    espcapa1 = line[jj].split(':')
                    espcapa1 = float(espcapa1[1].strip())
                    self.ui.initmod.doubleSpinBox_firstthick.setValue(espcapa1)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setFirstThick(espcapa1)
                if (line[jj].startswith('Vpmin')):
                    vpmin = line[jj].split(':')
                    vpmin = float(vpmin[1].strip())
                    self.ui.initmod.doubleSpinBox_pmin.setValue(vpmin)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setPmin(vpmin)
                if (line[jj].startswith('Vpmax')):
                    vpmax = line[jj].split(':')
                    vpmax = float(vpmax[1].strip())
                    self.ui.initmod.doubleSpinBox_pmax.setValue(vpmax)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setPmax(vpmax)
                if (line[jj].startswith('Vsmin')):
                    vsmin = line[jj].split(':')
                    vsmin = float(vsmin[1].strip())
                    self.ui.initmod.doubleSpinBox_smin.setValue(vsmin)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setSmin(vsmin)
                if (line[jj].startswith('Vsmax')):
                    vsmax = line[jj].split(':')
                    vsmax = float(vsmax[1].strip())
                    self.ui.initmod.doubleSpinBox_smax.setValue(vsmax)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setSmax(vsmax)
                if (line[jj].startswith('Denmin')):
                    denmin = line[jj].split(':')
                    denmin = float(denmin[1].strip())
                    self.ui.initmod.doubleSpinBox_dmin.setValue(denmin)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setDmin(denmin)
                if (line[jj].startswith('Denmax')):
                    denmax = line[jj].split(':')
                    denmax = float(denmax[1].strip())
                    self.ui.initmod.doubleSpinBox_dmax.setValue(denmax)
                    self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].setDmax(denmax)
        except:
            pass


    '''def save_processDB(self):
        self.proy.setproc()
        self.proy.processparams[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[self.proy.currentIndex].parametros
        self.set_fini(self.proy.currentIndex)
        #print(self.proy.processparams[self.proy.currentIndex])
        #self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].showHV(self.proy)'''

    '''def save_inverDB(self):
        self.proy.Inver[self.proy.currentIndex] = self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].InvRes
        self.proy.Ajuste[self.proy.currentIndex] = self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].InvAdjust
        self.proy.Convergence[self.proy.currentIndex]=self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].Conv
        self.proy.inverparams[self.proy.currentIndex]=self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].parametros'''
        #print(self.proy.inverparams[self.proy.currentIndex])

    '''def saveHV(self):
        self.proy.HV[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[self.proy.currentIndex].HV
        self.proy.HV200[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[self.proy.currentIndex].HV200
        self.proy.meankN[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[
            self.proy.currentIndex].procesamientoDB.meankN
        self.proy.meankE[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[
            self.proy.currentIndex].procesamientoDB.meankE
        self.proy.meankV[self.proy.currentIndex] = self.ui.mdiArea.subWindowList()[
            self.proy.currentIndex].procesamientoDB.meankV
        self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].actualHV(self.proy.HV[self.proy.currentIndex],
                                                                             self.proy.HV200[self.proy.currentIndex])
        self.ui.mdiArea_INV.subWindowList()[self.proy.currentIndex].showHV()'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    path2 = os.getcwd()
    pixmap = QtGui.QPixmap(os.path.join(path2,os.path.join("Logos","LogoE.png")))
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()
    MainWindow = QtWidgets.QMainWindow()
    splash.finish(MainWindow)
    ui = MainWindow_EXEC()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
