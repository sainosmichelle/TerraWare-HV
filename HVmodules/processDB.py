from HVmodules.NModule import *
import copy
import HVmodules.konno_ohmachi as konno

class process_DB():
    def __init__(self,currentIndex,safpath=""):
        #self.archi = 0
        self._nombre = "ninguno";
        self._dt = 0;
        self._delf = 0;
        self._tini = 0;
        self._tfin = 0;
        self._VE = 0;
        self._NS = 0;
        self._EW = 0;
        self._nmues = 0;
        self._currentIndex=currentIndex
        self._Ventana = 0; #ventana_process_form2.Ui_Ventana_procesamiento()
        self._procesado = False
        try:
            self.read_single(safpath)
        except:
            pass
        self._HV200=0
        self._fr=0
        self._HV=0
        self._meankN = 0
        self._meankE = 0
        self._meankV = 0
        self._stdminus=0
        self._stdplus=0
        self._params_list = []
        self._fNSs = 0
        self._fEWs = 0
        self._fVEs = 0
        #self.Ventana = ventana_process_form2.Ui_Ventana_procesamiento(file, currentIndex)
        self._konno = None
        self._taper = None
        self._onebit = False
        self.baseline =False
        self._normal = None
        self._svent = None
        self._tras = None
        self._wini = None  # 1e-05
        self._wfin = None  # 99.0
        self._fini = None
        self._ffin = None
        self._smax = None  # 5
        #self._tlta = None  # 500
        self._porc1 = None
        self._porc2 = None
        self._new_dt = None
        # self.new_dt = 0.005
        self._new_df = None # 0.05
        self.orden_butter = 6
        self._NSvif = None
        self._EWvif = None
        self._VEvif = None
        self._vi = None
        self._vf = None
        self._wincleantot = None
        self.color_names = np.asarray(['tomato', 'brown', 'forestgreen', 'darkgoldenrod', 'violet', 'darkgray',
                                       'deepskyblue', 'sienna', 'darkslategrey', 'teal', 'greenyellow', 'darkkhaki',
                                       'gold', 'seagreen', 'lawngreen', 'mediumturquoise', 'springgreen',
                                       'firebrick', 'peachpuff', 'cornflowerblue', 'darkgrey', 'mediumblue',
                                       'royalblue',
                                       'chartreuse', 'deeppink', 'blueviolet', 'mediumseagreen', 'darksalmon',
                                       'burlywood',
                                       'orchid', 'mediumvioletred', 'gainsboro', 'darkturquoise', 'magenta', 'hotpink',
                                       'rebeccapurple', 'navy', 'moccasin', 'goldenrod', 'skyblue', 'sandybrown',
                                       'paleturquoise',
                                       'steelblue', 'darkorchid', 'darkslateblue', 'limegreen', 'midnightblue',
                                       'palegoldenrod',
                                       'darkcyan', 'yellowgreen', 'darkred', 'darkmagenta', 'palevioletred', 'green',
                                       'dodgerblue', 'olive', 'mediumslateblue', 'mediumaquamarine', 'turquoise',
                                       'indianred',
                                       'slategray', 'lime', 'darkseagreen', 'blanchedalmond', 'mediumpurple', 'fuchsia',
                                       'darkviolet', 'slateblue', 'aquamarine', 'maroon', 'cadetblue', 'peru', 'orange',
                                       'plum', 'gray', 'khaki', 'saddlebrown', 'yellow', 'cyan', 'indigo',
                                       'mediumspringgreen',
                                       'chocolate', 'olivedrab', 'tan', 'orangered', 'powderblue', 'coral',
                                       'darkslategray', 'aqua', 'purple', 'slategrey', 'rosybrown', 'darkblue',
                                       'crimson',
                                       'darkolivegreen', 'blue', 'mediumorchid', 'red', 'pink', 'palegreen',
                                       'darkgreen', 'salmon', 'grey', 'darkorange'])

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,val):
        self._nombre = val

    @property
    def dt(self):
        return self._dt
    @dt.setter
    def dt(self,val):
        self._dt=val

    @property
    def delf(self):
        return self._delf
    @delf.setter
    def delf(self, val):
        self._delf = val

    @property
    def tini(self):
        return self._tini
    @tini.setter
    def tini(self, val):
        self._tini = val

    @property
    def tfin(self):
        return self._tfin
    @tfin.setter
    def tfin(self, val):
        self._tfin = val

    @property
    def VE(self):
        return self._VE
    @VE.setter
    def VE(self, val):
        self._VE = val

    @property
    def NS(self):
        return self._NS
    @NS.setter
    def NS(self, val):
        self._NS = val

    @property
    def EW(self):
        return self._EW
    @EW.setter
    def EW(self, val):
        self._EW = val

    @property
    def nmues(self):
        return self._nmues
    @nmues.setter
    def nmues(self, val):
        self._nmues = val

    @property
    def currentIndex(self):
        return self._currentIndex
    @currentIndex.setter
    def currentIndex(self, val):
        self._currentIndex = val

    @property
    def Ventana(self):
        return self._Ventana
    @Ventana.setter
    def Ventana(self, val):
        self._Ventana = val

    @property
    def procesado(self):
        return self._procesado
    @procesado.setter
    def procesado(self, val):
        self._procesado = val

    @property
    def HV200(self):
        return self._HV200
    @HV200.setter
    def HV200(self, val):
        self._HV200 = val

    @property
    def fr(self):
        return self._fr
    @fr.setter
    def fr(self, val):
        self._fr = val

    @property
    def HV(self):
        return self._HV
    @HV.setter
    def HV(self, val):
        self._HV = val

    @property
    def meankN(self):
        return self._meankN
    @meankN.setter
    def meankN(self, val):
        self._meankN = val

    @property
    def meankE(self):
        return self._meankE
    @meankE.setter
    def meankE(self, val):
        self._meankE = val

    @property
    def meankV(self):
        return self._meankV
    @meankV.setter
    def meankV(self, val):
        self._meankV = val

    @property
    def stdminus(self):
        return self._stdminus
    @stdminus.setter
    def stdminus(self, val):
        self._stdminus = val

    @property
    def stdplus(self):
        return self._stdplus
    @stdplus.setter
    def stdplus(self, val):
        self._stdplus = val

    @property
    def params_list(self):
        return self._params_list
    @params_list.setter
    def params_list(self, val):
        self._params_list = val

    @property
    def fNSs(self):
        return self._fNSs
    @fNSs.setter
    def fNSs(self, val):
        self._fNSs = val

    @property
    def fEWs(self):
        return self._fEWs
    @fEWs.setter
    def fEWs(self, val):
        self._fEWs = val

    @property
    def fVEs(self):
        return self._fVEs
    @fVEs.setter
    def fVEs(self, val):
        self._fVEs = val

    @property
    def konno(self):
        return self._konno
    @konno.setter
    def konno(self, val):
        self._konno = val

    @property
    def taper(self):
        return self._taper
    @taper.setter
    def taper(self, val):
        self._taper = val

    @property
    def onebit(self):
        return self._onebit
    @onebit.setter
    def onebit(self, val):
        self._onebit = val

    @property
    def normal(self):
        return self._normal
    @normal.setter
    def normal(self, val):
        self._normal = val

    @property
    def svent(self):
        return self._svent
    @svent.setter
    def svent(self, val):
        self._svent = val

    @property
    def tras(self):
        return self._tras
    @tras.setter
    def tras(self, val):
        self._tras = val

    @property
    def wini(self):
        return self._wini
    @wini.setter
    def wini(self, val):
        self._wini = val

    @property
    def wfin(self):
        return self._wfin
    @wfin.setter
    def wfin(self, val):
        self._wfin = val

    @property
    def fini(self):
        return self._fini
    @fini.setter
    def fini(self, val):
        self._fini = val

    @property
    def ffin(self):
        return self._ffin
    @ffin.setter
    def ffin(self, val):
        self._ffin = val

    @property
    def smax(self):
        return self._smax
    @smax.setter
    def smax(self, val):
        self._smax = val

    #@property
    #def tlta(self):
    #    return self._tlta
    #@tlta.setter
    #def tlta(self, val):
    #    self._tlta = val

    @property
    def porc1(self):
        return self._porc1
    @porc1.setter
    def porc1(self, val):
        self._porc1 = val

    @property
    def porc2(self):
        return self._porc2
    @porc2.setter
    def porc2(self, val):
        self._porc2 = val

    @property
    def new_dt(self):
        return self._new_dt
    @new_dt.setter
    def new_dt(self, val):
        self._new_dt = val

    @property
    def new_df(self):
        return self._new_df
    @new_df.setter
    def new_df(self, val):
        self._new_df = val

    @property
    def NSvif(self):
        return self._NSvif
    @NSvif.setter
    def NSvif(self, val):
        self._NSvif = val

    @property
    def EWvif(self):
        return self._EWvif
    @EWvif.setter
    def EWvif(self, val):
        self._EWvif = val

    @property
    def VEvif(self):
        return self._VEvif
    @VEvif.setter
    def VEvif(self, val):
        self._VEvif = val

    @property
    def vi(self):
        return self._vi
    @vi.setter
    def vi(self, val):
        self._vi = val

    @property
    def vf(self):
        return self._vf
    @vf.setter
    def vf(self, val):
        self._vf = val

    @property
    def wincleantot(self):
        return self._wincleantot
    @wincleantot.setter
    def wincleantot(self, val):
        self._wincleantot = val

    def smaxChanged(self, val):
        self.smax = val

    #def tltaChanged(self, val):
    #    self.tlta = val

    def porc1Changed(self, val):
        self.porc1 = val

    def porc2Changed(self, val):
        self.porc2 = val

    def konnoValueChanged(self, val):
        self.konno=val

    def taperValueChanged(self, val):
        self.taper=val

    def onebitStateChanged(self,b):
        if b==0:
            self.onebit=False
        else:
            self.onebit=True

    def baselineStateChanged(self,b):
        if b==0:
            self.baseline=False
        else:
            self.baseline=True

    def selectioNormChanged(self,i):
        if i==0:
            self.normal="ENER_UNIT"
        elif i==1:
            self.normal="SUM_ENER"
        elif i==2:
            self.normal="SPEC_WHIT"
        elif i==3:
            self.normal="ENV_TIME"

    def selectionTapChanged(self,i):
        if i==0:
            self.tapwin="tukey"
        elif i==1:
            self.tapwin="hann"
        elif i==2:
            self.tapwin="blackman"
        elif i==3:
            self.tapwin="triangular"
        elif i==4:
            self.tapwin = "cosine"
        elif i==5:
            self.tapwin = "hamming"
        elif i==6:
            self.tapwin = "flattop"
        elif i==7:
            self.tapwin = "boxcar"
        elif i==8:
            self.tapwin = "blackmanharris"

    def sventValueChanged(self, ival):
        self.svent=float(ival)

    def trasValueChanged(self, val):
        self.tras=val

    def winiValueChanged(self, val):
        self.wini=val

    def wfinValueChanged(self, val):
        self.wfin=val

    def wPasaAltas(self,val):
        self.wini=val
        self.wfin=None

    def wPasaBajas(self,val):
        self.wini=None
        self.wfin=val

    def finiValueChanged(self, val):
        self.fini=val

    def ffinValueChanged(self, val):
        self.ffin=val

    def dtValueChanged(self, val):
        self.new_dt=val

    def dfValueChanged(self, val):
        self.new_df=val

    def processParamsDefault(self):
        self.konno = 30.0
        self.taper = 0.05#0.1
        self.onebit = False
        self.baseline =False
        self.normal = "SUM_ENER"
        self.tapwin = "tukey"
        self.svent = 80.0
        self.tras = 0.0
        self.wini = None#1e-05
        self.wfin = None#99.0
        self.fini = 0.1
        self.ffin = 15.0
        self.smax = 1.0  # 5
        self.tlta = 180  # 500
        self.porc1 = 0.90
        self.porc2 = 0.90
        self.new_dt= self.dt
        #self.new_dt = 0.005
        self.new_df = 0.01  # 0.05
        self.NSvif = 0
        self.EWvif = 0
        self.VEvif = 0
        self.vi = 0
        self.vf = 0
        self.wincleantot = 0

    def parametros_process(self):
        self.params_list.append(self.konno)
        self.params_list.append(self.taper)
        self.params_list.append(self.onebit)
        self.params_list.append(self.normal)
        self.params_list.append(self.svent)
        self.params_list.append(self.tras)
        self.params_list.append(self.wini)
        self.params_list.append(self.wfin)
        self.params_list.append(self.fini)
        self.params_list.append(self.ffin)
        self.params_list.append(self.smax)
        self.params_list.append(self.tlta)
        self.params_list.append(self.porc1)
        self.params_list.append(self.porc2)
        self.params_list.append(self.new_dt)
        self.params_list.append(self.new_df)
        return self.params_list


    def read_single(self, safpath):
        try:
            f = open(safpath, "r")
            line = []
            encabs = 0
            for jj in range(30):
                line.append(f.readline())
                encabs += 1
                if line[jj].startswith('####--'):
                    break
                if line[jj].startswith('NDAT'):
                    smues = line[jj].split('=')
                    self.nmues = int(smues[1].strip())
                if line[jj].startswith('START_TIME'):
                    datestring = line[jj].split('=')
                    try:
                        self.tini = datetime.datetime.strptime(datestring[1].strip(), '%Y %m %d %H %M %S.%f')
                    except:
                        self.tini = datetime.datetime.strptime(datestring[1].strip(), '%Y %m %d %H %M %S')
                if line[jj].startswith('SAMP_FREQ'):
                    deltaff = line[jj].split('=')
                    self.delf = float(deltaff[1].strip())
            self.dt = (1.0 / self.delf)
            self.tfin = self.tini + datetime.timedelta(seconds=self.nmues * self.dt - self.dt)
            DF = pd.read_csv(safpath, skiprows=encabs, sep="\s+", header=None)
            self.VE = np.array(DF[0])
            self.NS = np.array(DF[1])
            self.EW = np.array(DF[2])
            ndir = safpath.split('/')#(op.sep)
            ndir = ndir[-1].split('.')
            self.nombre = ndir[-2].strip()
        except:
            print('read single; hay un error en arhivo: %s' % self.nombre)

    def saveTmp(self):
        try:
            fnew = np.linspace(self.fr[0], self.fr[-1], 200, endpoint=True)
            HVnew = self.resample_by_interpolation(self.HV, len(self.HV), 200)
            stdminusnew = self.resample_by_interpolation(self.stdminus, len(self.stdminus), 200)
            stdplusnew = self.resample_by_interpolation(self.stdplus, len(self.stdplus), 200)
            #HVlog = resample_by_interpolation_log(self.HV, len(self.HV), 200)
            self.df_or = pd.DataFrame({ "# frecuencia": self.fr, "average": self.HV})
            df_200 = pd.DataFrame({"# frecuencia": fnew, "average": HVnew, "stdminus":stdminusnew, "stdplus":stdplusnew})
            self.HV200 = df_200
            df_200.to_csv("actualHV.txt", index=None,sep='\t', columns=["# frecuencia", "average"], header=None)
        except:
            print("Error en salvar archivo temporal")


    def guardar_HV(self, filesave):
        try:
            jj = [i for i in range(len(self.f_fou)) if self.fini <= self.f_fou[i] < self.ffin]
            fr = self.f_fou[jj]
            SS1 = konno.fast_konno_ohmachi(self.HVSS_1, fr, smooth_coeff=self.konno)
            fnew = np.linspace(self.fr[0], self.fr[-1], 1000, endpoint=True)
            HVnew = self.resample_by_interpolation(self.HV, len(self.HV), 1000)
            SS = self.resample_by_interpolation(SS1, len(SS1), 1000)
            stdminusnew = self.resample_by_interpolation(self.stdminus, len(self.stdminus), 1000)
            stdplusnew = self.resample_by_interpolation(self.stdplus, len(self.stdplus), 1000)
            df_900 = pd.DataFrame(
                {"# frecuencia": fnew, "average": HVnew, "stdminus": stdminusnew, "stdplus": stdplusnew, "SS et.al.":SS})
            #df_200 = self.HV200
            df_900.to_csv(filesave[0], index=None, sep='\t', columns=["# frecuencia", "average", "stdminus", "stdplus", "SS et.al."])
        except:
            print("Error en salvar H/V")

    def guardar_esp_ampl(self, filesave):
        try:
            jj= [i for i in range(len(self.f_fou)) if self.fini<=self.f_fou[i]<self.ffin]
            fr = self.f_fou[jj]
            EW = self.EW_fou[jj]
            NS = self.NS_fou[jj]
            VE = self.VE_fou[jj]
            EW = konno.fast_konno_ohmachi(EW, fr, smooth_coeff=self.konno)
            NS = konno.fast_konno_ohmachi(NS, fr, smooth_coeff=self.konno)
            VE = konno.fast_konno_ohmachi(VE, fr, smooth_coeff=self.konno)
            fnew = np.linspace(self.fr[0], self.fr[-1], 1000, endpoint=True)
            EWnew = self.resample_by_interpolation(EW, len(EW), 1000)
            NSnew = self.resample_by_interpolation(NS, len(NS), 1000)
            VEnew = self.resample_by_interpolation(VE, len(VE), 1000)
            df_900 = pd.DataFrame({"# frecuencia": fnew, "NS": NSnew, "EW": EWnew, "VE": VEnew})
            #df_200 = self.HV200
            df_900.to_csv(filesave[0], index=None, sep='\t', columns=["# frecuencia", "NS", "EW", "VE"])
        except:
            print("Error en salvar espectros de amplitud")

    def guardar_DIRHV(self, filesave):
        try:
            NHV_k = konno.fast_konno_ohmachi(self.NHV, self.f_suav, smooth_coeff=self.konno)
            EHV_k = konno.fast_konno_ohmachi(self.EHV, self.f_suav, smooth_coeff=self.konno)
            fnew = np.linspace(self.f_suav[0], self.f_suav[-1], 1000, endpoint=True)
            HVnew = self.resample_by_interpolation(self.HV_suav, len(self.HV_suav), 1000)
            NHV = self.resample_by_interpolation(NHV_k, NHV_k, 1000)
            EHV = self.resample_by_interpolation(EHV_k, EHV_k, 1000)
            df_DIR = pd.DataFrame({'frec':fnew, 'NS/V':NHV, 'EW/V':EHV, 'H/V average':HVnew})
            df_DIR.to_csv(filesave[0], index=None, sep='\t', columns=["frec", "NS/V", "EW/V", "H/V average"])
        except:
            print("Error en salvar H/V direccionales")

    # DISCLAIMER: This function is copied from https://github.com/nwhitehead/swmixer/blob/master/swmixer.py,
    #             which was released under LGPL.
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

    def registros_plot_single(self, sub):
        '''Graficos de los registros crudos
           x=NS
           y=EW
           z=VE'''
        final_time = self.tini + datetime.timedelta(seconds=len(self.VE) * self.dt)
        time_arr = np.linspace(0, len(self.VE) - 1, len(self.VE))
        #time_arr = np.linspace(self.tini, final_time, len(self.VE))
        #if self.tini != 0.0:
        #time_arr = [self.tini + datetime.timedelta(seconds=jj * self.dt) for jj in range(len(self.VE))]
        #gs1 = gridspec.GridSpec(3, 1)
        ax1 = sub.add_subplot(3, 1, 1)
        #if self.tini != 0.0:
        ax1.plot(time_arr, self.VE, 'teal')
        ax1.set_ylabel('VE')
        ax1.tick_params(axis='both', which='minor')
        ax1.grid(b=True, which='major', color='k', linestyle=':')
        ax2 = sub.add_subplot(3, 1, 2)
        #if self.tini != 0.0:
        ax2.plot(time_arr, self.NS, 'darkslateblue')
        ax2.set_ylabel('NS')
        ax2.tick_params(axis='both', which='minor')
        ax2.grid(b=True, which='major', color='k', linestyle=':')

        ax3 = sub.add_subplot(3, 1, 3)
        #if self.tini != 0.0:
        ax3.plot(time_arr, self.EW, 'maroon')
        ax3.set_xlabel('tiempo')  # , fontsize=30)
        ax3.set_ylabel('EW')      # , fontsize=30)
        ax3.tick_params(axis='both', which='minor')  # , labelsize=25)
        ax3.grid(b=True, which='major', color='k', linestyle=':')

        matplotlib.rc('xtick')  # , labelsize=30)
        matplotlib.rc('ytick')  # , labelsize=18)
        ax1.set_title('Registros Crudos de Estación ' + str(self.nombre)+"\n"+
                      "     tiempo inicial: {},  tiempo final {}".format(self.tini, final_time))  # , fontsize=40)
        #gs1.tight_layout(sub)

    def ventanas_plot(self, sub):
        try:
            final_time =self.tini+datetime.timedelta(seconds=len(self.NSvif)*self.new_dt)
            time_arr1 = np.linspace(0, len(self.NSvif) - 1, len(self.NSvif))
        except:
            final_time = self.tini + datetime.timedelta(seconds=len(self.VEvif) * self.new_dt)
            time_arr1 = np.linspace(0, len(self.VEvif) - 1, len(self.VEvif))

        #time_arr1 = [self.tini + datetime.timedelta(seconds=jj * self.new_dt) for jj in range(len(self.VEvif))]
        zmin = self.VEvif.min()
        zmax = self.VEvif.max()
        #gs1 = gridspec.GridSpec(3, 1)
        ax1 = sub.add_subplot(3, 1, 1)
        ax1.plot(time_arr1, self.VEvif, 'teal')
        np.random.shuffle(self.color_names)
        for i in range(len(self.vi)):
            if self.wincleantot[i] != 0:
                ax1.fill_between(time_arr1[self.vi[i]:self.vf[i]], zmin, zmax, facecolor=random.choice(self.color_names), alpha=0.4)
        ax1.set_ylabel('VE')  # , fontsize=30)
        ax1.tick_params(axis='both', which='minor')  # , labelsize=25)
        ax1.grid(b=True, which='major', color='k', linestyle=':')
        xmin = self.NSvif.min()
        xmax = self.NSvif.max()
        ax2 = sub.add_subplot(3, 1, 2)
        ax2.plot(time_arr1, self.NSvif, 'darkslateblue')
        for i in range(len(self.vi)):
            if self.wincleantot[i] != 0:
                ax2.fill_between(time_arr1[self.vi[i]:self.vf[i]], xmin, xmax, facecolor=random.choice(self.color_names), alpha=0.4)
        ax2.set_ylabel('NS')  # , fontsize=30)
        ax2.tick_params(axis='both', which='minor')  # , labelsize=25)
        ax2.grid(b=True, which='major', color='k', linestyle=':')
        ymin = self.EWvif.min()
        ymax = self.EWvif.max()
        ax3 = sub.add_subplot(3, 1, 3)
        ax3.plot(time_arr1, self.EWvif, 'maroon')
        for i in range(len(self.vi)):
            if self.wincleantot[i] != 0:
                ax3.fill_between(time_arr1[self.vi[i]:self.vf[i]], ymin, ymax, facecolor=random.choice(self.color_names), alpha=0.4)
        ax3.set_ylabel('EW')  # , fontsize=30)
        ax3.set_xlabel('tiempo')
        ax3.tick_params(axis='both', which='minor')  # , labelsize=25)
        ax3.grid(b=True, which='major', color='k', linestyle=':')
        matplotlib.rc('xtick')  # , labelsize=30)
        matplotlib.rc('ytick')  # , labelsize=18)
        ax1.set_title('Ventanas de Estación ' + str(self.nombre) + "\n" +
         "tiempo inicial: {},  tiempo final {}".format(self.tini, final_time))
        #gs1.tight_layout(sub)
        return


    def espectros(self, sub, M, Nespec, fmax):#, NS, EW, Z, M, wincleantot, vi, vf, Nespec, fmax):
        Nvpart = 0
        Nv = 0
        fNS_vent = []
        fEW_vent = []
        fVE_vent = []
        fHH_vent = []
        NS_vent = []
        EW_vent = []
        V_vent = []
        for ii in range(M):
            if self.wincleantot[ii] == 0:
                continue
            NSw = self.NSvif[self.vi[ii]:self.vf[ii]]
            EWw = self.EWvif[self.vi[ii]:self.vf[ii]]
            Zw = self.VEvif[self.vi[ii]:self.vf[ii]]
            if sum(np.abs(EWw)) == 0 or sum(np.abs(NSw)) == 0 or sum(np.abs(Zw)) == 0:
                print
                "Espectros: suma absoluta es 0"
                continue
            f_NSvv_norm, f_EWvv_norm, f_VEvv_norm, NStnorm, EWtnorm, VEtnorm, Nblanfrec = self.normalizacion(NSw,EWw,
                                                                                                           Zw,Nespec)
            fNS_vent.append([np.abs(f_NSvv_norm)])
            fEW_vent.append([np.abs(f_EWvv_norm)])
            fVE_vent.append([np.abs(f_VEvv_norm)])
            fHH_vent.append([np.abs(np.sqrt((f_NSvv_norm ** 2 + f_EWvv_norm ** 2) / 2))])
            Nv += 1
            Nvpart += 1
        try:
            self.fNSs = copy.deepcopy(fNS_vent[0])
            self.fEWs = copy.deepcopy(fEW_vent[0])
            self.fVEs = copy.deepcopy(fVE_vent[0])
        except:
            self.fNSs = fNS_vent[0]
            self.fEWs = fEW_vent[0]
            self.fVEs = fVE_vent[0]
        self.Nespec= Nespec
        #print()
        #print(self.fNSs)
        #print()
        #self.espectros_suav()
        self.fr, self.HV = self.HVSR(sub, fNS_vent, fEW_vent, fVE_vent, Nespec, fmax)
        return self.fr, self.HV

    def espectros_plot(self, sub):#, x, y, z, vi, vf, winclean):
        NQ = int(self.Nespec / 2 + 1)
        fmax = 1. / (2 * self.new_dt)
        meanarrN = np.mean(self.fNSs, axis=0)
        meanarrE = np.mean(self.fEWs, axis=0)
        meanarrV = np.mean(self.fVEs, axis=0)
        freq = np.linspace(0, fmax, NQ, endpoint=True)
        jj = [i for i in range(len(freq)) if self.fini<=freq[i]<self.ffin]
        # PROCESADOS
        if self.konno != 90:
            try:
                print("Konno Fast espectros amplitud")
                self.meankN = konno.fast_konno_ohmachi(meanarrN[jj], freq[jj], smooth_coeff=self.konno)
                self.meankE = konno.fast_konno_ohmachi(meanarrE[jj], freq[jj], smooth_coeff=self.konno)
                self.meankV = konno.fast_konno_ohmachi(meanarrV[jj], freq[jj], smooth_coeff=self.konno)
                # print("Konno Faster espectros")
                # self.meankN = konno.faster_konno_ohmachi(meanarrN[jj], freq[jj], smooth_coeff=self.konno)
                # self.meankE = konno.faster_konno_ohmachi(meanarrE[jj], freq[jj], smooth_coeff=self.konno)
                # self.meankV = konno.faster_konno_ohmachi(meanarrV[jj], freq[jj], smooth_coeff=self.konno)
            except:
                print("No entra a konno")
        else:
            self.meankN = meanarrN[jj]
            self.meankE = meanarrE[jj]
            self.meankV = meanarrV[jj]
        #daf = pd.DataFrame({'f':freq[jj], 'NS':self.meankN, 'EW':self.meankE, 'Z':self.meankV})
        #daf.to_csv("esp_"+self.nombre+".txt", index=None,sep='\t', columns=["f", "NS","EW","Z"])
        #gs1 = gridspec.GridSpec(1, 1)
        ax1 = sub.add_subplot(111)
        #print(len(freq[jj]))
        #print(len(self.meankN))
        #print(len(meanarrN))
        #print(freq[jj][0], freq[jj][-1])
        ax1.plot(freq[jj], self.meankN, 'b' ,label="NS")
        ax1.plot(freq[jj], self.meankE, 'r', label="EW")
        ax1.plot(freq[jj], self.meankV, 'm', label="VE")
        minimo = np.min([np.min(self.meankN), np.min(self.meankE), np.min(self.meankV)])
        maximo = np.max([np.max(self.meankN), np.max(self.meankE), np.max(self.meankV)])
        for ii in range(10):
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "k", linestyle=":", linewidth=0.5)
        mingridx = np.linspace(0.1, 100.0, 200)
        for ii in mingridx:
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "lightgrey", linestyle=":", linewidth=0.5)
        ax1.legend(loc="upper right")
        ax1.set_xscale("symlog")
        ax1.set_yscale("linear")
        ax1.set_ylabel('Amplitud')
        ax1.set_xlabel('Frecuencia (Hz)')
        spacingyma = (maximo-minimo)/5
        majorLocator = MultipleLocator(spacingyma)
        spacingymi = (maximo-minimo)/5/10
        minorLocatory = MultipleLocator(spacingymi)
        ax1.yaxis.set_minor_locator(minorLocatory)
        ax1.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
        ax1.yaxis.set_major_locator(majorLocator)
        ax1.grid(which='major', color='k', linestyle=':')  # , linewidth=3)
        ax1.tick_params(axis='both', which='minor')  # , labelsize=45)
        ax1.tick_params(axis='x', which='major')  # , labelsize=45)
        #ax1.tick_params(axis='y', which='major')  # , labelsize=45)
        ax1.set_ylim(minimo - 0.1, maximo + 0.1)
        ax1.set_xlim(left=self.fini, right=self.ffin)
        ax1.set_title("Espectros de Amplitud de Estación " + self.nombre)
        #ax1.suptitle('Espectros de Amplitud de Estación ' + self.nombre)
        #gs1.tight_layout(sub)
        return

    def HVSR(self, sub, fNS_vent, fEW_vent, fVE_vent, Nespec, fmax):
        fr = 0
        filt_HV = 0
        NQ = int(Nespec / 2 + 1)
        Nv = len(fNS_vent)
        freq = np.linspace(0, fmax, NQ, endpoint=True)
        jj = [i for i in range(len(freq)) if freq[i] >= 0.1]
        HNS = np.zeros(NQ)
        HEW = np.zeros(NQ)
        HVE = np.zeros(NQ)
        for k in range(NQ):  # para cada frecuencia
            for i in range(Nv):  # todas las ventanas
                HNS[k] += fNS_vent[i][0][k] ** 2
                HEW[k] += fEW_vent[i][0][k] ** 2
                HVE[k] += fVE_vent[i][0][k] ** 2
        HVwin = [];
        HVprom = []
        OME = np.zeros(NQ)
        for i in range(Nv):
            HVwin.append(np.sqrt((fNS_vent[i][0][:] ** 2 + fEW_vent[i][0][:] ** 2)) / (2.0 * fVE_vent[i][0][:]))
            HVprom.append(np.sqrt((fNS_vent[i][0][:] ** 2 + fEW_vent[i][0][:] ** 2)) / (2.0 * fVE_vent[i][0][:]))
            OME += np.log10(HVwin[i]) / (Nv * 1.0)
        HVNak = 10.0 ** (OME)
        meanarr = np.mean(HVprom, axis=0)
        arrnew = [(np.log10(HVprom[i]) - np.log10(meanarr)) ** 2 for i in range(len(HVwin))]
        if len(HVwin)>1:
            stdarr = np.sqrt(np.sum(arrnew, axis=0) / (len(HVwin) - 1))
        else:
            stdarr = np.sqrt(np.sum(arrnew, axis=0) / (len(HVwin)))
        HVSR = np.sqrt((HNS + HEW) / (HVE))
        self.HVSS_1 = np.sqrt((HNS + HEW) / (2*HVE))
        self.EW_fou = HEW[jj]
        self.NS_fou = HNS[jj]
        self.VE_fou = HVE[jj]
        self.HVSS_1 = self.HVSS_1[jj]
        NHV = np.sqrt(HNS / HVE)
        EHV = np.sqrt(HEW / HVE)
        EHV = EHV[jj]
        NHV = NHV[jj]
        fr = freq[jj]
        self.f_fou = fr
        HV1 = HVSR[jj]
        HV2 = HVNak[jj]
        std = stdarr[jj]
        ind = [i for i in range(len(fr)) if (fr[i] >= self.fini) & (fr[i] <= self.ffin)]
        fr = fr[ind[0]:ind[-1]]
        HVCD = HV1[ind[0]:ind[-1]]
        HVNK = HV2[ind[0]:ind[-1]]
        stdn = std[ind[0]:ind[-1]]
        self.HVSS_1 = self.HVSS_1[ind[0]:ind[-1]]
        self.EHV = EHV[ind[0]:ind[-1]]
        self.NHV = NHV[ind[0]:ind[-1]]
        filt_HV = self.HVSR_konno(sub, fr, HVCD, HVNK, stdn)
        return fr, filt_HV

    def HVDIR_plot(self, sub):
        if self.konno !=90:
            print("Konno-Ohmachi Fast: Suavizando los H/V direccionales")
            NHV_k = konno.fast_konno_ohmachi(self.NHV, self.f_suav, smooth_coeff=self.konno)
            EHV_k = konno.fast_konno_ohmachi(self.EHV, self.f_suav, smooth_coeff=self.konno)
        else:
            NHV_k = self.NHV
            EHV_k = self.EHV
        #matplotlib.rcParams['axes.linewidth'] = 1.5  # set the value globally
        spacingyma = 1.
        majorLocator = MultipleLocator(spacingyma)
        spacingymi = 0.5
        minorLocatory = MultipleLocator(spacingymi)
        #gs1 = gridspec.GridSpec(1,1)
        ax1 = sub.add_subplot(111)
        ax1.plot(self.f_suav, self.HV_suav, 'k', label=r'$\sqrt{\frac{NS+EW}{VE}}$')
        ax1.plot(self.f_suav, NHV_k, 'dodgerblue', label=r"$\sqrt{\frac{NS}{VE}}$")
        ax1.plot(self.f_suav, EHV_k, 'mediumvioletred', label=r"$\sqrt{ \frac{EW}{VE}}$")
        #minimo = np.min(self.HV_suav-self.stdminus)
        #maximo = np.max(self.HV_suav+self.stdplus)
        minimo = np.min([np.min(NHV_k - self.std), np.min(EHV_k - self.std), np.min(self.HV_suav - self.std)])
        maximo = np.max([np.max(NHV_k + self.std), np.max(EHV_k + self.std), np.max(self.HV_suav + self.std)])
        for ii in range(10):
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "k", linestyle=":", linewidth=0.5)
        mingridx = np.linspace(0.1, 100.0, 200)
        for ii in mingridx:
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "lightgrey", linestyle=":", linewidth=0.5)
        ax1.legend(loc="upper right") #prop={'size': 55},
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
        ax1.set_ylim(minimo - 0.1, maximo + 2.0)
        ax1.set_xlim(left=self.fini, right=self.ffin)
        ax1.set_title("H/V direccionales de estación "+ self.nombre)
        #gs1.tight_layout(sub)


    def HVSR_konno(self, sub, f, HVCD, HVNK, std):
        stdminus = []
        stdplus= []
        if self.konno != 90:
            #stdminus = self.smooth_ma(HVNK - std, int(len(HVCD) / 10))
            #stdplus = self.smooth_ma(HVCD + std, int(len(HVCD) / 10))
            try:
                print("Konno-Ohmachi Fast: Suzvizando H/V average y std")
                filt_HV = konno.fast_konno_ohmachi(HVCD, f, smooth_coeff=self.konno)
                stdkonno = konno.fast_konno_ohmachi(std, f, smooth_coeff=self.konno)
            except:
                print("Konno-Ohmachi Faster")
                filt_HV = konno.faster_konno_ohmachi(HVCD, f, smooth_coeff=self.konno)
                stdkonno = konno.faster_konno_ohmachi(std, f, smooth_coeff=self.konno)
            for i in range(len(filt_HV)):
                stdminus.append(filt_HV[i]-stdkonno[i])
                stdplus.append(filt_HV[i]+stdkonno[i])
        else:
            filt_HV = HVCD
            filt_HVNK = HVNK
            stdminus = HVNK - std
            stdplus = HVCD + std

        if np.mean(filt_HV) < 1.0:
            print("Media del HV: ", np.mean(filt_HV))
            stdminus = filt_HV
            filt_HV = konno.fast_konno_ohmachi(filt_HV + 2*std, f, smooth_coeff=self.konno)
            stdplus = konno.fast_konno_ohmachi(filt_HV + std, f, smooth_coeff=40)

        self.stdminus = stdminus
        self.stdplus = stdplus
        self.HV_suav = filt_HV
        self.f_suav = f
        self.std =std

        self.HV_plot(sub)

        return filt_HV

    def HV_plot(self, sub):
        matplotlib.rcParams['axes.linewidth'] = 1.5  # set the value globally
        spacingyma = 1.
        majorLocator = MultipleLocator(spacingyma)
        spacingymi = 0.5
        minorLocatory = MultipleLocator(spacingymi)
        #gs1 =gridspec.GridSpec(1,1)
        ax1 = sub.add_subplot(111)
        #arch = pd.read_csv(r"C:\Users\52551\Documents\TWHV_GEOPSY\CANANEA\1.hv", sep='\s+',header=None, skiprows=7)
        #print(arch.head())
        ax1.plot(self.f_suav, self.HV_suav, 'k')
        #ax1.plot(self.f_suav, self.SS1, label=r'SS \sqrt{\frac{H}{2VE}}')
        #ax1.plot(arch.iloc[:,0], arch.iloc[:,1], label='GEOPSY')
        ax1.plot(self.f_suav, self.stdplus, 'firebrick', linestyle=":")
        ax1.plot(self.f_suav, self.stdminus, 'firebrick', linestyle=":")
        minimo = np.min(self.HV_suav - self.std)
        maximo = np.max(self.HV_suav + self.std)
        for ii in range(10):
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "k", linestyle=":", linewidth=0.5)
        #mingridx = np.linspace(0.1, 20.0, 100)
        mingridx = np.linspace(0.1, 100.0, 200)
        for ii in mingridx:
            ax1.plot([ii] * 5, np.linspace(minimo - 10, maximo + 10, 5), "lightgrey", linestyle=":", linewidth=0.5)
        #ax1.legend(loc="upper right")
        #dfnew = pd.DataFrame({'f':self.f_suav, 'TW':self.HV_suav, 'NAK':self.NAK, 'SS1':self.SS1, 'SS2':self.SS2})
        #dfnew.to_csv("comparacion_"+self.nombre+".txt", index=None,sep='\t', columns=["f","TW","NAK","SS1","SS2"])
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
        ax1.set_ylim(np.min(self.stdminus) - 0.1, np.max(self.stdplus) +2.0)
        ax1.set_xlim(left=self.fini, right=self.ffin)
        ax1.set_title('H/V de estación ' + self.nombre)
        #gs1.tight_layout(sub)

    def normalizacion(self, NS, EW, Z, Nespec):
        """
        NSw, EWw, Zw, Nespec, band, onebit, new_dt, factap
        :param NSw:
        :param EWw:
        :param Zw:
        :param Nespec:
        :return:
        """
        NSw = copy.deepcopy(NS)
        EWw = copy.deepcopy(EW)
        Zw = copy.deepcopy(Z)
        N = len(Zw)
        NQ = Nespec
        ff = np.linspace(0, 1 / (2. * self.new_dt), NQ)
        Nblanqfrec = [i for i in range(len(ff)) if ff[i] >= 0.1]
        Nblanqfrec = Nblanqfrec[0]
        Nblanqtiempo = int(20 / self.new_dt)
        facts = [0, 0, 0]
        if (self.normal == "ENER_UNIT") or (self.normal == "SUM_ENER") or (self.normal == "SPEC_WHIT"):
            if self.onebit == True:
                NSw = np.sign(NSw)
                EWw = np.sign(EWw)
                Zw = np.sign(Zw)
            fL = np.fft.rfft(NSw, Nespec)
            fV = np.fft.rfft(Zw, Nespec)
            fT = np.fft.rfft(EWw, Nespec)
            # Hasta la frecuencia de Nyquist
            fL = fL[0:int(NQ)]
            fV = fV[0:int(NQ)]
            fT = fT[0:int(NQ)]
            if self.normal == "ENER_UNIT":
                # ENER UNITARIAS
                fLnorm = fL
                fVnorm = fV
                fTnorm = fT
            elif self.normal == "SUM_ENER":
                # Division entre las suma de las energias potenciales de las 3 direcciones
                # SUMA DE ENERGIAS POTENCIALES
                CEE = np.sqrt((np.abs(fL)) ** 2 + (np.abs(fV)) ** 2 + (np.abs(fT)) ** 2)
                CEE = self.smooth_ma(np.abs(CEE), Nblanqfrec)
                fLnorm = fL / CEE
                fVnorm = fV / CEE
                fTnorm = fT / CEE
            elif self.normal == "SPEC_WHIT":
                # Blanqueamiento espectral
                fLnorm = fL / self.smooth_ma(np.abs(fL), Nblanqfrec)
                fVnorm = fV / self.smooth_ma(np.abs(fV), Nblanqfrec)
                fTnorm = fT / self.smooth_ma(np.abs(fT), Nblanqfrec)
        elif self.normal == "ENV_TIME":
            if self.onebit == True:
                NSw = np.sign(NSw)
                EWw = np.sign(EWw)
                Zw = np.sign(Zw)
            # Señal en tiempo entre su envolvente suavizada
            Lnorm = NSw / np.abs(signal.hilbert(NSw))  # ,Nblanqtiempo)
            Vnorm = Zw / self.smooth_ma(np.abs(signal.hilbert(Zw)), Nblanqtiempo)
            Tnorm = EWw / self.smooth_ma(np.abs(signal.hilbert(EWw)), Nblanqtiempo)
        elif self.normal == "ENER_TIME":
            if self.onebit == True:
                NSw = np.sign(NSw)
                EWw = np.sign(EWw)
                Zw = np.sign(Zw)
            # Señal en tiempo entre la integral del canal al cuadrado respecto al tiempo
            Lnorm = NSw / np.trapz(NSw ** 2, dx=self.new_dt)
            Tnorm = EWw / np.trapz(EWw ** 2, dx=self.new_dt)
            Vnorm = Zw / np.trapz(Zw ** 2, dx=self.new_dt)
        # TRANSFORMADA INVERSA
        if self.normal == "ENER_UNIT":
            Lnorm = NSw
            Vnorm = EWw
            Tnorm = NSw
        elif (self.normal == "SUM_ENER") or (self.normal == "SPEC_WHIT"):
            a = np.array(fLnorm[1:-1])
            b = np.flipud(np.conj(np.array(fLnorm[1:-1])))
            Lnorm = np.fft.ifft(np.concatenate((0, a, 0, b), axis=None))
            a = np.array(fVnorm[1:-1])
            b = np.flipud(np.conj(np.array(fVnorm[1:-1])))
            Vnorm = np.fft.ifft(np.concatenate((0, a, 0, b), axis=None))
            a = np.array(fTnorm[1:-1])
            b = np.flipud(np.conj(np.array(fTnorm[1:-1])))
            Tnorm = np.fft.ifft(np.concatenate((0, a, 0, b), axis=None))
            if self.tapwin == 'tukey':
                taper = signal.tukey(len(Vnorm), alpha=self.taper)
            elif self.tapwin == 'hann':
                taper = signal.hann(len(Vnorm))
            elif self.tapwin == 'blackman':
                taper = signal.blackman(len(Vnorm))
            elif self.tapwin == 'triangular':
                taper = signal.triang(len(Vnorm))
            elif self.tapwin == 'cosine':
                taper = signal.cosine(len(Vnorm))
            elif self.tapwin == 'hamming':
                taper = signal.hamming(len(Vnorm))
            elif self.tapwin == 'flattop':
                taper = signal.flattop(len(Vnorm))
            elif self.tapwin == 'boxcar':
                taper = signal.boxcar(len(Vnorm))
            elif self.tapwin == 'blackmanharris':
                taper = signal.blackmanharris(len(Vnorm))
            Lnorm *= taper
            Tnorm *= taper
            Vnorm *= taper
        elif (self.normal == "ENV_TIME") or (self.normal == "ENER_TIME"):
            fLnorm = np.fft.rfft(Lnorm, Nespec)
            fTnorm = np.fft.rfft(Tnorm, Nespec)
            fVnorm = np.fft.rfft(Vnorm, Nespec)
            fLnorm = fLnorm[0:NQ]
            fTnorm = fTnorm[0:NQ]
            fVnorm = fVnorm[0:NQ]
        return fLnorm, fTnorm, fVnorm, Lnorm, Tnorm, Vnorm, Nblanqfrec

    def butterworth_filtro(self):
        '''
        Filtrado con Butterworth centrado:
        wini-. frecuencia de corte inicial
        wfin-. frecuencia de corte final
        deltaf
        orden-. orden de butterworth
        self.wini, self.wfin, self.delf[self.currentIndex], self.orden_butter
        '''
        nyq = 0.5 * self.delf
        if self.wini==None and self.wfin!=None:
            #pasa bajas
            #print("pasa bajas")
            high = self.wfin / nyq
            b, a = signal.butter(self.orden_butter, high, btype='low', analog=False, output='ba')
            status = True
        elif self.wfin==None and self.wini!=None:
            # pasa altas
            #print("pasa altas")
            low = self.wini / nyq
            b, a = signal.butter(self.orden_butter, low, btype='highpass', analog=False, output='ba')
            status = True
        elif self.wfin!=None and self.wini!=None:
            # pasa bandas
            #print("pasa bandas")
            low = self.wini / nyq
            high = self.wfin / nyq
            b, a = signal.butter(self.orden_butter, [low, high], btype='band', analog=False, output='ba')
            status=True
        elif self.wfin==None and self.wini==None:
            #print("Ninguno")
            a=[]
            b=[]
            status=False
        return b, a, status

    def picos(self, sigin):
        # self.new_dt, Smax, tlta, porc1, porc2
        '''
        Quita las ventanas que contengan fuentes transitorias
        porc1 era .75
        porc2 era .85
        tlta numero de muestras por ventanilla
        Smax limite de tolerancia entre los promedios y el minimo
        Regresa el vector de ventantas aceptadas
        '''
        try:
            sig = copy.deepcopy(sigin)
        except:
            print("Warning: No crea copia legítima de señal de entrada de picos")
            sig = sigin
        SIGabs = np.absolute(sig)
        M = len(self.vi)
        N = len(sig)
        winclean = np.ones(M)
        # Maximos y medias por ventana
        maxs = np.zeros(M)
        STA = np.zeros(M)
        for i in range(M):
            SIGp = SIGabs[self.vi[i]:self.vf[i]]
            maxs[i] = SIGp.max()
            STA[i] = np.mean(SIGp)
            count = 0
            '''if M<7194:
                for j in range(1, len(SIGp)):
                    if np.abs(SIGp[j] - SIGp[j - 1]) < 1.0e-4:
                        count += 1
                        if count > 100:
                           winclean[i] = 0
                           continue
            else:
                print("Warning: Señal mayor a una hora de registro")
                pass'''
        #print("Sale del ciclo de limpieza de ceros")
        #print(winclean)
        maxtot = maxs.max()
        # Elimina picos superiores al 75% del pico maximo de la señal
        #print("Entra al ciclo de limpieza de picos1")
        for i in range(M):
            if maxs[i] > self.porc1 * maxtot:
                winclean[i] = 0
            if STA[i] == 0.0:
                winclean[i] = 0
            # if mins[i] < 1e-3:
            #    winclean[i] = 0
        mues = [i for i in range(M) if winclean[i] == 1]
        #print("Sale del ciclo de limpieza de picos1")
        #print(winclean)
        try:
            maxtot = max(maxs[mues])
        except:
            print("Error: maxtot = max(maxs[mues])")
            return
        # Elimina picos superiores al 70% del pico maximo de la señal
        for i in range(M):
            if winclean[i] == 1:
                if maxs[i] > self.porc2 * maxtot:
                    winclean[i] = 0
        # Busca valores de maximos por ventanas de 10s
        #print("TERMINA TERCER CICLO")
        try:
            # tlta = 200; #3600/20; #segundos
            #Nlta = int(self.tlta / self.new_dt)
            SIGabs[SIGabs == 0] = np.nan  # revisar
            #LTamin = self.smooth_ma(SIGabs, Nlta)
            #LTamin = LTamin[Nlta + 1:-1 - Nlta]
            LTamin = np.mean(STA)
            #LTamin = 90.0
        except:
            "Advertencia: tlta=100"
            #self.tlta = 100  # 3600./20.0; #segundos
            #Nlta = int(self.tlta / self.new_dt)
            SIGabs[SIGabs == 0] = np.nan  # revisar
            #LTamin = self.smooth_ma(SIGabs, Nlta)
            #LTamin = LTamin[Nlta + 1:-1 - Nlta]
            #LTamin = min(STA)
            LTamin = 90.0
        #print("TERMINA TRY")
        # Evaluacion STA/LTA > Smax
        for i in range(M):
            if winclean[i] == 1:
                #print(STA[i], STA[i] / LTamin)
                if STA[i] / LTamin > self.smax:
                    winclean[i] = 0
        #print("TERMINA CUARTO CICLO")
        return winclean

    def smooth_ma(self, sig, period):
        """
        Moving average centrado con la señal en los extremos
        :param sig:
        :param period:
        :return:
        """
        buf = np.zeros(len(sig))
        buf[:] = copy.deepcopy(sig[:])
        for i in range(int(period / 2), len(sig) - int(period / 2)):
            buf[i] = sig[i - int(period / 2):i + int(period / 2)].mean()
        return buf

    def moving_average(self, sig, period):
        """
        Moving average centrado con 0s en los extremos
        :param sig:
        :param period:
        :return:
        """
        buf = np.zeros(len(sig))
        for i in range(int(period / 2), len(sig) - int(period / 2)):
            buf[i] = sig[i - int(period / 2):i + int(period / 2)].mean()
        return buf

    def baseline_taper(self, siginor):
        """
        Hace correccion de linea base y taper por ventana
        :param sigin: ventana de la señal
        :return: ventana de la señal con correccion de lb y taper
        """
        sigin = copy.deepcopy(siginor)
        sigout = sigin.astype('float32')
        if self.baseline == True:
            sigout = signal.detrend(sigout, type='linear')
        #print("sigin: ", sigin)
        #print("sigout: ", sigout)
        #print()
        #print()
        #sigout = sigin
        if self.tapwin == 'tukey':
            taper = signal.tukey(len(sigout), alpha=self.taper)
        elif self.tapwin == 'hann':
            taper = signal.hann(len(sigout))
        elif self.tapwin == 'blackman':
            taper = signal.blackman(len(sigout))
        elif self.tapwin == 'triangular':
            taper = signal.triang(len(sigout))
        elif self.tapwin == 'cosine':
            taper = signal.cosine(len(sigout))
        elif self.tapwin == 'hamming':
            taper = signal.hamming(len(sigout))
        elif self.tapwin == 'flattop':
            taper = signal.flattop(len(sigout))
        elif self.tapwin == 'boxcar':
            taper = signal.boxcar(len(sigout))
        elif self.tapwin == 'blackmanharris':
            taper = signal.blackmanharris(len(sigout))
        #taper = signal.tukey(len(sigout), self.taper)
        sigout *= taper
        return sigout

    def butterf(self):
        """
        Remuestreo: Diezmado o Interpolacion
        Filtro de Buterworth con las frecuencias de corte correspondientes
        Señales pares
        Regresa:
        el registro modificado (aguas! que no esta en los returns)
        t_ini, t_fin, deltaf, deltat
        """
        Nor = copy.deepcopy(self.NS)
        Eor = copy.deepcopy(self.EW)
        Zor = copy.deepcopy(self.VE)
        fact = self.delf * self.new_dt
        #print(fact)
        NSnew = Nor
        ESnew = Eor
        VSnew = Zor
        try:
            if fact < 1:
                print("Se altera por muestreo la señal: interpolacion fact <1")
                time_arr = np.linspace(time.mktime(self.tini.timetuple()),
                                       time.mktime(self.tfin.timetuple()),
                                       num=self.nmues, endpoint=True)
                fx = interpolate.interp1d(time_arr, Nor, kind='linear')
                fy = interpolate.interp1d(time_arr, Eor, kind='linear')
                fz = interpolate.interp1d(time_arr, Zor, kind='linear')
                nmues = int((time.mktime(self.tfin.timetuple()) -
                             time.mktime(self.tini.timetuple()) + 1) / self.new_dt)
                newtime = np.linspace(time.mktime(self.tini.timetuple()),
                             time.mktime(self.tfin.timetuple()), num=nmues, endpoint=True)
                NSnew = fx(newtime)
                ESnew = fy(newtime)
                VSnew = fz(newtime)
            elif fact > 1:
                print("Se altera por muestreo la señal: diezmado fact >1")
                NSnew = signal.decimate(Nor, int(fact))
                ESnew = signal.decimate(Eor, int(fact))
                VSnew = signal.decimate(Zor, int(fact))
            else:
                print("No se altera por muestreo la señal")
                pass
        except:
            print("Error en re-muestreo de señal")
            pass

        # Filtrado con Butterworth
        b, a, status = self.butterworth_filtro()
        if status==False:
            NSfilt = NSnew
            ESfilt = ESnew
            VSfilt = VSnew
        else:
            #print("Filtro phase cero")
            NSfilt = signal.filtfilt(b, a, NSnew)  # normal filter: lfilt() zero phase: filtfilt
            ESfilt = signal.filtfilt(b, a, ESnew)
            VSfilt = signal.filtfilt(b, a, VSnew)

        # Señal par
        if len(VSfilt) % 2 != 0:
            print("Corta la señal par")
            #print(len(NSfilt))
            NSfilt = NSfilt[:-1]
            ESfilt = ESfilt[:-1]
            VSfilt = VSfilt[:-1]
            #print(len(NSfilt))

        return NSfilt, ESfilt, VSfilt

