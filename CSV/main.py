import sys
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import dates as mpl_dates
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QErrorMessage,QFileDialog,QTableWidgetItem
from codigo.ventanacsv import Ui_VentanaPrincipal


excel=""
notas=""
titulo=""
etiqueta1=""
etiqueta2=""
etiqueta3=""
etiqueta4=""
listaEncabezados=[]
listadatos=[]
class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__()
        self.ui=Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.ui.BUSCAR.clicked.connect(self.Buscar)
        self.ui.realizar.clicked.connect(self.REALIZAR)
        self.ui.GRAFICAR.clicked.connect(self.Graficar)

        self.ui.titulo_Grafico.setDisabled(True)
        self.ui.etiqueta_nombre.setDisabled(True)
        self.ui.etiqueta_valor.setDisabled(True)
        self.ui.etiqueta_usuario.setDisabled(True)
        self.ui.etiqueta_tiempo.setDisabled(True)
        self.ui.GRAFICAR.setDisabled(True)


    def Buscar(self):
        self.ui.GRAFICAR.setDisabled(True)
        try:
            global excel
            global notas
            global listaEncabezados
            listaEncabezados=[]
            self.ui.encabezados.clear()
            self.ui.tableWidget.clear()
            ruta=QFileDialog.getOpenFileName(self,'Open file')
            for dato in ruta[::-1]:
                excel=dato
            self.ui.nombreruta.setText(excel)
        except:
            self.ui.nombreruta.setText("No se Encontro el Archivo")

    def REALIZAR(self):
        global notas
        global excel
        global listaEncabezados
        global listadatos
        contador=0
        if self.ui.verCSV.isChecked()==True:
            self.ui.titulo_Grafico.setDisabled(True)
            self.ui.etiqueta_nombre.setDisabled(True)
            self.ui.etiqueta_valor.setDisabled(True)
            self.ui.etiqueta_usuario.setDisabled(True)
            self.ui.etiqueta_tiempo.setDisabled(True)

            self.ui.GRAFICAR.setDisabled(True)
            try:
                self.ui.tituloGrafica.setText("")
                self.ui.titulo_Grafico.setPlaceholderText("")
                self.ui.etiqueta_nombre.setPlaceholderText("")
                self.ui.etiqueta_valor.setPlaceholderText("")
                self.ui.etiqueta_usuario.setPlaceholderText("")
                self.ui.etiqueta_tiempo.setPlaceholderText("")


                self.ui.titulo_Grafico.clear()
                self.ui.etiqueta_nombre.clear()
                self.ui.etiqueta_valor.clear()
                self.ui.etiqueta_usuario.clear()
                self.ui.etiqueta_tiempo.clear()

                self.ui.encabezados.clear()
                self.ui.tableWidget.clear()
                listaEncabezados=[]
                listadatos=[]
                notas=pd.read_csv(excel)
                
                for encabezados in notas.columns:
                    listaEncabezados.append(encabezados)

                for x in listaEncabezados:
                    contador=contador+1
                    self.ui.encabezados.addItem(x)

                self.ui.errorarchivo.setText("")

                filas=len(notas.index)
                self.ui.tableWidget.setRowCount(filas)
                self.ui.tableWidget.setColumnCount(contador)
                


                for registros in notas.values:
                    dato=(tuple(registros))
                    listadatos.append(dato)
                
                fila=0
                for registro in listadatos:
                    columna=0
                    for elemento in registro:
                        celda=QTableWidgetItem(str(elemento))
                        self.ui.tableWidget.setItem(fila,columna,celda)
                        columna=columna+1
                    fila=fila+1
                self.ui.tableWidget.setHorizontalHeaderLabels(listaEncabezados)
                    
               

            except:
                listaEncabezados=[]
                listadatos=[]
                self.ui.encabezados.clear()
                self.ui.tableWidget.clear()
                self.ui.errorarchivo.setText("El Archivo no se puede leer")

        elif self.ui.graficaPastel.isChecked()==True:
            self.ui.titulo_Grafico.setEnabled(True)
            self.ui.etiqueta_nombre.setEnabled(True)
            self.ui.etiqueta_valor.setEnabled(True)
            self.ui.GRAFICAR.setEnabled(True)

            self.ui.etiqueta_usuario.clear()
            self.ui.etiqueta_tiempo.clear()


            
            self.ui.etiqueta_usuario.setDisabled(True)
            self.ui.etiqueta_tiempo.setDisabled(True)
            global titulo
            global etiqueta1
            global etiqueta2
            global etiqueta3
            global etiqueta4
            titulo=""
            etiqueta1=""
            etiqueta2=""
            etiqueta3=""
            etiqueta4=""
            self.ui.tituloGrafica.setText("DATOS PARA PODER GRAFICAR:\nPASTEL:")
            self.ui.titulo_Grafico.setPlaceholderText("Ingrese el Titulo del Grafico:")
            self.ui.etiqueta_nombre.setPlaceholderText("Ingrese la Etiqueta del Nombre:")
            self.ui.etiqueta_valor.setPlaceholderText("Ingrese la Etiqueta del Valor:")
            self.ui.etiqueta_usuario.setPlaceholderText("")
            self.ui.etiqueta_tiempo.setPlaceholderText("")
            
            titulo=self.ui.titulo_Grafico.text()
            etiqueta1=self.ui.etiqueta_nombre.text()
            etiqueta2=self.ui.etiqueta_valor.text()

        elif self.ui.graficaBarras.isChecked()==True:
            self.ui.titulo_Grafico.setEnabled(True)
            self.ui.etiqueta_nombre.setEnabled(True)
            self.ui.etiqueta_valor.setEnabled(True)
            self.ui.GRAFICAR.setEnabled(True)

            self.ui.etiqueta_usuario.clear()
            self.ui.etiqueta_tiempo.clear()

            self.ui.etiqueta_usuario.setDisabled(True)
            self.ui.etiqueta_tiempo.setDisabled(True)

            titulo=""
            etiqueta1=""
            etiqueta2=""
            etiqueta3=""
            etiqueta4=""
            self.ui.tituloGrafica.setText("DATOS PARA PODER GRAFICAR:\nBARRAS:")
            self.ui.titulo_Grafico.setPlaceholderText("Ingrese el Titulo del Grafico:")
            self.ui.etiqueta_nombre.setPlaceholderText("Ingrese la Etiqueta del Nombre:")
            self.ui.etiqueta_valor.setPlaceholderText("Ingrese la Etiqueta del Valor:")
            self.ui.etiqueta_usuario.setPlaceholderText("")
            self.ui.etiqueta_tiempo.setPlaceholderText("")
            
            titulo=self.ui.titulo_Grafico.text()
            etiqueta1=self.ui.etiqueta_nombre.text()
            etiqueta2=self.ui.etiqueta_valor.text()

        elif self.ui.graficaTenInd.isChecked()==True:

            self.ui.titulo_Grafico.setEnabled(True)
            self.ui.etiqueta_nombre.setEnabled(True)
            self.ui.etiqueta_valor.setEnabled(True)
            self.ui.etiqueta_usuario.setEnabled(True)
            self.ui.etiqueta_tiempo.setEnabled(True)
            self.ui.GRAFICAR.setEnabled(True)

            titulo=""
            etiqueta1=""
            etiqueta2=""
            etiqueta3=""
            etiqueta4=""
            self.ui.tituloGrafica.setText("DATOS PARA PODER GRAFICAR:\nTendencia\n(Usuario):")
            self.ui.titulo_Grafico.setPlaceholderText("Ingrese el Titulo del Grafico:")
            self.ui.etiqueta_nombre.setPlaceholderText("Ingrese la Etiqueta del Nombre:")
            self.ui.etiqueta_valor.setPlaceholderText("Ingrese la Etiqueta del Valor:")
            self.ui.etiqueta_usuario.setPlaceholderText("Ingrese la Etiqueta del Usuario:")
            self.ui.etiqueta_tiempo.setPlaceholderText("Ingrese la Etiqueta del Tiempo:")

            titulo=self.ui.titulo_Grafico.text()
            etiqueta1=self.ui.etiqueta_nombre.text()
            etiqueta2=self.ui.etiqueta_valor.text()
            etiqueta3=self.ui.etiqueta_usuario.text()
            etiqueta4=self.ui.etiqueta_tiempo.text()


    def Graficar(self):
        global notas
        global excel
        global titulo
        global etiqueta1
        global etiqueta2
        global etiqueta3
        global etiqueta4
        
       
        if self.ui.graficaPastel.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0:
                try:
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel)
                    nombre=notas[etiqueta1]
                    valor=notas[etiqueta2]

                    porcentaje=notas[etiqueta2].sum()
                    porcentajeb=round(porcentaje)
                    
                    leyenda = []
                    for navegador, mercado in zip(nombre,valor):
                        mercado2=round((mercado/porcentajeb*100),2)
                        leyenda.append(navegador + '  (' + str(mercado2) + '%)')

                    
                    plt.pie(valor,labels=None,autopct="%0.1f %%")
                    plt.title(titulo)
                    plt.rc('legend', fontsize=6)
                    plt.legend(leyenda,loc='best',bbox_to_anchor=(1.05, 1.0))
                    plt.show()
                    
                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")
        

        elif self.ui.graficaBarras.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0:
                try:
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel)
                    nombre=notas[etiqueta1]
                    valor=notas[etiqueta2]

                    fig=plt.subplots()
                    plt.xlabel(etiqueta1,fontsize=20)
                    plt.ylabel(etiqueta2,fontsize=20)
                    plt.xticks(rotation=45)
                    plt.title(titulo,fontsize=20)
                    plt.bar(nombre,valor)
                    plt.grid(True)
                    plt.show()
                    
                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")
        

        
        if self.ui.graficaTenInd.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0 and len(etiqueta3)>0 and len(etiqueta4)>0:
                try:
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel)
                    notas[etiqueta3]=pd.to_datetime(notas[etiqueta3])

                    dato=notas[etiqueta1]==etiqueta4
                    DATOS=notas[dato]

                    valor=DATOS[etiqueta2]
                    tiempo=DATOS[etiqueta3]

                    
                    plt.style.use('seaborn')
                    plt.plot_date(tiempo,valor,linestyle="solid")
                    plt.gcf().autofmt_xdate()
                    #formato=mpl_dates.DateFormatter('%b, %d, %Y')
                    #plt.gca().xaxis.set_major_formatter(formato)
                    plt.title(titulo+": "+etiqueta1+": "+etiqueta4)
                    plt.xlabel(etiqueta3)
                    plt.ylabel(etiqueta2)
                    plt.tight_layout()
                    plt.show()
                    

                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")

            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")

        
                
           
        

            

        

        
        
            
            

            

        


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())