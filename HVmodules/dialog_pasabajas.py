# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_pasabajas.ui',
# licensing of 'dialog_pasabajas.ui' applies.
#
# Created: Fri Feb  7 13:43:15 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *

class Ui_pasabajas(object):
    def setupUi(self, pasabajas):
        pasabajas.setObjectName("pasabajas")
        pasabajas.resize(220, 123)
        self.layoutWidget = QtWidgets.QWidget(pasabajas)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_basabajas = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_basabajas.setObjectName("groupBox_basabajas")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_basabajas)
        self.formLayout.setObjectName("formLayout")
        self.label_wfin = QtWidgets.QLabel(self.groupBox_basabajas)
        self.label_wfin.setObjectName("label_wfin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_wfin)
        self.doubleSpinBox_wfin = QtWidgets.QDoubleSpinBox(self.groupBox_basabajas)
        self.doubleSpinBox_wfin.setDecimals(5)
        self.doubleSpinBox_wfin.setProperty("value", 0.0)
        self.doubleSpinBox_wfin.setObjectName("doubleSpinBox_wfin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_wfin)
        self.verticalLayout.addWidget(self.groupBox_basabajas)
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

        self.retranslateUi(pasabajas)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), pasabajas.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), pasabajas.reject)
        QtCore.QMetaObject.connectSlotsByName(pasabajas)

    def retranslateUi(self, pasabajas):
        pasabajas.setWindowTitle(QtWidgets.QApplication.translate("pasabajas", "Pasa bajas", None, -1))
        self.groupBox_basabajas.setTitle(QtWidgets.QApplication.translate("pasabajas", "Frecuencia de corte pasa bajas", None, -1))
        self.label_wfin.setText(QtWidgets.QApplication.translate("pasabajas", "Frecuencia de corte", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogpinver = QtWidgets.QDialog()
    ui = Ui_pasabajas()
    ui.setupUi(dialogpinver)
    dialogpinver.show()
    sys.exit(app.exec_())