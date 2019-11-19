from UI.Interface_AGB import QtWidgets, Ui_MainWindow, QtCore
from PyQt5 import QtGui
import matplotlib.pyplot as plt
from UI.external_widgets.error_graph import Error_Graph
from UI.external_widgets.points_input import Points_Input
import numpy as np
import threading
from Algorithms.AGB import AGB
from Algorithms.dieta import Dieta

def mapStringInt(value):
    edad = value[0]
    if edad:
        if edad[0] is '>':
            m = [51]
            yield m
        else:
            mM = list(map(float,edad.split('-')))
            yield mM
    else:
        yield []
    for i in value[1:]:
        if i.strip():
            b = float(i.split(' ')[0])
            yield b
        else:
            yield i.strip()

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Points_Input, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        
        self.init_information_table()
        self.datos = list(map(list,map(mapStringInt, np.array(self.informacion_recomendada)[1:,1:])))
        self.inp_edad.valueChanged.connect(self.edadChanged)
        self.btn_train.clicked.connect(self.train_som)
        self.cbx_sexo.currentTextChanged.connect(self.sexoChanged)
        self.rb_emb.toggled.connect(lambda:self.edadChanged(self.inp_edad.value()))
        self.rb_lac.toggled.connect(lambda:self.edadChanged(self.inp_edad.value()))
        self.rb_ning.toggled.connect(lambda:self.edadChanged(self.inp_edad.value()))
        

    

    def edadChanged(self, value):
        for fila in self.datos:
            edad = fila[0]
            if self.cbx_sexo.currentText() == 'Hombre':
                if len(edad) == 2:
                    if float(value) >= edad[0] and float(value) <= edad[1]:
                        if fila[1]:
                            self.inp_kcal.setValue(fila[1])
                        if fila[2]:
                            self.inp_vit_a.setValue(fila[2])
                        if fila[3]:
                            self.inp_fibra.setValue(fila[3])
                        if fila[4]:
                            self.inp_calcio.setValue(fila[4])
                        if fila[5]:
                            self.inp_hierro.setValue(fila[5])
                        break
                elif len(edad) == 1:
                    if float(value) >= edad[0]:
                        if fila[1]:
                            self.inp_kcal.setValue(fila[1])
                        if fila[2]:
                            self.inp_vit_a.setValue(fila[2])
                        if fila[3]:
                            self.inp_fibra.setValue(fila[3])
                        if fila[4]:
                            self.inp_calcio.setValue(fila[4])
                        if fila[5]:
                            self.inp_hierro.setValue(fila[5])
                        break
            elif self.cbx_sexo.currentText() == 'Mujer':
                if self.rb_ning.isChecked():
                    if len(edad) == 2:
                        if float(value) >= edad[0] and float(value) <= edad[1]:
                            if fila[1]:
                                self.inp_kcal.setValue(fila[1])
                            if fila[2]:
                                self.inp_vit_a.setValue(fila[2])
                            if fila[3]:
                                self.inp_fibra.setValue(fila[3])
                            if fila[4]:
                                self.inp_calcio.setValue(fila[4])
                            if fila[5]:
                                self.inp_hierro.setValue(fila[5])
                            break
                    elif len(edad) == 1:
                        if float(value) >= edad[0]:
                            if fila[1]:
                                self.inp_kcal.setValue(fila[1])
                            if fila[2]:
                                self.inp_vit_a.setValue(fila[2])
                            if fila[3]:
                                self.inp_fibra.setValue(fila[3])
                            if fila[4]:
                                self.inp_calcio.setValue(fila[4])
                            if fila[5]:
                                self.inp_hierro.setValue(fila[5])
                            break
                elif self.rb_emb.isChecked():
                    if len(edad) == 2:
                        if float(value) >= edad[0] and float(value) <= edad[1]:
                            if fila[1]:
                                self.inp_kcal.setValue(fila[1] + 300)
                            if fila[2]:
                                self.inp_vit_a.setValue(fila[2])
                            if fila[3]:
                                self.inp_fibra.setValue(fila[3])
                            if fila[4]:
                                self.inp_calcio.setValue(1.3)
                            if fila[5]:
                                self.inp_hierro.setValue(1.3)
                            break
                    elif len(edad) == 1:
                        if float(value) >= edad[0]:
                            if fila[1]:
                                self.inp_kcal.setValue(fila[1] + 300)
                            if fila[2]:
                                self.inp_vit_a.setValue(fila[2])
                            if fila[3]:
                                self.inp_fibra.setValue(fila[3])
                            if fila[4]:
                                self.inp_calcio.setValue(1.3)
                            if fila[5]:
                                self.inp_hierro.setValue(1.3)
                            break
                elif self.rb_lac.isChecked():
                    if len(edad) == 2:
                        if float(value) >= edad[0] and float(value) <= edad[1]:
                            if fila[1]:
                                self.inp_kcal.setValue(fila[1] + 300)
                            if fila[2]:
                                self.inp_vit_a.setValue(fila[2])
                            if fila[3]:
                                self.inp_fibra.setValue(fila[3])
                            if fila[4]:
                                self.inp_calcio.setValue(1.3)
                            if fila[5]:
                                self.inp_hierro.setValue(1.3)
                            break
                    elif len(edad) == 1:
                        if float(value) >= edad[0]:
                            if fila[1]:
                                self.inp_kcal.setValue(fila[1] + 300)
                            if fila[2]:
                                self.inp_vit_a.setValue(fila[2])
                            if fila[3]:
                                self.inp_fibra.setValue(fila[3])
                            if fila[4]:
                                self.inp_calcio.setValue(1.3)
                            if fila[5]:
                                self.inp_hierro.setValue(1.3)
                            break


    def sexoChanged(self, value):
        if value == 'Mujer':
            self.rb_ning.setChecked(True)
            self.rb_ning.setEnabled(True)
            self.rb_lac.setEnabled(True)
            self.rb_emb.setEnabled(True)
        elif value == 'Hombre':
            self.rb_ning.setChecked(False)
            self.rb_emb.setChecked(False)
            self.rb_lac.setChecked(False)
            self.rb_ning.setEnabled(False)
            self.rb_lac.setEnabled(False)
            self.rb_emb.setEnabled(False)
        self.edadChanged(self.inp_edad.value())

    def init_information_table(self):
        self.tbl_informacion.horizontalHeader().setVisible(True)
        self.tbl_informacion.verticalHeader().setVisible(True)
        self.tbl_informacion.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tbl_informacion.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.informacion_recomendada = []

        info = open('datos/informacion_recomendada.csv','r')
        for dato in info.readlines():
            dato = dato.split(',')
            self.informacion_recomendada.append(dato)

        datos = list(map(list,np.array(self.informacion_recomendada)[1:,1:]))

        for columna in range(len(self.informacion_recomendada[0])-1):
            for fila in range(len(np.array(self.informacion_recomendada).T[0])-1):
                self.tbl_informacion.setItem(fila, columna, QtWidgets.QTableWidgetItem(datos[fila][columna]))




    def train_som(self):
        self.kilocalorias_max = float(self.inp_kcal.value())
        self.vitamina_max = float(self.inp_vit_a.value())
        self.fibra_max = float(self.inp_fibra.value())
        self.calcio_max = float(self.inp_calcio.value())
        self.hierro_max = float(self.inp_hierro.value())
        
        self.btn_train.setEnabled(False)
        self.btn_asignar.setEnabled(False)

        self.generaciones = int(self.inp_generaciones.value())
        self.individuos = int(self.inp_individuos.value())
        self.dimensiones = int(self.inp_dimensiones.value())
        self.p_mut = float(self.inp_p_mutacion.value())

        self.dieta = Dieta(self.kilocalorias_max, self.vitamina_max, self.fibra_max, self.calcio_max, self.hierro_max)
        self.agb = AGB(self.individuos, self.dimensiones, 1, self.generaciones, self.p_mut, self.dieta)
        self.agb.countChanged.connect(self.onCountChanged)
        self.agb.finished.connect(self.onFinished)
        self.agb.start()

    def onCountChanged(self, value):
        self.progressBar.setValue(value)

    def onFinished(self):
        self.progressBar.setValue(100)
        self.error_graph.graph_errors(self.agb.historicos)
        self.btn_train.setEnabled(True)
        self.btn_asignar.setEnabled(True)