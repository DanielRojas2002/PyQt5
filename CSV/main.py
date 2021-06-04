import sys
import pandas as pd 
import matplotlib.pyplot as plt 
import os 
from os import remove

from matplotlib import dates as mpl_dates
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QErrorMessage,QFileDialog,QTableWidgetItem
from codigo.ventanacsv import Ui_VentanaPrincipal
from codigo.ventanaopciones import Ui_VentanaOpciones
from codigo.ventana_eliminador import Ui_Ventana_Eliminar
from codigo.ventanaunircsv import Ui_Ventana_Unir
from codigo.ventana_eliminador_columnas import Ui_Ventana_Eliminar_Columnas
from codigo.ventanaseleccion import Ui_VentanaSeleccionar


excel=""
notas=""
titulo=""
etiqueta1=""
etiqueta2=""
etiqueta3=""
etiqueta4=""
csv1=""
csv2=""
datocolumna=""
seleccion=""
df_condicion=""
listaEncabezados=[]
listadatos=[]
listacolumnas=[]
statuscsv=""
validacioninforme=""
listacolores=['#00FFFF','#0000FF', '#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E',
'#6495ED','#DC143C','#00008B','#008B8B','#B8860B','#A9A9A9','#006400', '#BDB76B','#8B008B','#FF8C00','#8B0000'
,'#483D8B','#2F4F4F','#FF1493','#1E90FF','#228B22','#FFD700','#DAA520','#7CFC00','#0000CD','#FF0000','#9ACD32']


