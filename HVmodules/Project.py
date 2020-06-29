from HVmodules.NModule import *

class proyecto():
    def __init__(self):
        super().__init__()
        self.proyname = None  # Nombre del proyecto         !!!!!!
        self.archi = 0        # Numero de archivos
        self.names=[]         # Nombre de los archivos
        self.CwindowsP = []   # Ui_Ventana_procesamiento
        self.processparams=[] #parametros de procesamiento   !!!!!!!
        self.crudos=[]        # Señales originales
        self.HV=[]            # HV procesado de 1000 muestras
        self.HV200 = []       # HV remuestreado
        self.meankN = []      # espectros NS
        self.meankE = []      # espectros EW
        self.meankV = []      # espectros VE
        self.procesados =[]   # Archivos procesados
        self.CwindowsI = []   # Ui_Ventana_procesamiento
        self.inverparams = [] # parametros de inversion       !!!!!!!
        self.Inver = []       # Inversiones
        self.Ajuste = []      # Ajustes
        self.Convergence = [] # Convergencia
        self.invertidos = []  # Archivos invertidos
        self.key_names = []
        self.keyNames()
        self.konno=[]
        self.taper=[]
        self.onebit=[]
        self.normal=[]
        self.svent=[]
        self.tras=[]
        self.wini=[]
        self.wfin=[]
        self.fini=[]
        self.ffin=[]
        self.tlta=[]
        self.porc1=[]
        self.porc2=[]
        self.new_dt=[]
        self.new_df=[]
        self.spectreVE=[]
        self.spectreNS=[]
        self.spectreEW=[]
        self.frec_large=[]
        self.HV_large=[]
        self.smin=[]
        self.smax=[]
        self.pmin=[]
        self.dmin=[]
        self.dmax=[]
        self.prof=[]
        self.firstthick=[]
        self.ncapas=[]
        self.iter=[]
        self.parts=[]
        self.Wini=[]
        self.Wamor=[]
        self.C1=[]
        self.C2=[]
        self.Vmax=[]
        self.vsgrad=[]
        self.vpgrad=[]
        self.dengrad=[]
        self.f200=[]
        self.HV200=[]
        self.Inver_prof=[]
        self.Inver_vp=[]
        self.Inver_vs=[]
        self.Inver_rho=[]
        self.VE=[]
        self.NS=[]
        self.EW=[]
        self.list_proy=[]

    def setarchi(self):
        self.HV=[0]*self.archi
        self.HV200=[0]*self.archi
        self.meankN = [0]*self.archi
        self.meankE = [0]*self.archi
        self.meankV = [0]*self.archi
        self.Inver=[0]*self.archi
        self.Ajuste=[0]*self.archi
        self.Convergence = [0]*self.archi
        self.processparams = [0]*self.archi
        self.inverparams = [0]*self.archi

    def guardarProyecto(self,name):
        self.dictsCreacion() #self.list_dicts
        for i in range(self.archi):
            ## PARAMETROS DE PROCESAMIENTO
            values = []
            values.append(self.names[i])
            values.append(self.procesados[i])  # procesado =
            if self.procesados[i] == True:
                values.append(self.processparams[i][0])  # konno =
                values.append(self.processparams[i][1])  # taper =
                values.append(self.processparams[i][2])  # onebit =
                values.append(self.processparams[i][3])  # normal =
                values.append(self.processparams[i][4])  # svent =
                values.append(self.processparams[i][5])  # tras =
                values.append(self.processparams[i][6])  # wini =
                values.append(self.processparams[i][7])  # wfin =
                values.append(self.processparams[i][8])  # fini =
                values.append(self.processparams[i][9])  # ffin =
                values.append(self.processparams[i][10])  # smax =
                values.append(self.processparams[i][11])  # tlta =
                values.append(self.processparams[i][12])  # porc1 =
                values.append(self.processparams[i][13])  # porc2 =
                values.append(self.processparams[i][14])  # new_dt =
                values.append(self.processparams[i][15])  # new_df =
                values.append(','.join(map(str,self.meankN[i]))) #  self.meankN[i])  # spectreNS =   # list
                values.append(','.join(map(str,self.meankE[i])))  # spectreEW =   # list
                values.append(','.join(map(str,self.meankV[i])))  # spectreVE =   # list
                values.append(','.join(map(str,self.HV[i].iloc[:, 0].to_numpy()))) # frec_large =   # DataFrame 'f','HVSR'
                values.append(','.join(map(str,self.HV[i].iloc[:, 1].to_numpy())))  # HV_large =
            else:
                values.append(None)  # konno = null
                values.append(None)  # taper =
                values.append(None)  # onebit =
                values.append(None)  # normal =
                values.append(None)  # svent =
                values.append(None)  # tras =
                values.append(None)  # wini =
                values.append(None)  # wfin =
                values.append(None)  # fini =
                values.append(None)  # ffin =
                values.append(None)  # smax =
                values.append(None)  # tlta =
                values.append(None)  # porc1 =
                values.append(None)  # porc2 =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                values.append(None)  # porc2 =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                ## PARAMETROS DE INVERSION
            values.append(self.invertidos[i])  # invertido =
            if self.invertidos[i] == True:
                values.append(self.inverparams[i][0])  # smin =
                values.append(self.inverparams[i][1])  # smax =
                values.append(self.inverparams[i][2])  # pmin =
                values.append(self.inverparams[i][3])  # pmax =
                values.append(self.inverparams[i][4])  # dmin =
                values.append(self.inverparams[i][5])  # dmax =
                values.append(self.inverparams[i][6])  # prof =
                values.append(self.inverparams[i][7])  # firstthick =
                values.append(self.inverparams[i][8])  # ncapas =
                values.append(self.inverparams[i][9])  # iter =
                values.append(self.inverparams[i][10])  # parts =
                values.append(self.inverparams[i][11])  # Wini =
                values.append(self.inverparams[i][12])  # Wamor =
                values.append(self.inverparams[i][13])  # C1 =
                values.append(self.inverparams[i][14])  # C2 =
                values.append(self.inverparams[i][15])  # Vmax =
                values.append(self.inverparams[i][16])  # fini =
                values.append(self.inverparams[i][17])  # vsgrad =
                values.append(self.inverparams[i][18])  # vpgrad =
                values.append(self.inverparams[i][19])  # dengrad =
                values.append(','.join(map(str,self.Ajuste[i].iloc[:,0].to_numpy())))  # f200 =   # DataFrame "# frecuencia", "average", "stdminus", "stdplus"
                values.append(','.join(map(str,self.Ajuste[i].iloc[:, 2].to_numpy())))  # HV200 =
                values.append(','.join(map(str,self.Inver[i].iloc[:, 0].to_numpy())))  # Inver_prof =   # DataFrame 0,1,2,3
                values.append(','.join(map(str,self.Inver[i].iloc[:, 1].to_numpy())))  # Inver_vp =
                values.append(','.join(map(str,self.Inver[i].iloc[:, 2].to_numpy())))  # Inver_vs =
                values.append(','.join(map(str,self.Inver[i].iloc[:, 3].to_numpy())))  # Inver_rho =
                values.append(','.join(map(str,self.Ajuste[i].iloc[:, 1].to_numpy())))  # Ajuste =   # DataFrame 0,1,2 (freq, ajuste, HV200)
                values.append(','.join(map(str,self.Convergence[i].iloc[:, 0].to_numpy())))  # Convergence =   # Dataframe 0 ()
            else:
                values.append(None)  # konno =
                values.append(None)  # taper =
                values.append(None)  # onebit =
                values.append(None)  # normal =
                values.append(None)  # svent =
                values.append(None)  # tras =
                values.append(None)  # wini =
                values.append(None)  # wfin =
                values.append(None)  # fini =
                values.append(None)  # ffin =
                values.append(None)  # smax =
                values.append(None)  # tlta =
                values.append(None)  # porc1 =
                values.append(None)  # porc2 =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
            values.append(','.join(map(str,self.crudos[i].iloc[:, 0].to_numpy())))  # VE =   # Dataframe {'VE', 'NS', 'EW'}
            values.append(','.join(map(str,self.crudos[i].iloc[:, 1].to_numpy())))  # NS =
            values.append(','.join(map(str,self.crudos[i].iloc[:, 2].to_numpy())))  # EW ='''
            ii=0
            for j in self.key_names:
                self.list_dicts[i][j]=values[ii]
                ii += 1
        new_list_dicts=[]
        for i in range(len(self.list_dicts)):
            if not self.list_dicts[i]:
                pass
            else:
                new_list_dicts.append(self.list_dicts[i])
        import json
        jsona = json.dumps(new_list_dicts)
        f=open(name, 'w')
        f.write(jsona)
        f.close()
        print("Se ha guardado proyecto")

    def leerProyecto(self,name):
        print("Lectura de proyecto")
        import json
        with open(name,"r") as read_file:
            data = json.load(read_file)
        self.asignaVars(data)
        return data


    def asignaVars(self,data):
        self.archi=len(data)
        for i in range(self.archi):
            print(i)
            self.names.append(data[i]["name"])  # Nombre del proyecto         !!!!!!
            self.procesados.append(data[i]["procesado"])
            self.konno.append(data[i]["konno"])
            self.taper.append(data[i]["taper"])
            self.onebit.append(data[i]["onebit"])
            self.normal.append(data[i]["normal"])
            self.svent.append(data[i]["svent"])
            self.tras.append(data[i]["tras"])
            self.wini.append(data[i]["wini"])
            self.wfin.append(data[i]["wfin"])
            self.fini.append(data[i]["fini"])
            self.ffin.append(data[i]["ffin"])
            self.tlta.append(data[i]["tlta"])
            self.porc1.append(data[i]["porc1"])
            self.porc2.append(data[i]["porc2"])
            self.new_dt.append(data[i]["new_dt"])
            self.new_df.append(data[i]["new_df"])
            self.spectreVE.append(data[i]["spectreVE"])
            self.spectreNS.append(data[i]["spectreNS"])
            self.spectreEW.append(data[i]["spectreEW"])
            self.frec_large.append(data[i]["frec_large"])
            self.HV_large.append(data[i]["HV_large"])
            self.invertidos.append(data[i]["invertido"])
            self.smin.append(data[i]["smin"])
            self.smax.append(data[i]["smax"])
            self.pmin.append(data[i]["pmin"])
            #self.pmax.append(data[i]["pmax"])
            self.dmin.append(data[i]["dmin"])
            self.dmax.append(data[i]["dmax"])
            self.prof.append(data[i]["prof"])
            self.firstthick.append(data[i]["firstthick"])
            self.ncapas.append(data[i]["ncapas"])
            self.iter.append(data[i]["iter"])
            self.parts.append(data[i]["parts"])
            self.Wini.append(data[i]["Wini"])
            self.Wamor.append(data[i]["Wamor"])
            self.C1.append(data[i]["C1"])
            self.C2.append(data[i]["C2"])
            self.Vmax.append(data[i]["Vmax"])
            self.vsgrad.append(data[i]["vsgrad"])
            self.vpgrad.append(data[i]["vpgrad"])
            self.dengrad.append(data[i]["dengrad"]) #f200
            self.f200.append(data[i]["f200"])
            self.HV200.append(data[i]["HV200"])
            self.Inver_prof.append(data[i]["Inver_prof"])
            self.Inver_vp.append(data[i]["Inver_vp"])
            self.Inver_vs.append(data[i]["Inver_vs"])
            self.Inver_rho.append(data[i]["Inver_rho"])
            self.Ajuste.append(data[i]["Ajuste"])
            self.Convergence.append(data[i]["Convergence"])
            self.VE.append(data[i]["VE"])
            self.NS.append(data[i]["NS"])
            self.EW.append(data[i]["EW"])

    def setproc(self):
        self.procesados[self.currentIndex]=True
        return

    def setinv(self):
        self.invertidos[self.currentIndex]=True
        return

    def whichIndex(self, currentIndex):
        self.currentIndex=currentIndex


    def changeKonnoAll(self, val):
        for i in range(len(self.CwindowsP)):
            if not self.procesados[i]:
                self.CwindowsP[i].doubleSpinBox_konno.setValue(val)

    def changeTapperAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_taper.setValue(val)

    def changeOnebitAll(self, b):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].checkBox_onebit.setChecked(b)

    def changeBLAll(self, b):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].checkBox_baseline.setChecked(b)

    def changeNormIndex(self, ind):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].comboBox_norm.setCurrentIndex(ind)

    def changeTapIndex(self, ind):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].comboBox_tap.setCurrentIndex(ind)

    def changeSventAll(self, ival):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].spinBox_svents.setValue(ival)

    def changeTrasAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_trasl.setValue(val)

    def changeWiniAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_wini.setValue(val)

    def changeWfinAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_wfin.setValue(val)

    def changeFiniAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_fini.setValue(val)

    def changeFfinAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_ffin.setValue(val)

    def changeDtAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_dt.setValue(val)

    def changeDfAll(self, val):
        for i in range(self.archi):
            if self.procesados[i] == False:
                self.CwindowsP[i].doubleSpinBox_df.setValue(val)

    def keyNames(self):
        self.key_names.append("name")
        self.key_names.append("procesado")
        self.key_names.append("konno")
        self.key_names.append("taper")
        self.key_names.append("onebit")
        self.key_names.append("normal")
        self.key_names.append("svent")
        self.key_names.append("tras")
        self.key_names.append("wini")
        self.key_names.append("wfin")
        self.key_names.append("fini")
        self.key_names.append("ffin")
        self.key_names.append("smax")
        self.key_names.append("tlta")
        self.key_names.append("porc1")
        self.key_names.append("porc2")
        self.key_names.append("new_dt")
        self.key_names.append("new_df")
        self.key_names.append("spectreNS")
        self.key_names.append("spectreEW")
        self.key_names.append("spectreVE")
        self.key_names.append("frec_large")
        self.key_names.append("HV_large")
        self.key_names.append("invertido")
        self.key_names.append("smin")
        self.key_names.append("smax")
        self.key_names.append("pmin")
        self.key_names.append("pmax")
        self.key_names.append("dmin")
        self.key_names.append("dmax")
        self.key_names.append("prof")
        self.key_names.append("firstthick")
        self.key_names.append("ncapas")
        self.key_names.append("iter")
        self.key_names.append("parts")
        self.key_names.append("Wini")
        self.key_names.append("Wamor")
        self.key_names.append("C1")
        self.key_names.append("C2")
        self.key_names.append("Vmax")
        self.key_names.append("fini")
        self.key_names.append("vsgrad")
        self.key_names.append("vpgrad")
        self.key_names.append("dengrad")
        self.key_names.append("f200")
        self.key_names.append("HV200")
        self.key_names.append("Inver_prof")
        self.key_names.append("Inver_vp")
        self.key_names.append("Inver_vs")
        self.key_names.append("Inver_rho")
        self.key_names.append("Ajuste")
        self.key_names.append("Convergence")
        self.key_names.append("VE")
        self.key_names.append("NS")
        self.key_names.append("EW")

    def dictsCreacion(self):
        self.list_dicts = []
        for i in range(50):
            self.list_dicts.append({})

        '''for i in range(self.archi):
            key_names.append("procesado_"+str(i))
            key_names.append("konno_" + str(i))
            key_names.append("taper_" + str(i))
            key_names.append("onebit_" + str(i))
            key_names.append("normal_" + str(i))
            key_names.append("svent_" + str(i))
            key_names.append("tras_" + str(i))
            key_names.append("wini_" + str(i))
            key_names.append("wfin_" + str(i))
            key_names.append("fini_" + str(i))
            key_names.append("ffin_" + str(i))
            key_names.append("smax_" + str(i))
            key_names.append("tlta_" + str(i))
            key_names.append("porc1_" + str(i))
            key_names.append("porc2_" + str(i))
            key_names.append("new_dt_" + str(i))
            key_names.append("new_df_" + str(i))
            key_names.append("spectreNS_" + str(i))
            key_names.append("spectreEW_" + str(i))
            key_names.append("spectreVE_" + str(i))
            key_names.append("frec_large_" + str(i))
            key_names.append("HV_large_" + str(i))
            key_names.append("invertido_" + str(i))
            key_names.append("smin_" + str(i))
            key_names.append("smax_" + str(i))
            key_names.append("pmin_" + str(i))
            key_names.append("pmax_" + str(i))
            key_names.append("dmin_" + str(i))
            key_names.append("dmax_" + str(i))
            key_names.append("prof_" + str(i))
            key_names.append("firstthick_" + str(i))
            key_names.append("ncapas_" + str(i))
            key_names.append("iter_" + str(i))
            key_names.append("parts_" + str(i))
            key_names.append("Wini_" + str(i))
            key_names.append("Wamor_" + str(i))
            key_names.append("C1_" + str(i))
            key_names.append("C2_" + str(i))
            key_names.append("Vmax_" + str(i))
            key_names.append("fini_" + str(i))
            key_names.append("vsgrad_" + str(i))
            key_names.append("vpgrad_" + str(i))
            key_names.append("dengrad_" + str(i))
            key_names.append("f200_" + str(i))
            key_names.append("HV200_" + str(i))
            key_names.append("Inver_prof_" + str(i))
            key_names.append("Inver_vp_" + str(i))
            key_names.append("Inver_vs_" + str(i))
            key_names.append("Inver_rho_" + str(i))
            key_names.append("Ajuste_" + str(i))
            key_names.append("Convergence_" + str(i))
            key_names.append("VE_" + str(i))
            key_names.append("NS_" + str(i))
            key_names.append("EW_" + str(i))

            ## PARAMETROS DE PROCESAMIENTO
            values.append(self.procesados[i])#procesado =
            if self.procesados[i]==True:
                values.append(self.processparams[i][0])#konno =
                values.append(self.processparams[i][1])#taper =
                values.append(self.processparams[i][2])#onebit =
                values.append(self.processparams[i][3])#normal =
                values.append(self.processparams[i][4])#svent =
                values.append(self.processparams[i][5])#tras =
                values.append(self.processparams[i][6])#wini =
                values.append(self.processparams[i][7])#wfin =
                values.append(self.processparams[i][8])#fini =
                values.append(self.processparams[i][9])#ffin =
                values.append(self.processparams[i][10])#smax =
                values.append(self.processparams[i][11])#tlta =
                values.append(self.processparams[i][12])#porc1 =
                values.append(self.processparams[i][13])#porc2 =
                values.append(self.processparams[i][14])#new_dt =
                values.append(self.processparams[i][15])#new_df =
                values.append(self.meankN[i])  # spectreNS =   # list
                values.append(self.meankE[i])  # spectreEW =   # list
                values.append(self.meankV[i])  # spectreVE =   # list
                values.append(self.HV[i].iloc[:, 0].to_numpy())  # frec_large =   # DataFrame 'f','HVSR'
                values.append(self.HV[i].iloc[:, 1].to_numpy())  # HV_large =
            else:
                values.append(None)  # konno =
                values.append(None)  # taper =
                values.append(None)  # onebit =
                values.append(None)  # normal =
                values.append(None)  # svent =
                values.append(None)  # tras =
                values.append(None)  # wini =
                values.append(None)  # wfin =
                values.append(None)  # fini =
                values.append(None)  # ffin =
                values.append(None)  # smax =
                values.append(None)  # tlta =
                values.append(None)  # porc1 =
                values.append(None)  # porc2 =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                values.append(None)  # porc2 =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
            ## PARAMETROS DE INVERSION
            values.append(self.invertidos[i])#invertido =
            if self.invertidos[i]==True:
                values.append(self.inverparams[i][0])#smin =
                values.append(self.inverparams[i][1])#smax =
                values.append(self.inverparams[i][2])#pmin =
                values.append(self.inverparams[i][3])#pmax =
                values.append(self.inverparams[i][4])#dmin =
                values.append(self.inverparams[i][5])#dmax =
                values.append(self.inverparams[i][6])#prof =
                values.append(self.inverparams[i][7])#firstthick =
                values.append(self.inverparams[i][8])#ncapas =
                values.append(self.inverparams[i][9])#iter =
                values.append(self.inverparams[i][10])#parts =
                values.append(self.inverparams[i][11])#Wini =
                values.append(self.inverparams[i][12])#Wamor =
                values.append(self.inverparams[i][13])#C1 =
                values.append(self.inverparams[i][14])#C2 =
                values.append(self.inverparams[i][15])#Vmax =
                values.append(self.inverparams[i][16])#fini =
                values.append(self.inverparams[i][17])#vsgrad =
                values.append(self.inverparams[i][18])#vpgrad =
                values.append(self.inverparams[i][19])#dengrad =
                values.append(self.Ajuste[i].iloc[:, 0].to_numpy())  # f200 =   # DataFrame "# frecuencia", "average", "stdminus", "stdplus"
                values.append(self.Ajuste[i].iloc[:, 2].to_numpy())  # HV200 =
                values.append(self.Inver[i].iloc[:, 0].to_numpy())  # Inver_prof =   # DataFrame 0,1,2,3
                values.append(self.Inver[i].iloc[:, 1].to_numpy())  # Inver_vp =
                values.append(self.Inver[i].iloc[:, 2].to_numpy())  # Inver_vs =
                values.append(self.Inver[i].iloc[:, 3].to_numpy())  # Inver_rho =
                values.append(self.Ajuste[i].iloc[:, 1].to_numpy())  # Ajuste =   # DataFrame 0,1,2 (freq, ajuste, HV200)
                values.append(self.Convergence[i].iloc[:, 0].to_numpy())  # Convergence =   # Dataframe 0 ()
            else:
                values.append(None)  # konno =
                values.append(None)  # taper =
                values.append(None)  # onebit =
                values.append(None)  # normal =
                values.append(None)  # svent =
                values.append(None)  # tras =
                values.append(None)  # wini =
                values.append(None)  # wfin =
                values.append(None)  # fini =
                values.append(None)  # ffin =
                values.append(None)  # smax =
                values.append(None)  # tlta =
                values.append(None)  # porc1 =
                values.append(None)  # porc2 =
                values.append(None)  # new_dt =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =
                values.append(None)  # new_df =

            values.append(self.crudos[i].iloc[:, 0].to_numpy())#VE =   # Dataframe {'VE', 'NS', 'EW'}
            values.append(self.crudos[i].iloc[:, 1].to_numpy())#NS =
            values.append(self.crudos[i].iloc[:, 2].to_numpy())#EW =
            
        dicts={}
        i=0
        for j in key_names:
            dicts[j]=values[i]
            i += 1
        
        with open(name, 'w') as f:
            for key, value in dicts.items():
                try:
                    if len(value) > 1:
                        f.write('%s:' % (key))
                        f.write(','.join(map(str, value)))
                        f.write('\n')
                except:
                    f.write('%s:%s\n' % (key, value))
                    
                    
            """self.list_proy.append(self.archi)
        self.list_proy.append(self.names)
        self.list_proy.append(self.procesados)
        self.list_proy.append(self.konno)
        self.list_proy.append(self.taper)
        self.list_proy.append(self.onebit)
        self.list_proy.append(self.normal)
        self.list_proy.append(self.svent)
        self.list_proy.append(self.tras)
        self.list_proy.append(self.wini)
        self.list_proy.append(self.wfin)
        self.list_proy.append(self.fini)
        self.list_proy.append(self.ffin)
        self.list_proy.append(self.tlta)
        self.list_proy.append(self.porc1)
        self.list_proy.append(self.porc2)
        self.list_proy.append(self.new_dt)
        self.list_proy.append(self.new_df)
        self.list_proy.append(self.spectreVE)
        self.list_proy.append(self.spectreNS)
        self.list_proy.append(self.spectreEW)
        self.list_proy.append(self.frec_large)
        self.list_proy.append(self.HV_large)
        self.list_proy.append(self.invertidos)
        self.list_proy.append(self.smin)
        self.list_proy.append(self.smax)
        self.list_proy.append(self.pmin)
        self.list_proy.append(self.pmax)
        self.list_proy.append(self.dmin)
        self.list_proy.append(self.dmax)
        self.list_proy.append(self.prof)
        self.list_proy.append(self.firstthick)
        self.list_proy.append(self.ncapas)
        self.list_proy.append(self.iter)
        self.list_proy.append(self.parts)
        self.list_proy.append(self.Wini)
        self.list_proy.append(self.Wamor)
        self.list_proy.append(self.C1)
        self.list_proy.append(self.C2)
        self.list_proy.append(self.Vmax)
        self.list_proy.append(self.vsgrad)
        self.list_proy.append(self.vpgrad)
        self.list_proy.append(self.dengrad)
        self.list_proy.append(self.f200)
        self.list_proy.append(self.HV200)
        self.list_proy.append(self.Inver_prof)
        self.list_proy.append(self.Inver_vp)
        self.list_proy.append(self.Inver_vs)
        self.list_proy.append(self.Inver_rho)
        self.list_proy.append(self.Ajuste)
        self.list_proy.append(self.)"""        
            '''










