# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_filtertype.ui',
# licensing of 'dialog_filtertype.ui' applies.
#
# Created: Fri Feb  7 13:42:18 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *
import HVmodules.dialog_pasaaltas as dialog_pasaaltas
import HVmodules.dialog_pasabajas as dialog_pasabajas
import HVmodules.dialog_pasabandas as dialog_pasabandas

class Ui_Filtrobutter(object):
    def setupUi(self, Filtrobutter):
        Filtrobutter.setObjectName("Filtrobutter")
        Filtrobutter.resize(218, 122)
        self.layoutWidget = QtWidgets.QWidget(Filtrobutter)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_tipofiltro = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_tipofiltro.setObjectName("groupBox_tipofiltro")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_tipofiltro)
        self.formLayout.setObjectName("formLayout")
        self.label_tipofiltro = QtWidgets.QLabel(self.groupBox_tipofiltro)
        self.label_tipofiltro.setObjectName("label_tipofiltro")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tipofiltro)
        self.comboBox_tipofiltro = QtWidgets.QComboBox(self.groupBox_tipofiltro)
        self.comboBox_tipofiltro.setObjectName("comboBox_tipofiltro")
        self.comboBox_tipofiltro.addItem("")
        self.comboBox_tipofiltro.addItem("")
        self.comboBox_tipofiltro.addItem("")
        self.comboBox_tipofiltro.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_tipofiltro)
        self.verticalLayout.addWidget(self.groupBox_tipofiltro)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Filtrobutter)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Filtrobutter.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Filtrobutter.reject)
        QtCore.QMetaObject.connectSlotsByName(Filtrobutter)

        # PASA BANDAS
        self.diaPasaBandas = QtWidgets.QDialog()
        self.pasaBandas = dialog_pasabandas.Ui_pasabandas()
        self.pasaBandas.setupUi(self.diaPasaBandas)
        # PASA BAJAS
        self.diaPasaBajas = QtWidgets.QDialog()
        self.pasaBajas = dialog_pasabajas.Ui_pasabajas()
        self.pasaBajas.setupUi(self.diaPasaBajas)
        #PASA ALTAS
        self.diaPasaAltas = QtWidgets.QDialog()
        self.pasaAltas = dialog_pasaaltas.Ui_pasaaltas()
        self.pasaAltas.setupUi(self.diaPasaAltas)

        self.conexiones()

    def conexiones(self):
        self.comboBox_tipofiltro.currentIndexChanged.connect(self.selectfiltro)

    def selectfiltro(self,i):
        if i == 1:
            self.diaPasaBandas.open()
        elif i==2:
            self.diaPasaBajas.open()
        elif i==3:
            self.diaPasaAltas.open()
        else:
            pass

    def retranslateUi(self, Filtrobutter):
        Filtrobutter.setWindowTitle(QtWidgets.QApplication.translate("Filtrobutter", "Selección de Filtro", None, -1))
        self.groupBox_tipofiltro.setTitle(QtWidgets.QApplication.translate("Filtrobutter", "Filtro Butterworth", None, -1))
        self.label_tipofiltro.setText(QtWidgets.QApplication.translate("Filtrobutter", "Tipo de Filtro:", None, -1))
        self.comboBox_tipofiltro.setItemText(0, QtWidgets.QApplication.translate("Filtrobutter", "Selecciona Filtro", None, -1))
        self.comboBox_tipofiltro.setItemText(1, QtWidgets.QApplication.translate("Filtrobutter", "Pasa bandas", None, -1))
        self.comboBox_tipofiltro.setItemText(2, QtWidgets.QApplication.translate("Filtrobutter", "Pasa bajas", None, -1))
        self.comboBox_tipofiltro.setItemText(3, QtWidgets.QApplication.translate("Filtrobutter", "Pasa altas", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogpinver = QtWidgets.QDialog()
    ui = Ui_Filtrobutter()
    ui.setupUi(dialogpinver)
    dialogpinver.show()
    sys.exit(app.exec_())