#AQUI INICIA LA CLASE DE LA INTERFAZ
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

    #ESTA OPCION BUSCA Y SELECCIONA LA RUTA DONDE ESTA EL ARCHIVO CSV 
    def Buscar(self):
        self.ui.GRAFICAR.setDisabled(True)
        try:
            global excel
            global notas
            global listaEncabezados
            listaEncabezados=[]
            self.ui.tableWidget.setSortingEnabled(False)
            self.ui.encabezados.clear()
            self.ui.tableWidget.clear()
            self.ui.tableDescripcion.clear()
            self.ui.cantidad_registros.setText("")
            ruta=QFileDialog.getOpenFileName(self,'Open file')
            for dato in ruta[::-1]:
                excel=dato
            self.ui.nombreruta.setText(excel)
        except:
            self.ui.nombreruta.setText("No se Encontro el Archivo")

    # ESTA OPCION ES UN BOTON EL CUAL BUSCA EL RADIOBUTTON ESTA SELECCIONADO
    def REALIZAR(self):
        global notas
        global excel
        global listaEncabezados
        global listadatos
        global listacolumnas
        contador=0
        # SI ESTE RAIDOBUTTON ESTA SELECCIONADO VA HACER ESTAS COSAS
        if self.ui.verCSV.isChecked()==True:
            self.ui.tableWidget.setSortingEnabled(False)
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
                notas=pd.read_csv(excel,encoding='utf-8')
                
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
                self.ui.tableWidget.setSortingEnabled(True)
            
                for x in range(0,contador+1):
                    self.ui.tableWidget.setColumnWidth(x,200)
                               
            except:
                listaEncabezados=[]
                listadatos=[]
                self.ui.encabezados.clear()
                self.ui.tableWidget.clear()
                self.ui.errorarchivo.setText("El Archivo no se puede leer")

        # SI ESTE RAIDOBUTTON ESTA SELECCIONADO VA HACER ESTAS COSAS
        elif self.ui.Estadistica.isChecked()==True:
            try:
                self.ui.titulo_Grafico.setDisabled(True)
                self.ui.etiqueta_nombre.setDisabled(True)
                self.ui.etiqueta_valor.setDisabled(True)
                self.ui.etiqueta_usuario.setDisabled(True)
                self.ui.etiqueta_tiempo.setDisabled(True)

                self.ui.GRAFICAR.setDisabled(True)
                
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
                
                listacolumnas=[]
                notas=pd.read_csv(excel,encoding='utf-8')
                descripcion=notas.describe()
                

                for columna in descripcion:
                    listacolumnas.append(columna)
                                
                lista=[]
                listanueva=[]
                listadatos=[]
                contador=0

                for elemento in listacolumnas:
                    contador=contador+1
                    listanueva=[]
                    
                    desviacion=str(round(notas[elemento].std(),2))
                    maximo=str(round(notas[elemento].max(),2))
                    minimo=str(round(notas[elemento].min(),2))
                    promedio=str(round(notas[elemento].mean(),2))
                    
                    listanueva.append(desviacion)
                    listanueva.append(maximo)
                    listanueva.append(minimo)
                    listanueva.append(promedio)

                    lista.append(listanueva)
  
                registro=len(notas.index)    

                filas=contador
                self.ui.cantidad_registros.setText("")
                self.ui.cantidad_registros.setText("Cantidad de Registros: "+str(registro))
                listaDescripcion=["Desviacion","Maximo","Minimo","Promedio"]
                
                self.ui.tableDescripcion.setRowCount(filas)
                self.ui.tableDescripcion.setColumnCount(4)

                for registros in lista:
                    dato=(tuple(registros))
                    listadatos.append(dato)

                fila=0
                for registro in listadatos:
                    columna=0
                    for elemento in registro:
                        celda=QTableWidgetItem(str(elemento))
                        self.ui.tableDescripcion.setItem(fila,columna,celda)
                        columna=columna+1
                    fila=fila+1
                self.ui.tableDescripcion.setHorizontalHeaderLabels(listaDescripcion)
                self.ui.tableDescripcion.setVerticalHeaderLabels(listacolumnas)
                self.ui.tableDescripcion.setSortingEnabled(True)

                for x in range(0,contador+1):
                    self.ui.tableDescripcion.setColumnWidth(x,100)

            except:
                self.ui.tableDescripcion.clear()
                self.ui.errorarchivo.setText("ERROR")

        # SI ESTE RAIDOBUTTON ESTA SELECCIONADO VA HACER ESTAS COSAS
        elif self.ui.graficaPastel.isChecked()==True:
            self.ui.errorarchivo.setText("")

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

        # SI ESTE RAIDOBUTTON ESTA SELECCIONADO VA HACER ESTAS COSAS
        elif self.ui.graficaBarras.isChecked()==True:
            self.ui.errorarchivo.setText("")

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

        # SI ESTE RAIDOBUTTON ESTA SELECCIONADO VA HACER ESTAS COSAS
        elif self.ui.graficaTenInd.isChecked()==True: 

            self.ui.errorarchivo.setText("")
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

            self.ui.tituloGrafica.setText("DATOS PARA PODER GRAFICAR:\nTendencia(Usuario):")
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

        # SI ESTE RAIDOBUTTON ESTA SELECCIONADO VA HACER ESTAS COSAS
        elif self.ui.graficarTenGru.isChecked()==True:

            self.ui.errorarchivo.setText("")
            self.ui.titulo_Grafico.setEnabled(True)
            self.ui.etiqueta_nombre.setEnabled(True)
            self.ui.etiqueta_valor.setEnabled(True)

            self.ui.etiqueta_usuario.setDisabled(True)
            self.ui.etiqueta_usuario.setPlaceholderText("")

            self.ui.etiqueta_tiempo.setEnabled(True)
            self.ui.GRAFICAR.setEnabled(True)

            titulo=""
            etiqueta1=""
            etiqueta2=""
            etiqueta3=""
            etiqueta4=""

            self.ui.tituloGrafica.setText("DATOS PARA PODER GRAFICAR:\nTendencia(Grupal):")
            self.ui.titulo_Grafico.setPlaceholderText("Ingrese el Titulo del Grafico:")
            self.ui.etiqueta_nombre.setPlaceholderText("Ingrese la Etiqueta del Nombre:")
            self.ui.etiqueta_valor.setPlaceholderText("Ingrese la Etiqueta del Valor:")  
            self.ui.etiqueta_tiempo.setPlaceholderText("Ingrese la Etiqueta del Tiempo:")

            titulo=self.ui.titulo_Grafico.text()
            etiqueta1=self.ui.etiqueta_nombre.text()
            etiqueta2=self.ui.etiqueta_valor.text()
            etiqueta4=self.ui.etiqueta_tiempo.text()

        elif self.ui.masopciones.isChecked()==True:
            try:
                notas=pd.read_csv(excel,encoding='utf-8')
                self.hide()
                otraventana=VentanaOpciones(self)
                otraventana.show()
                self.ui.errorarchivo.setText("")
            except:
                self.ui.errorarchivo.setText("Tiene que seleccionar el Archivo")



    # ESTE BOTON ES EL BOTON GRAFICAR 
    def Graficar(self):
        global notas
        global excel
        global titulo
        global etiqueta1
        global etiqueta2
        global etiqueta3
        global etiqueta4
        global listacolores
        
       #Ya Funciona esta funcion VALORES UNICOS MAXIMO 40 SE PUEDEN MAS PERO SE VERA MAL LA GRAFICA
        if self.ui.graficaPastel.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0:
                try:
                
                    listasuma=[]
                    listanombres=[]
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel,encoding='utf-8')

                    nombreunicos=notas[etiqueta1].unique()
                    
                    
                    for x in nombreunicos:
                        listanombres.append(nombreunicos)
                        
                        valor=notas[[etiqueta1,etiqueta2]]
                        

                        dato=valor[etiqueta1]==x
                        DATOS=notas[dato]
                    
                        suma=DATOS[etiqueta2].sum()

                        listasuma.append(suma)
                                               
                    nombre=notas[etiqueta1].unique()                    
                    longitud=len(listasuma)
                    listacolores2=[]
                 
                    if longitud<=len(listacolores):
                        colores=listacolores[:longitud]

                        for color in colores:
                            listacolores2.append(color)

                    elif longitud>=len(listacolores):
                        colorenecesarios=longitud
                        contadorcolores=0
                        
                        for x in range(colorenecesarios):
                            listacolores2.append(listacolores[contadorcolores])               
                            contadorcolores=contadorcolores+1

                            if contadorcolores==len(listacolores):
                                contadorcolores=0
                                                        
                    porcentaje=notas[etiqueta2].sum()
                    porcentajeb=round(porcentaje)
                        
                    leyenda = []
                    for navegador, mercado in zip(nombre,listasuma):
                        mercado2=round((mercado/porcentajeb*100),2)
                        leyenda.append(navegador + '  (' + str(mercado2) + '%)')
                 
                    plt.pie(listasuma,labels=None,autopct="%0.1f %%",colors=listacolores2)
                    plt.title(titulo+"("+etiqueta1+":"+etiqueta2+")")
                    plt.rc('legend', fontsize=6)
                    plt.legend(leyenda,loc='best',bbox_to_anchor=(1.05, 1.0))
                    plt.show()
                
                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")
        
        #ESTA OPCION SACA GRAFICA DE BARRAS SE PERMITEN MUCHOS VALORES PERO ENTRE MENOS MEJOR SE VERA LA GRAFICA
        elif self.ui.graficaBarras.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0:
                try:
                    listasuma=[]
                    listanombres=[]
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel,encoding='utf-8')

                    nombreunicos=notas[etiqueta1].unique()
                    
                    
                    for x in nombreunicos:
                        valor=notas[[etiqueta1,etiqueta2]]
                        
                        dato=valor[etiqueta1]==x
                        DATOS=notas[dato]
                    
                        suma=DATOS[etiqueta2].sum()

                        listasuma.append(suma)
                                                
                    listanombres=notas[etiqueta1].unique()                   
                    longitud=len(listasuma)
                    listacolores2=[]
                    
                    if longitud<=len(listacolores):
                        colores=listacolores[:longitud]

                        for color in colores:
                            listacolores2.append(color)

                    elif longitud>=len(listacolores):
                        colorenecesarios=longitud
                        contadorcolores=0
                        
                        for x in range(colorenecesarios):
                            listacolores2.append(listacolores[contadorcolores])               
                            contadorcolores=contadorcolores+1

                            if contadorcolores==len(listacolores):
                                contadorcolores=0
                    
                    datoslimpios={}
                    datoslimpios["Nombres"]=listanombres
                    datoslimpios["Totales"]=listasuma

                    dataframe=pd.DataFrame(datoslimpios)
                    nombre=dataframe["Nombres"]
                    valor=dataframe["Totales"]

                
                    fig=plt.subplots()
                    plt.xlabel(etiqueta1,fontsize=20)
                    plt.ylabel(etiqueta2,fontsize=20)
                    plt.xticks(rotation=45)
                    plt.title(titulo+"("+etiqueta1+":"+etiqueta2+")",fontsize=20)
                    plt.bar(nombre,valor,color=listacolores2)
                    plt.grid(True)
                    plt.show()
                    
                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")
        

        #AQUI EL CSV TIENE QUE ESTAR LA FECHA COMO AÑO MES DIA (INDIVIDUAL)
        if self.ui.graficaTenInd.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0 and len(etiqueta3)>0 and len(etiqueta4)>0:
                try:
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel,encoding='utf-8')
                    notas[etiqueta4]=pd.to_datetime(notas[etiqueta4])
                    

                    dato=notas[etiqueta1]==etiqueta3
                    DATOS=notas[dato]

                    valor=DATOS[etiqueta2]
                    tiempo=DATOS[etiqueta4]
                
                    plt.style.use('seaborn')
                    plt.plot_date(tiempo,valor,linestyle="solid")
                    plt.gcf().autofmt_xdate()
                    formato=mpl_dates.DateFormatter('%d,%b,%Y')
                    plt.gca().xaxis.set_major_formatter(formato)
                    plt.title(titulo+": "+etiqueta1+": "+etiqueta4)
                    plt.xlabel(etiqueta3)
                    plt.ylabel(etiqueta2)
                    plt.tight_layout()
                    plt.show()
               
                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")

        #  TENDENCIA GRUPAL DE PREFERENCIA VALORES UNICOAS MAXIMO 30 PARA QUE SE VEA BIEN LA GRAFICA
        if self.ui.graficarTenGru.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0 and len(etiqueta4)>0:
                try:

                
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel,encoding='utf-8')

                    notas[etiqueta4]=pd.to_datetime(notas[etiqueta4])
                    
                    datos=notas[etiqueta1].unique()
            
                    plt.style.use('seaborn')
                    listalegend=[]
                    contadorcolores=0
                    longitud=len(listacolores)
                    fig,ax=plt.subplots()

                    for x in datos:
                        listalegend.append(x)
                        dato=notas[etiqueta1]==x
                        DATOS=notas[dato]

                        valor=DATOS[etiqueta2]
                        tiempo=DATOS[etiqueta4]
                        ax.plot(tiempo,valor,marker="o",linewidth=2,color=listacolores[contadorcolores])
                        contadorcolores=contadorcolores+1

                        if longitud==contadorcolores:
                            contadorcolores=0
                                
                    plt.gcf().autofmt_xdate()
                    formato=mpl_dates.DateFormatter('%d,%b,%Y')
                    plt.gca().xaxis.set_major_formatter(formato)
                    plt.title("GRAFICA LINEAL(GRUPAL)")
                    plt.xlabel(etiqueta1)
                    plt.ylabel(etiqueta2)          
                    plt.rc('legend', fontsize=6)
                    plt.legend(listalegend,loc='best',bbox_to_anchor=(1.05, 1.0))          
                    plt.show()

                except:
                    self.ui.errorarchivo.setText("Ingreso mal Una Etiqueta")

               
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")




