# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../python/base/widgets/detail_widget/resources/detailed_widget.ui'
#
# Created: Sun Apr 24 00:22:18 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Detailed_mutations(object):
    def setupUi(self, Detailed_mutations):
        Detailed_mutations.setObjectName("Detailed_mutations")
        Detailed_mutations.resize(500, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Detailed_mutations.sizePolicy().hasHeightForWidth())
        Detailed_mutations.setSizePolicy(sizePolicy)
        Detailed_mutations.setMinimumSize(QtCore.QSize(500, 350))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Detailed_mutations)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(Detailed_mutations)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_consensus_residue = QtGui.QLabel(Detailed_mutations)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.label_consensus_residue.setFont(font)
        self.label_consensus_residue.setAlignment(QtCore.Qt.AlignCenter)
        self.label_consensus_residue.setObjectName("label_consensus_residue")
        self.verticalLayout.addWidget(self.label_consensus_residue)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(Detailed_mutations)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_position = QtGui.QLabel(Detailed_mutations)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.label_position.setFont(font)
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")
        self.verticalLayout.addWidget(self.label_position)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.treeView_mutation_types = QtGui.QTreeView(Detailed_mutations)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_mutation_types.sizePolicy().hasHeightForWidth())
        self.treeView_mutation_types.setSizePolicy(sizePolicy)
        self.treeView_mutation_types.setMinimumSize(QtCore.QSize(200, 100))
        self.treeView_mutation_types.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView_mutation_types.setAlternatingRowColors(True)
        self.treeView_mutation_types.setObjectName("treeView_mutation_types")
        self.verticalLayout.addWidget(self.treeView_mutation_types)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.treeView_detailed_mutations = QtGui.QTreeView(Detailed_mutations)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_detailed_mutations.sizePolicy().hasHeightForWidth())
        self.treeView_detailed_mutations.setSizePolicy(sizePolicy)
        self.treeView_detailed_mutations.setMinimumSize(QtCore.QSize(250, 300))
        self.treeView_detailed_mutations.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView_detailed_mutations.setAlternatingRowColors(True)
        self.treeView_detailed_mutations.setObjectName("treeView_detailed_mutations")
        self.horizontalLayout.addWidget(self.treeView_detailed_mutations)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Detailed_mutations)
        QtCore.QMetaObject.connectSlotsByName(Detailed_mutations)

    def retranslateUi(self, Detailed_mutations):
        Detailed_mutations.setWindowTitle(QtGui.QApplication.translate("Detailed_mutations", "Deatiled Mutations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Detailed_mutations", "Consensus Residue:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_consensus_residue.setText(QtGui.QApplication.translate("Detailed_mutations", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Detailed_mutations", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_position.setText(QtGui.QApplication.translate("Detailed_mutations", "A", None, QtGui.QApplication.UnicodeUTF8))

