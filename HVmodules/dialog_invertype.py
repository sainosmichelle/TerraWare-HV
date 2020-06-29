# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_invertype.ui',
# licensing of 'dialog_invertype.ui' applies.
#
# Created: Tue Dec 10 16:07:01 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *
import HVmodules.dialog_pinver as dialog_pinver

class Ui_dialoginvtype(object):
    def setupUi(self, inversion):
        inversion.setObjectName("inversion")
        inversion.resize(264, 190)
        font = QtGui.QFont("MS Shell Dlg 2", 10.5)
        self.widget = QtWidgets.QWidget(inversion)
        self.widget.setGeometry(QtCore.QRect(10, 20, 241, 151))
        self.widget.setObjectName("widget")
        self.widget.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(inversion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), inversion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), inversion.reject)
        QtCore.QMetaObject.connectSlotsByName(inversion)

        self.dialog2 = QtWidgets.QDialog()
        self.inverparams = dialog_pinver.Ui_dialogpinver()
        self.inverparams.setupUi(self.dialog2)

        self.conexiones()

    def conexiones(self):
        self.comboBox.currentIndexChanged.connect(self.selectinversion)

    def selectinversion(self,i):
        if i == 1:
            self.dialog2.open()
        else:
            pass

    def retranslateUi(self, inversion):
        inversion.setWindowTitle(QtWidgets.QApplication.translate("inversion", "Inversión", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("inversion", "Elige tipo de inversión:", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("inversion", "Método", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("inversion", "Particle Swarm Optimization", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("inversion", "Simulated Annealing", None, -1))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogpinver = QtWidgets.QDialog()
    ui = Ui_dialoginvtype()
    ui.setupUi(dialogpinver)
    dialogpinver.show()
    sys.exit(app.exec_())