class VentanaOpciones(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaOpciones,self).__init__(parent) 
        self.ui=Ui_VentanaOpciones()
        self.ui.setupUi(self)

        self.ui.regresar.clicked.connect(self.atras)

        self.ui.elegir.clicked.connect(self.elegir)

    def elegir(self):
        seleccion=self.ui.opciones.itemText(self.ui.opciones.currentIndex())
        
        if seleccion=="Agregar Columnas":
            pass
        
        elif seleccion=="Agregar Registros":
            pass
        
        elif seleccion=="Eliminar Columnas":
            self.hide()
            otraventana=VentanaEliminarColumnas(self)
            otraventana.show()
        
        elif seleccion=="Eliminar Registros":
            self.hide()
            otraventana=VentanaEliminarRegistros(self)
            otraventana.show()
        
        elif seleccion=="Segmentar dos CSV´s":
            self.hide()
            otraventana=VentanaUnirDosCSV(self)
            otraventana.show()
        
        elif seleccion=="Cambiar el Tipo de Dato de una columna":
            pass

        
        elif seleccion=="Hacer Operaciones entre columnas":
            pass

        elif seleccion=="Buscar Datos en especifico del CSV":
            self.hide()
            otraventana=VentanaSeleccionar(self)
            otraventana.show()

        

        
        
    def atras(self):
        self.parent().show()
        self.close()

