# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_pvents.ui',
# licensing of 'dialog_pvents.ui' applies.
#
# Created: Fri Jan  3 12:57:33 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from HVmodules.NModule import *

class Ui_dialogVents(object):
    def setupUi(self, dialogpinver):
        dialogpinver.setObjectName("dialogpinver")
        dialogpinver.resize(306, 243)
        font = QtGui.QFont("MS Shell Dlg 2", 10.5)
        self.layoutWidget = QtWidgets.QWidget(dialogpinver)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 290, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_pinver = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_pinver.setObjectName("groupBox_pinver")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_pinver)
        self.formLayout.setObjectName("formLayout")
        self.label_iter = QtWidgets.QLabel(self.groupBox_pinver)
        self.label_iter.setObjectName("label_iter")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_iter)
        self.spinBox_iter = QtWidgets.QDoubleSpinBox(self.groupBox_pinver)
        self.spinBox_iter.setMinimum(1)
        self.spinBox_iter.setMaximum(10)
        self.spinBox_iter.setDecimals(2)
        self.spinBox_iter.setProperty("value", 1.0)  #smax
        self.spinBox_iter.setObjectName("spinBox_iter")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_iter)
        #self.label_parts = QtWidgets.QLabel(self.groupBox_pinver)
        #self.label_parts.setObjectName("label_parts")
        #self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_parts)
        #self.spinBox_parts = QtWidgets.QSpinBox(self.groupBox_pinver)
        #self.spinBox_parts.setMinimum(50)
        #self.spinBox_parts.setMaximum(500)
        #self.spinBox_parts.setProperty("value", 180)
        #self.spinBox_parts.setObjectName("spinBox_parts")
        #self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_parts)
        self.label_wini = QtWidgets.QLabel(self.groupBox_pinver)
        self.label_wini.setObjectName("label_wini")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_wini)
        self.doubleSpinBox_wini = QtWidgets.QDoubleSpinBox(self.groupBox_pinver)
        self.doubleSpinBox_wini.setDecimals(2)
        self.doubleSpinBox_wini.setMaximum(100.0)
        self.doubleSpinBox_wini.setSingleStep(1.0)
        self.doubleSpinBox_wini.setProperty("value", 0.90)
        self.doubleSpinBox_wini.setObjectName("doubleSpinBox_wini")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_wini)
        self.label_wa = QtWidgets.QLabel(self.groupBox_pinver)
        self.label_wa.setObjectName("label_wa")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_wa)
        self.doubleSpinBox_wa = QtWidgets.QDoubleSpinBox(self.groupBox_pinver)
        self.doubleSpinBox_wa.setDecimals(2)
        self.doubleSpinBox_wa.setMaximum(100.0)
        self.doubleSpinBox_wa.setSingleStep(1.0)
        self.doubleSpinBox_wa.setProperty("value", 0.90)
        self.doubleSpinBox_wa.setObjectName("doubleSpinBox_wa")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_wa)
        self.verticalLayout.addWidget(self.groupBox_pinver)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_info = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout.addWidget(self.pushButton_info)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialogpinver)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialogpinver.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialogpinver.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogpinver)


    def retranslateUi(self, dialogpinver):
        dialogpinver.setWindowTitle(QtWidgets.QApplication.translate("dialogpinver", "Parámetros de ventanas", None, -1))
        self.groupBox_pinver.setTitle(QtWidgets.QApplication.translate("dialogpinver", "Parámetros de eliminación de ventana", None, -1))
        self.label_iter.setText(QtWidgets.QApplication.translate("dialogpinver", "Máximo # de std: ", None, -1))
        #self.label_parts.setText(QtWidgets.QApplication.translate("dialogpinver", "Tlta:", None, -1))
        self.label_wini.setText(QtWidgets.QApplication.translate("dialogpinver", "% del primer pico:", None, -1))
        self.label_wa.setText(QtWidgets.QApplication.translate("dialogpinver", "% del segundo pico:", None, -1))
        self.pushButton_info.setText(QtWidgets.QApplication.translate("dialogpinver", "Info", None, -1))

