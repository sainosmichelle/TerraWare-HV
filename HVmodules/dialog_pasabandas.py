# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_pasabandas.ui',
# licensing of 'dialog_pasabandas.ui' applies.
#
# Created: Fri Feb  7 13:43:26 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *

class Ui_pasabandas(object):
    def setupUi(self, pasabandas):
        pasabandas.setObjectName("pasabandas")
        pasabandas.resize(220, 155)
        self.layoutWidget = QtWidgets.QWidget(pasabandas)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_basabandas = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_basabandas.setObjectName("groupBox_basabandas")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_basabandas)
        self.formLayout.setObjectName("formLayout")
        self.label_wini = QtWidgets.QLabel(self.groupBox_basabandas)
        self.label_wini.setObjectName("label_wini")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_wini)
        self.label_wfin = QtWidgets.QLabel(self.groupBox_basabandas)
        self.label_wfin.setObjectName("label_wfin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_wfin)
        self.doubleSpinBox_wini = QtWidgets.QDoubleSpinBox(self.groupBox_basabandas)
        self.doubleSpinBox_wini.setDecimals(5)
        self.doubleSpinBox_wini.setMinimum(0.0)
        self.doubleSpinBox_wini.setMaximum(99.0)
        #self.doubleSpinBox_wini.setProperty("value", 1e-05)
        self.doubleSpinBox_wini.setObjectName("doubleSpinBox_wini")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_wini)
        self.doubleSpinBox_wfin = QtWidgets.QDoubleSpinBox(self.groupBox_basabandas)
        self.doubleSpinBox_wfin.setDecimals(5)
        self.doubleSpinBox_wfin.setMaximum(99.0)
        #self.doubleSpinBox_wfin.setProperty("value", 99.0)
        self.doubleSpinBox_wfin.setObjectName("doubleSpinBox_wfin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_wfin)
        self.verticalLayout.addWidget(self.groupBox_basabandas)
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

        self.retranslateUi(pasabandas)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), pasabandas.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), pasabandas.reject)
        QtCore.QMetaObject.connectSlotsByName(pasabandas)
        self.default()

    def default(self):
        self.doubleSpinBox_wini.setProperty("value", 0.0)
        self.doubleSpinBox_wfin.setProperty("value", 0.0)

    def retranslateUi(self, pasabandas):
        pasabandas.setWindowTitle(QtWidgets.QApplication.translate("pasabandas", "Pasa bandas", None, -1))
        self.groupBox_basabandas.setTitle(QtWidgets.QApplication.translate("pasabandas", "Frecuencias de corte", None, -1))
        self.label_wini.setText(QtWidgets.QApplication.translate("pasabandas", "Frecuencia inicial", None, -1))
        self.label_wfin.setText(QtWidgets.QApplication.translate("pasabandas", "Frecuencia final", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogpinver = QtWidgets.QDialog()
    ui = Ui_pasabandas()
    ui.setupUi(dialogpinver)
    dialogpinver.show()
    sys.exit(app.exec_())