class VentanaEliminarRegistros(QMainWindow):
    def __init__ (self,parent=None):
        super(VentanaEliminarRegistros,self).__init__(parent)
        self.ui=Ui_Ventana_Eliminar()
        self.ui.setupUi(self)

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.eliminar.clicked.connect(self.eliminar)

        try:
            global excel
            notas=pd.read_csv(excel,encoding='utf-8')

            for encabezados in notas.columns:
                listaEncabezados.append(encabezados) 

            listadatos=[]	
            filas=len(notas.index)	
            contador=len(notas.columns)
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
          
            self.ui.tableWidget.setColumnWidth(0,100)
            self.ui.tableWidget.setColumnWidth(1,220)

          
            for x in range(1,filas+1):
                self.ui.opciones.addItem(str(x))

        except:
            self.ui.titulo.setText("No Hay Registros a borrar")

    def eliminar(self):
        try:

            global excel
            notas=pd.read_csv(excel,encoding='utf-8')

            seleccion=int(self.ui.opciones.itemText(self.ui.opciones.currentIndex()))
            seleccion=seleccion-1
            notas.drop([seleccion],axis="index",inplace=True)
            remove(excel)

            ruta=excel
            

            notas.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))

            notas=pd.read_csv(excel,encoding='utf-8')
            listaEncabezados=[]
            listadatos=[]

            for encabezados in notas.columns:
                listaEncabezados.append(encabezados)
            
                
            filas=len(notas.index)	
            contador=len(notas.columns)
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
            

            
            self.ui.tableWidget.setColumnWidth(0,100)
            self.ui.tableWidget.setColumnWidth(1,220)

            self.ui.opciones.clear()
            for x in range(1,filas+1):
                self.ui.opciones.addItem(str(x))

        except:
            self.ui.titulo.setText("No Hay Registros a borrar")


            
        

    def atras(self):
        self.parent().show()
        self.close()


