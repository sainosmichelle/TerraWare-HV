from HVmodules.NModule import *
import HVmodules.vel_model2 as vel_model2

class inver_DB():
    def __init__(self,name):
        self.HV=0
        self.HV200=0
        self.nombre=name
        self.smin = 0
        self.smax = 0
        self.pmin = 0
        self.pmax = 0
        self.dmin = 0
        self.dmax = 0
        self.prof = 0
        self.firstthick = 0
        self.ncapas = 0
        self.iter = 0
        self.parts = 0
        self.Wini = 0
        self.Wamor = 0
        self.C1 = 0
        self.C2 = 0
        self.Vmax = 0
        self.df =0.01
        self.fini= 0.1
        self.vsgrad = 0.009
        self.vpgrad = 0.01
        self.dengrad = 0.02
        self.adjust = 0
        self.results = 0
        self.conv = 0
        self.invertido= False
        self.params_list=[]
        self.adjusts_N=0
        self.results_N=0
        self.results2=0
        self.lines2D_vp = []
        self.lines2D_vs = []
        self.lines2D_den = []
        self.dialogmodel = QtWidgets.QDialog()
        self.modified_model = vel_model2.Ui_ModVel()
        self.basement = 1

    def parametros_process(self):
        self.params_list.append(self.smin)
        self.params_list.append(self.smax)
        self.params_list.append(self.pmin)
        self.params_list.append(self.pmax)
        self.params_list.append(self.dmin)
        self.params_list.append(self.dmax)
        self.params_list.append(self.prof)
        self.params_list.append(self.firstthick)
        self.params_list.append(self.ncapas)
        self.params_list.append(self.iter)
        self.params_list.append(self.parts)
        self.params_list.append(self.Wini)
        self.params_list.append(self.Wamor)
        self.params_list.append(self.C1)
        self.params_list.append(self.C2)
        self.params_list.append(self.Vmax)
        self.params_list.append(self.fini)
        self.params_list.append(self.vsgrad)
        self.params_list.append(self.vpgrad)
        self.params_list.append(self.dengrad)
        #self.params_list.append(self.basement)
        return self.params_list

    def setHV(self,HV, HV200):
        self.HV = HV
        self.HV200 = HV200

    def printParams(self,progress,sub1,sub2):
        path=os.path.dirname(os.path.abspath(__file__))
        path2=os.getcwd()
        winpath=os.path.join(path2,os.path.join('HVmodules',os.path.join('Inversion',"Project1.exe")))
        print(winpath)
        a=[]
        a.append(self.prof)
        a.append(self.firstthick)
        a.append(self.ncapas)
        a.append(self.pmin)
        a.append(self.pmax)
        a.append(self.smin)
        a.append(self.smax)
        a.append(self.dmin)
        a.append(self.dmax)
        a.append(self.iter)
        a.append(self.parts)
        a.append(self.Wini)
        a.append(self.Wamor)
        a.append(self.C1)
        a.append(self.C2)
        a.append(self.Vmax)
        a.append(self.df)
        a.append(self.fini)
        a.append(self.vsgrad)
        a.append(self.vpgrad)
        a.append(self.dengrad)
        a.append(self.basement)
        d={self.nombre: pd.Series(a)}
        df=pd.DataFrame(d)
        df.to_csv(os.path.join(os.path.join("HVmodules", "Inversion"), 'last_params.txt'), sep='\t', index=False, header=False)
        df.to_csv("last_params.txt", sep='\t', index=False, header=False)
        df.to_csv(os.path.join(os.path.join("HVmodules", "Inversion"), 'parametros_inv.txt'), sep='\t', index=False,
                  header=False)
        df.to_csv("parametros_inv.txt", sep='\t', index=False, header=False)
        progress.setValue(30)
        if platform.system()=='Linux':
            try:
                os.system("./link")
            except:
                os.system("sh link")
        elif platform.system()=='Windows':
            try:
                print("Ejecutando inversion")
                os.system(winpath)
                print("Termino de inversión")
                #os.startfile(r"C:\Users\GTM_USER\Documents\TERRAWARE-HV_WINDOWS\Project1.exe")
                #os.system("Project1.exe")
            except:
                print("No se pudo leer el ejecutable")
            #print ('Ejecución exitosa')
        elif platform.system()=='Darwin':
            print ('Pendiente')
        progress.setValue(80)
        self.saveResults()
        self.plotModel(sub1)
        progress.setValue(90)
        self.plotInversion(sub2)
        self.conv = pd.read_csv("ConvergenceETotal.txt", sep='\s+', header=None)
        #os.system("cd link")
        #os.system("ls")

    def changeDmin(self, val):
        self.dmin = val

    def changeDmax(self, val):
        self.dmax = val

    def changeSmin(self, val):
        self.smin = val

    def changeSmax(self, val):
        self.smax = val

    def changePmin(self, val):
        self.pmin = val

    def changePmax(self, val):
        self.pmax = val

    def changeProf(self, val):
        self.prof = val

    def changefirstthick(self, val):
        self.firstthick = val

    def changeNcapas(self, val):
        self.ncapas= val

    def changeIter(self, val):
        self.iter= val

    def changeIter(self, val):
        self.iter= val

    def changeParts(self,val):
        self.parts = val

    def changeWini(self, val):
        self.Wini = val

    def changeWamor(self, val):
        self.Wamor = val

    def changeC1(self, val):
        self.C1 = val

    def changeC2(self, val):
        self.C2 = val

    def changeVmax(self, val):
        self.Vmax = val

    def changeVpgrad(self, val):
        self.vpgrad = val

    def changeVsgrad(self, val):
        self.vsgrad = val

    def changeDengrad(self, val):
        self.dengrad = val

    def setHV(self,HV, HV200):
        self.HV = HV
        self.HV200 = HV200

    def plotConvergence(self, sub):
        ax1 = sub.add_subplot(111)
        ax1.loglog(self.conv.iloc[:,0], "mediumvioletred")
        #ax1.set_xscale("log")
        #ax1.set_yscale("log")
        ax1.set_xlabel('Iteraciones')
        ax1.set_ylabel('Error del ajuste total')
        ax1.grid(True,which="both",ls="-")
        ax1.set_title("Convergencia de estación "+self.nombre)
        #ax1.grid(which='minor', color='k', linestyle=':')
        #ax1.grid(which='major', color='k', linestyle=':')
        #ax1.tick_params(axis='both', which='minor')#, labelsize=0)
        #ax1.tick_params(axis='x', which='major')
        #ax1.tick_params(axis='y', which='major')
        #minimo = np.min(conv.iloc[:, 0])  # np.min(HV - std)0
        #maximo = np.max(conv.iloc[:, 0])  # np.max(HV + std)
        #max_X= len(conv.iloc[:, 0])
        #for ii in range(10):
        #    x = (maximo-minimo)/(10.0-1) *ii
        #    ax1.plot(np.linspace(0, max_X, 5), [x]*5, "k", linestyle=":", linewidth=0.5)
        #mingridx = np.linspace(0.1, 20.0, 100)
        #for ii in mingridx:
        #    ax1.plot([ii] * 5, np.linspace(minimo, maximo, 5), "lightgrey", linestyle=":", linewidth=0.5)
        #ax1.set_ylim(minimo, maximo)
        #ax1.set_xlim(0, len(conv.iloc[:, 0]))

    def saveResults(self):
        try:
            self.adjust = pd.read_csv("DataHVSR.dat", sep='\s+', header=None)
            self.results = pd.read_csv("InvertModelHVSR.dat", sep='\s+', header=None)
            self.adjusts_N = pd.read_csv("Ajustes100HVSR.dat", sep='\s+', header=None)
            self.results_N = pd.read_csv("Models100HVSR.dat", sep='\s+', header=None)
            bal1=np.full(len(self.results), np.inf)
            bal=np.full(len(self.results_N), np.inf)
            self.results_N[3]=bal
            #print("head1")
            #print(self.results_N.head())
            self.results[4]=bal1
            for i in range(len(self.results_N)):
                self.results_N.at[i,3]=np.sqrt(2*self.results_N.iloc[i,1]**2*(1.0-self.results_N.iloc[i,0])/(1.0-2.0*self.results_N.iloc[i,0]))
            for i in range(len(self.results)):
                self.results.at[i,4] = np.sqrt(2*self.results.iloc[i, 2]**2 *(1.0 - self.results.iloc[i, 1]) / (
                                1.0 - 2.0 * self.results.iloc[i, 1]))
            #print("head2")
            #print(self.results_N.head())
        except:
            print("Entra except")
            pass
        for i in range(2, len(self.results.iloc[:,0])):
            if self.results.iloc[i,0]==self.results.iloc[i-1,0]:
                self.results.iloc[i, 0]=self.results.iloc[i, 0]+0.01

    def plotModel(self, sub):
        matplotlib.rcParams['axes.linewidth'] = 1.5  # set the value globally
        spacingyma = 1.
        majorLocator = MultipleLocator(spacingyma)
        spacingymi = 0.5
        minorLocatory = MultipleLocator(spacingymi)
        ax1 = sub.add_subplot(111)
        long=200
        nmodels=int(len(self.adjusts_N)/long)
        try:
            ax1.plot(self.HV['f'], self.HV['HVSR'], 'k', label='HV Observado')
            minimo = np.min(self.HV['HVSR'])  # np.min(HV - std)0
            maximo = np.max(self.HV['HVSR'])  # np.max(HV + std)
            ax1.set_xlim(left=np.min(self.HV['f']), right=np.max(self.HV['f']))
        except:
            ax1.plot(self.HV.iloc[:,0], self.HV.iloc[:,1], 'k', label='HV Observado')
            minimo = np.min(self.HV.iloc[:,1])  # np.min(HV - std)0
            maximo = np.max(self.HV.iloc[:,1])  # np.max(HV + std)
            ax1.set_xlim(left=np.min(self.HV.iloc[:,0]), right=np.max(self.HV.iloc[:,0]))
        #inv=pd.read_csv("DataHVSR.dat",  sep='\s+', header=None)
        self.saveResults()

        #for i in range(nmodels-1):
        #    ax1.plot(self.adjust.iloc[:,0], self.adjusts_N[i*200:(i+1)*200,0],  alpha=0.1)

        ax1.plot(self.adjust.iloc[:,0], self.adjust.iloc[:,1], '--b', linewidth=1, label='HV Invertido')
        for ii in range(10):
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "k", linestyle=":", linewidth=0.5)
        #mingridx = np.linspace(0.1, 20.0, 100)
        mingridx = np.linspace(0.1, 100.0, 200)
        for ii in mingridx:
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "lightgrey", linestyle=":", linewidth=0.5)
        ax1.legend(loc="upper right")
        ax1.set_xscale("symlog")
        ax1.set_yscale("linear")
        ax1.set_ylabel('Amplitud')
        ax1.set_xlabel('Frecuencia (Hz)')
        ax1.yaxis.set_minor_locator(minorLocatory)
        ax1.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
        ax1.yaxis.set_major_locator(majorLocator)
        ax1.grid(which='major', color='k', linestyle=':')  # , linewidth=3)
        ax1.tick_params(axis='both', which='minor')  # , labelsize=45)
        ax1.tick_params(axis='x', which='major')  # , labelsize=45)
        ax1.tick_params(axis='y', which='major')  # , labelsize=45)
        ax1.set_ylim(minimo - 0.5, maximo + 1.2)
        ax1.set_title("Modelo invertido vs. modelo observado estación "+self.nombre)

    def plotInversion(self, sub):
        self.sub=sub
        self.long=int(self.ncapas*2)
        self.nmodels=int(self.results_N.shape[0]/self.long)
        #print()
        #print("nmodelos: %d"%(self.results_N.shape[0]/self.long))
        #print("long: %d"%(self.ncapas*2))
        #print("renglones: %d" % (self.results_N.shape[0]))
        #print()
        # print("%d : %d"%((nmodels-1)*long,nmodels*long))
        self.results.iloc[-1, 0] = self.results.iloc[-2, 0] + self.results.iloc[-2, 0] / 3.0
        ax1 = self.sub.add_subplot(1, 4, 1)
        self.ax2 = self.sub.add_subplot(1, 4, 2)
        ax3 = self.sub.add_subplot(1, 4, 3)
        ax4 = self.sub.add_subplot(1, 4, 4)
        #print("Nmodels: ",self.nmodels)
        #print("long: ", self.long)
        for i in range(self.nmodels-1):
            #print("%d : %d"%(i*self.long,(i+1)*self.long))
            ax1.plot(self.results_N.iloc[i*self.long:(i+1)*self.long, 3], -self.results.iloc[:, 0],  alpha=0.3)
            self.ax2.plot(self.results_N.iloc[i*self.long:(i+1)*self.long, 1], -self.results.iloc[:, 0], linewidth=1,alpha=0.4, picker=True)
            ax3.plot(self.results_N.iloc[i*self.long:(i+1)*self.long, 2], -self.results.iloc[:, 0], alpha=0.3)
            ax4.plot(self.results_N.iloc[i * self.long:(i + 1) * self.long, 0], -self.results.iloc[:, 0], alpha=0.3)
        #print()
        #print("nmodelos: %d"%(self.results_N.shape[0]/long))
        #print("long: %d"%(self.ncapas*2))
        #print("renglones: %d" % (self.results_N.shape[0]))
        #print()
        #print("%d : %d"%((nmodels-1)*long,nmodels*long))
        ax1.plot(self.results_N.iloc[(self.nmodels - 1) * self.long:self.nmodels * self.long, 3], -self.results.iloc[:, 0], 'k')
        self.ax2.plot(self.results_N.iloc[(self.nmodels-1)*self.long:self.nmodels*self.long, 1], -self.results.iloc[:, 0], 'k',linewidth=1.5, picker=True)
        ax3.plot(self.results_N.iloc[(self.nmodels - 1) * self.long:self.nmodels * self.long, 2], -self.results.iloc[:, 0], 'k')
        ax4.plot(self.results_N.iloc[(self.nmodels - 1) * self.long:self.nmodels * self.long, 0],-self.results.iloc[:, 0], 'k')
        #ax1.plot(self.results.iloc[:, 1], -self.results.iloc[:, 0], '--r')
        #ax2.plot(self.results.iloc[:, 2], -self.results.iloc[:, 0], '--r', picker=1)
        #ax3.plot(self.results.iloc[:, 3], -self.results.iloc[:, 0], '--r')

        ax1.set_yscale("linear")
        ax1.set_xscale("linear")
        ax1.set_xlabel(r'Velocidad ($\frac{m}{s}$)')
        ax1.set_ylabel('Profundidad (m)')

        ax1.set_title('VP', y=1.02)
        ax1.tick_params(axis='x', which='major')
        ax1.tick_params(axis='y', which='major')
        ax1.tick_params(axis='both', which='minor')
        ax1.grid(b=True, which='minor', color='k', linestyle=':')
        ax1.grid(b=True, which='major', color='k', linestyle=':')
        ax1.set_xlim(np.min(self.results.iloc[:, 4]) - 500, np.max(self.results.iloc[:, 4]) + 500)
        ax1.set_ylim(-np.max(self.results.iloc[:, 0]), 0.0)

        self.ax2.set_title('VS', y=1.02)
        self.ax2.tick_params(axis='y', which='major', labelsize=0)
        self.ax2.tick_params(axis='y', which='minor', labelsize=0)
        self.ax2.tick_params(axis='x', which='major')
        self.ax2.tick_params(axis='x', which='minor')
        self.ax2.grid(b=True, which='minor', color='grey', linestyle=':')
        self.ax2.grid(b=True, which='major', color='k', linestyle=':')
        self.ax2.set_xlabel(r'Velocidad ($\frac{m}{s}$)')
        self.ax2.set_xlim(0.0, np.max(self.results.iloc[:, 2]) + 200)
        self.ax2.set_ylim(-np.max(self.results.iloc[:, 0]), 0.0)

        ax3.set_title('Densidades', y=1.02)
        ax3.tick_params(axis='y', which='major', labelsize=0)
        ax3.tick_params(axis='y', which='minor', labelsize=0)
        ax3.tick_params(axis='x', which='major')
        ax3.tick_params(axis='x', which='minor')
        ax3.grid(b=True, which='minor', color='grey', linestyle=':')
        ax3.grid(b=True, which='major', color='k', linestyle=':')
        ax3.set_xlabel(r'Densidad ($\frac{kg}{m^3}$)')
        ax3.set_xlim(np.min(self.results.iloc[:, 3]) - 500, np.max(self.results.iloc[:, 3]) + 500)
        ax3.set_ylim(-np.max(self.results.iloc[:, 0]), 0.0)

        ax4.set_title('Poisson', y=1.02)
        ax4.tick_params(axis='y', which='major', labelsize=0)
        ax4.tick_params(axis='y', which='minor', labelsize=0)
        ax4.tick_params(axis='x', which='major')
        ax4.tick_params(axis='x', which='minor')
        ax4.grid(b=True, which='minor', color='grey', linestyle=':')
        ax4.grid(b=True, which='major', color='k', linestyle=':')
        #ax4.set_xlabel(r'')
        ax4.set_xlim(np.min(self.results.iloc[:, 1]) - 0.05, np.max(self.results.iloc[:, 1]) + 0.05)
        ax4.set_ylim(-np.max(self.results.iloc[:, 0]), 0.0)

        self.clickconnect = self.sub.canvas.mpl_connect('pick_event', self.onpick)


    def replot(self,mod):
        print("replot")
        print(mod)
        #print("%d : %d" % (i * self.long, (i + 1) * self.long))
        PROF = [-1*self.results.iloc[i, 0] for i in range(self.results.shape[0])]
        VPP = self.results_N.iloc[mod*self.long : (mod + 1)*self.long, 3].values.tolist()
        VSS = self.results_N.iloc[mod*self.long : (mod + 1)*self.long, 1].values.tolist()
        DEN = self.results_N.iloc[mod*self.long : (mod + 1)*self.long, 2].values.tolist()
        POI = self.results_N.iloc[mod*self.long : (mod + 1)*self.long, 0].values.tolist()
        AJUS = self.adjusts_N.iloc[mod*200 : (mod + 1)*200,0].values.tolist()

        self.modified_model.setupUi(self.dialogmodel, PROF, VPP, VSS, DEN, AJUS, POI)
        self.dialogmodel.open()
        #self.sub.clf()
        """fig = Figure()
        p = FigureCanvas(fig)
        
        self.mdiArea_HV.layout.addWidget(p)
        self.mdiArea_HV.layout.setMenuBar(NavigationToolbar(p, self.mdiArea_HV))
        self.mdiArea_HV.plotsis = p.figure
        fig.suptitle('Ajuste de Modelo Invertido ' + self.inversion.nombre)
        self.inversion.plotModel(self.mdiArea_HV.plotsis)"""


    def onpick (self,event):
        #long = self.ncapas * 2
        #nmodels = int(self.results_N.shape[0] / long)
        #print("artist:")
        #print(dir(event.artist))
        #print()
        #print(event.artist.get_ydata())
        #print()

        #if event.artist != line: return True

        N = len(event.ind)
        if not N:
            return True

        for i in range(self.nmodels):
            index=0
            l=0
            for j in range(i*self.long,(i+1)*self.long):
                if event.artist.get_xdata()[l] == self.results_N.iloc[j, 1]:
                    index += 1
                l +=1
            if index == self.long:
                modelo=i
        self.replot(modelo)
        self.sub.canvas.mpl_disconnect(self.clickconnect)
        self.modelo=modelo



    def showHV(self,sub):
        matplotlib.rcParams['axes.linewidth'] = 1.5  # set the value globally
        spacingyma = 1.
        majorLocator = MultipleLocator(spacingyma)
        spacingymi = 0.5
        minorLocatory = MultipleLocator(spacingymi)
        ax1 = sub.add_subplot(111)
        try:
            ax1.plot(self.HV['f'], self.HV['HVSR'], 'k')
            minimo = np.min(self.HV['HVSR'])  # np.min(HV - std)
            maximo = np.max(self.HV['HVSR'])  # np.max(HV + std)
            ax1.set_xlim(left=np.min(self.HV['f']), right=np.max(self.HV['f']))
        except:
            ax1.plot(self.HV.iloc[:,0], self.HV.iloc[:,1], 'k')
            minimo = np.min(self.HV.iloc[:,1])  # np.min(HV - std)
            maximo = np.max(self.HV.iloc[:,1])  # np.max(HV + std)
            ax1.set_xlim(left=np.min(self.HV.iloc[:,0]), right=np.max(self.HV.iloc[:,0]))
        #ax1.plot(f, stdplus, 'k', linestyle=":")
        #ax1.plot(f, stdminus, 'k', linestyle=":")
        for ii in range(10):
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "k", linestyle=":", linewidth=0.5)
        #mingridx = np.linspace(0.1, 20.0, 100)
        mingridx = np.linspace(0.1, 100.0, 200)
        for ii in mingridx:
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "lightgrey", linestyle=":", linewidth=0.5)
        # ax1.legend(prop={'size': 55}, loc="upper right")
        ax1.set_xscale("symlog")
        ax1.set_yscale("linear")
        ax1.set_ylabel('Amplitud')
        ax1.set_xlabel('Frecuencia (Hz)')
        ax1.yaxis.set_minor_locator(minorLocatory)
        ax1.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
        ax1.yaxis.set_major_locator(majorLocator)
        ax1.grid(which='major', color='k', linestyle=':')  # , linewidth=3)
        ax1.tick_params(axis='both', which='minor')  # , labelsize=45)
        ax1.tick_params(axis='x', which='major')  # , labelsize=45)
        ax1.tick_params(axis='y', which='major')  # , labelsize=45)
        ax1.set_ylim(minimo - 0.1, maximo + 1.2)
        ax1.set_title("H/V observado de estación "+self.nombre)

