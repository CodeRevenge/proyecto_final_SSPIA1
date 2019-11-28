from UI.Interface_AGB import QtWidgets, Ui_MainWindow, QtCore
from PyQt5 import QtGui
import matplotlib.pyplot as plt
from UI.external_widgets.error_graph import Error_Graph
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

class UI_Backend(QtWidgets.QMainWindow, Ui_MainWindow, Error_Graph):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        
        self.init_information_table()
        self.cargarAlimentos()
        self.datos = list(map(list,map(mapStringInt, np.array(self.informacion_recomendada)[1:,1:])))
        self.inp_edad.valueChanged.connect(self.edadChanged)
        self.btn_train.clicked.connect(self.ejecutar_algoritmo)
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

    def cargarAlimentos(self):
        self.alimentos = []

        info = open('datos/alimentos_recomendados.csv','r')
        for dato in info.readlines():
            dato = dato.split(',')
            self.alimentos.append(dato)
        info.close()

        self.actualizarTablaAlimentos()

    def actualizarTablaAlimentos(self):
        datos = list(map(list,np.array(self.alimentos)[1:,1:]))

        self.alimentos = []

        for i in datos:
            for ind, j in enumerate(i):
                try:
                    i[ind] = float(j)
                except ValueError:
                    pass 
            self.alimentos.append(i)

        for fila in range(len(np.array(self.alimentos).T[0])-1):
            self.tbl_alimentos.insertRow(self.tbl_alimentos.rowCount())
            for columna in range(len(self.alimentos[0])):
                if type(datos[fila][columna]) is float:
                    self.tbl_alimentos.setItem(fila, columna, QtWidgets.QTableWidgetItem('{:.7f}'.format(datos[fila][columna])))
                else:
                    self.tbl_alimentos.setItem(fila, columna, QtWidgets.QTableWidgetItem(datos[fila][columna]))

        self.tbl_alimentos.horizontalHeader().setVisible(True)
        self.tbl_alimentos.verticalHeader().setVisible(True)
        self.tbl_alimentos.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tbl_alimentos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


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

        info.close()




    def ejecutar_algoritmo(self):
        self.kilocalorias_max = float(self.inp_kcal.value())
        self.vitamina_max = float(self.inp_vit_a.value())
        self.fibra_max = float(self.inp_fibra.value())
        self.calcio_max = float(self.inp_calcio.value())
        self.hierro_max = float(self.inp_hierro.value())
        
        self.btn_train.setEnabled(False)

        self.generaciones = int(self.inp_generaciones.value())
        self.individuos = int(self.inp_individuos.value())
        self.alelos = len(self.alimentos)
        self.p_mut = float(self.inp_p_mutacion.value())

        # self.dieta = Dieta(self.kilocalorias_max, self.vitamina_max, self.fibra_max, self.calcio_max, self.hierro_max, self.alimentos)
        # self.agb = AGB(self.individuos, self.alelos, 1, self.generaciones, self.p_mut, self.dieta)
        # self.agb.countChanged.connect(self.onCountChanged)
        # self.agb.finished.connect(self.onFinished)
        # self.agb.start()

        self.dieta = Dieta(self.kilocalorias_max, self.vitamina_max, self.fibra_max, self.calcio_max, self.hierro_max, self.alimentos)
        self.agb = AGB(self.individuos, self.alelos, 1, self.generaciones, self.p_mut, self.dieta)
        self.agb.optimizar()
        self.onFinished()

        

    def onCountChanged(self, value):
        self.progressBar.setValue(value)

    def onFinished(self):
        self.progressBar.setValue(100)
        self.error_graph.graph_errors(self.agb.historicos)
        self.btn_train.setEnabled(True)
        self.resultados()

    def resultados(self):
        suma = [0]*(len(self.alimentos)-1)
        while self.tbl_resultados.rowCount() > 0:
            self.tbl_resultados.removeRow(0)
        for indx, sel in enumerate(self.agb._mejor_historico._cromosoma):
            if sel:
                datos = self.alimentos[indx]
                self.tbl_resultados.insertRow(self.tbl_resultados.rowCount())
                c = 0
                for columna in range(len(self.alimentos[0])):
                    if type(datos[columna]) is float:
                        self.tbl_resultados.setItem(self.tbl_resultados.rowCount()-1, columna, QtWidgets.QTableWidgetItem('{:.7f}'.format(datos[columna])))
                        suma[c] += datos[columna]
                        c += 1
                    else:
                        self.tbl_resultados.setItem(self.tbl_resultados.rowCount()-1, columna, QtWidgets.QTableWidgetItem(datos[columna]))
        
        self.tbl_resultados.insertRow(self.tbl_resultados.rowCount())
        for indx,dato in enumerate(suma):
            self.tbl_resultados.setItem(self.tbl_resultados.rowCount()-1, indx+1, QtWidgets.QTableWidgetItem('{:.7f}'.format(dato)))

        self.tbl_resultados.horizontalHeader().setVisible(True)
        self.tbl_resultados.verticalHeader().setVisible(True)
        self.tbl_resultados.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tbl_resultados.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