class VentanaUnirDosCSV(QMainWindow):
    def __init__ (self,parent=None):
        super(VentanaUnirDosCSV,self).__init__(parent)
        self.ui=Ui_Ventana_Unir()
        self.ui.setupUi(self)
       
        self.ui.regresar.clicked.connect(self.atras)

        self.ui.botoncsv1.clicked.connect(self.csv1)
        self.ui.botoncsv2.clicked.connect(self.csv2)
        self.ui.unir.clicked.connect(self.UNIR)

    
    def csv1(self):
        global csv1
        global listaEncabezados
        listaEncabezados=[]
        try:
            ruta=QFileDialog.getOpenFileName(self,'Open file')
            for dato in ruta[::-1]:
                csv1=dato
            self.ui.ruta1.setText(csv1)
            csvreferencia=pd.read_csv(csv1,encoding='utf-8')
            self.ui.columnajoin.clear()
            for encabezados in csvreferencia.columns:
                listaEncabezados.append(encabezados)
                self.ui.columnajoin.addItem(str(encabezados))

        except:
            self.ui.ruta1.setText("No se Encontro el Archivo")

    def csv2(self):
        global csv2
        try:
            ruta=QFileDialog.getOpenFileName(self,'Open file')
            for dato in ruta[::-1]:
                csv2=dato
            self.ui.ruta2.setText(csv2)
        except:
            self.ui.ruta2.setText("No se Encontro el Archivo")

    def UNIR(self):
        try:
            global csv1
            global csv2
            columna=self.ui.columnajoin.itemText(self.ui.columnajoin.currentIndex())
            join=self.ui.tipo_join.itemText(self.ui.tipo_join.currentIndex())
            df1=pd.read_csv(csv1,encoding='utf-8')
            df2=pd.read_csv(csv2,encoding='utf-8')

            try:
  
                if len(self.ui.nombrearchivo.text())>0:
                    ruta="./"+self.ui.nombrearchivo.text()+".csv"
                else:
                    self.ui.resultado.setText("Nombre del Archivo?")

                if join=="Inner" and len(self.ui.nombrearchivo.text())>0:
                    df_unido=df1.merge(df2,on=columna,how="inner")
                    DF_UNIDO=pd.DataFrame(df_unido)
                    DF_UNIDO.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.resultado.setText("Ya se guardo el csv")
                    self.ui.nombrearchivo.clear()
                    
                    

                elif join=="Outer" and len(self.ui.nombrearchivo.text())>0:
                    df_unido=df1.merge(df2,on=columna,how="outer")
                    DF_UNIDO=pd.DataFrame(df_unido)
                    DF_UNIDO.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.resultado.setText("Ya se guardo el csv")
                    self.ui.nombrearchivo.clear()

                elif join=="Left" and len(self.ui.nombrearchivo.text())>0:
                    df_unido=df1.merge(df2,on=columna,how="left")
                    DF_UNIDO=pd.DataFrame(df_unido)
                    DF_UNIDO.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.resultado.setText("Ya se guardo el csv")
                    self.ui.nombrearchivo.clear()

                elif join=="Right" and len(self.ui.nombrearchivo.text())>0:
                    df_unido=df1.merge(df2,on=columna,how="right")
                    DF_UNIDO=pd.DataFrame(df_unido)
                    DF_UNIDO.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.resultado.setText("Ya se guardo el csv")
                    self.ui.nombrearchivo.clear()

                

            except:
                self.ui.resultado.setText("La columna no coincide")
        except:
            self.ui.resultado.setText("Eliga los Archivos")
            
       

    def atras(self):
        self.parent().show()
        self.close()


