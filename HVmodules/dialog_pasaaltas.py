# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_pasaaltas.ui',
# licensing of 'dialog_pasaaltas.ui' applies.
#
# Created: Fri Feb  7 13:42:55 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *

class Ui_pasaaltas(object):
    def setupUi(self, pasaaltas):
        pasaaltas.setObjectName("pasaaltas")
        pasaaltas.resize(220, 123)
        self.layoutWidget = QtWidgets.QWidget(pasaaltas)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_basaaltas = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_basaaltas.setObjectName("groupBox_basaaltas")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_basaaltas)
        self.formLayout.setObjectName("formLayout")
        self.label_wini = QtWidgets.QLabel(self.groupBox_basaaltas)
        self.label_wini.setObjectName("label_wini")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_wini)
        self.doubleSpinBox_wini = QtWidgets.QDoubleSpinBox(self.groupBox_basaaltas)
        self.doubleSpinBox_wini.setDecimals(5)
        self.doubleSpinBox_wini.setProperty("value", 0.0)
        self.doubleSpinBox_wini.setObjectName("doubleSpinBox_wini")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_wini)
        self.verticalLayout.addWidget(self.groupBox_basaaltas)
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

        self.retranslateUi(pasaaltas)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), pasaaltas.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), pasaaltas.reject)
        QtCore.QMetaObject.connectSlotsByName(pasaaltas)

    def retranslateUi(self, pasaaltas):
        pasaaltas.setWindowTitle(QtWidgets.QApplication.translate("pasaaltas", "Pasa altas", None, -1))
        self.groupBox_basaaltas.setTitle(QtWidgets.QApplication.translate("pasaaltas", "Frecuencia de corte pasa altas", None, -1))
        self.label_wini.setText(QtWidgets.QApplication.translate("pasaaltas", "Frecuencia de corte", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogpinver = QtWidgets.QDialog()
    ui = Ui_pasaaltas()
    ui.setupUi(dialogpinver)
    dialogpinver.show()
    sys.exit(app.exec_())