class VentanaEliminarColumnas(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaEliminarColumnas,self).__init__(parent)
        self.ui=Ui_Ventana_Eliminar_Columnas()
        self.ui.setupUi(self)

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.listaColumnas.itemClicked.connect(self.seleccion) 
        self.ui.eliminar.clicked.connect(self.eliminar)
		

        try:
            global excel
            notas=pd.read_csv(excel,encoding='utf-8')

            for encabezados in notas.columns:
                self.ui.listaColumnas.addItem(str(encabezados)) 
        except:
            self.ui.titulo.setText("No hay Columnas")

    def seleccion(self):
        global datocolumna 
        datocolumna=self.ui.listaColumnas.currentItem().text()
        self.ui.columna.setText(str(datocolumna))

    def eliminar(self):
        try:
            global datocolumna 
            global excel
            df=pd.read_csv(excel,encoding='utf-8')
            df.drop([datocolumna],axis="columns",inplace=True)
            remove(excel)

            ruta=excel
            
            df.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))

            df=pd.read_csv(excel,encoding='utf-8')
            self.ui.listaColumnas.clear()
            self.ui.columna.clear()

            for encabezados in df.columns:
                self.ui.listaColumnas.addItem(str(encabezados)) 
            

        except:
            self.ui.listaColumnas.clear()
            self.ui.columna.clear()
            self.ui.titulo.setText("No Hay Columnas")

        

    def atras(self):
        self.parent().show()
        self.close()

class VentanaSeleccionar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaSeleccionar,self).__init__(parent)
        self.ui=Ui_VentanaSeleccionar()
        self.ui.setupUi(self)

        self.ui.atras.clicked.connect(self.atras)
        self.ui.realizar.clicked.connect(self.realizar)
        self.ui.seleccionar.clicked.connect(self.seleccionar)
        self.ui.generarinforme.clicked.connect(self.generarcsv)
        
        global listaEncabezados
        notas=pd.read_csv(excel,encoding='utf-8')
        listaEncabezados=[]

        for encabezados in notas.columns:
            listaEncabezados.append(encabezados)

        

    def seleccionar(self):
        global seleccion
        global listaEncabezados
        
        self.ui.titulo2.setText("")
        self.ui.dato.setText("")
        selecciones=self.ui.opciones.itemText(self.ui.opciones.currentIndex())

        if selecciones=="TODOS":
            seleccion="TODOS"
            self.ui.dato.setDisabled(True)
            self.ui.opciones_2.setDisabled(True)
            self.ui.opciones_2.clear()
            self.ui.tableWidget.clear()
            

        elif selecciones=="Especifico":
            seleccion="Especifico"
            self.ui.dato.setEnabled(True)
            self.ui.opciones_2.setEnabled(True)
            self.ui.opciones_2.clear()
            self.ui.tableWidget.clear()
        
            for elemento in listaEncabezados:
                self.ui.opciones_2.addItem(elemento)

        elif selecciones=="Empiece con...":
            seleccion="Empiece con..."
            self.ui.dato.setEnabled(True)
            self.ui.opciones_2.setEnabled(True)
            self.ui.opciones_2.clear()
            self.ui.tableWidget.clear()

            for elemento in listaEncabezados:
                self.ui.opciones_2.addItem(elemento)

        elif selecciones=="Termine con...":
            seleccion="Termine con..."
            self.ui.dato.setEnabled(True)
            self.ui.opciones_2.setEnabled(True)
            self.ui.opciones_2.clear()
            self.ui.tableWidget.clear()

            for elemento in listaEncabezados:
                self.ui.opciones_2.addItem(elemento)


    def realizar(self):
        global seleccion
        global listaEncabezados
        global excel
        global statuscsv
        global validacioninforme
        statuscsv=""

        if seleccion=="TODOS":
            statuscsv="TODOS"
            try:
                notas=pd.read_csv(excel,encoding='utf-8')
                self.ui.tableWidget.clear()
                listadatos=[]
                contador=0
                otrocontador=0
                
                for x in listaEncabezados:
                    contador=contador+1

                filas=len(notas.index)
                self.ui.tableWidget.setRowCount(filas)
                self.ui.tableWidget.setColumnCount(contador)
                
                for registros in notas.values:
                    otrocontador=otrocontador+1
                    dato=(tuple(registros))
                    listadatos.append(dato)

                if otrocontador==0:
                    self.ui.titulo2.setText("No Hay Registros")
                    validacioninforme=0

                else:
                    fila=0
                    for registro in listadatos:
                        columna=0
                        for elemento in registro:
                            celda=QTableWidgetItem(str(elemento))
                            self.ui.tableWidget.setItem(fila,columna,celda)
                            columna=columna+1
                        fila=fila+1
                    self.ui.tableWidget.setHorizontalHeaderLabels(listaEncabezados)
                    self.ui.tableWidget.setSortingEnabled(True)
                
                    for x in range(0,contador+1):
                        self.ui.tableWidget.setColumnWidth(x,200)

            except:
                self.ui.titulo2.setText("No Hay Registros")


        elif seleccion=="Especifico":
            global df_condicion
            statuscsv=""
            statuscsv="Especifico"
            try:

                notas=pd.read_csv(excel,encoding='utf-8')
                columna=str(self.ui.opciones_2.itemText(self.ui.opciones_2.currentIndex()))
                dato=str((self.ui.dato.text()))

                for encabezado in listaEncabezados:
                    notas[encabezado]=notas[encabezado].astype('object')

                df=pd.DataFrame(notas)
                
                try:
                    df_condicion=df.loc[(df[columna]==int(dato))]
                    
                except:
                    df_condicion=df.loc[(df[columna]==str(dato))]
                    
                self.ui.tableWidget.clear()
                listadatos=[]
                contador=0
                otrocontador=0

                for x in listaEncabezados:
                    contador=contador+1
                    

                filas=len(df_condicion.index)
                self.ui.tableWidget.setRowCount(filas)
                self.ui.tableWidget.setColumnCount(contador)
                
                for registros in df_condicion.values:
                    otrocontador=otrocontador+1
                    dato=(tuple(registros))
                    listadatos.append(dato)

                if otrocontador==0:
                    self.ui.titulo2.setText("No Hay Registros")
                    validacioninforme=0

                else:
                    fila=0
                    for registro in listadatos:
                        columna=0
                        for elemento in registro:
                            celda=QTableWidgetItem(str(elemento))
                            self.ui.tableWidget.setItem(fila,columna,celda)
                            columna=columna+1
                        fila=fila+1
                    self.ui.tableWidget.setHorizontalHeaderLabels(listaEncabezados)
                    self.ui.tableWidget.setSortingEnabled(True)
                
                    for x in range(0,contador+1):
                        self.ui.tableWidget.setColumnWidth(x,200)

            except:
                self.ui.titulo2.setText("No Hay Registros")

    def generarcsv(self):
        global statuscsv 
        global df_condicion
        global excel
        global validacioninforme
        
        
        if statuscsv=="TODOS":
            if validacioninforme==0:
                self.ui.titulo2.setText("No se puede generar el Informe")

            else:
                try:
                    ruta="./"+"Reporte TODOS"+".csv"
                    remove(ruta)
                    notas=pd.read_csv(excel,encoding='utf-8')
                    notas.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.titulo2.setText("Ya se genero el CSV")
                except:
                    ruta="./"+"Reporte TODOS"+".csv"
                    notas=pd.read_csv(excel,encoding='utf-8')
                    notas.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.titulo2.setText("Ya se genero el CSV")
                
            

        elif statuscsv=="Especifico":
            if validacioninforme==0:
                self.ui.titulo2.setText("No se puede generar el Informe")
                
            else:
                try:
                    ruta="./"+"Reporte "+self.ui.dato.text()+".csv"
                    remove(ruta)
                    df_condicion.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.titulo2.setText("Ya se genero el CSV")
                except:
                    ruta="./"+"Reporte "+self.ui.dato.text()+".csv"
                    df_condicion.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                    self.ui.titulo2.setText("Ya se genero el CSV")



    def atras(self):
        self.parent().show()
        self.close()


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())