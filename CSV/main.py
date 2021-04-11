import sys
import pandas as pd 
import matplotlib.pyplot as plt 

from matplotlib import dates as mpl_dates
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QErrorMessage,QFileDialog,QTableWidgetItem
from codigo.ventanacsv import Ui_VentanaPrincipal

#CHECAR COMO SOLUCIONAR CUANDO ELIGAN EL CSV Y ELIGA LA OPCION DE VERCSV EN EL LLENADO DE DATOS 
excel=""
notas=""
titulo=""
etiqueta1=""
etiqueta2=""
etiqueta3=""
etiqueta4=""
listaEncabezados=[]
listadatos=[]
listacolumnas=[]
listacolores=['#00FFFF','#0000FF', '#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E',
'#6495ED','#DC143C','#00008B','#008B8B','#B8860B','#A9A9A9','#006400', '#BDB76B','#8B008B','#FF8C00','#8B0000'
,'#483D8B','#2F4F4F','#FF1493','#1E90FF','#228B22','#FFD700','#DAA520','#7CFC00','#0000CD','#FF0000','#9ACD32']


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

    #ESTA OPCION ESTA BIEN 
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


    def REALIZAR(self):
        global notas
        global excel
        global listaEncabezados
        global listadatos
        global listacolumnas
        contador=0
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

        #ESTA OPCION ESTA BIEN
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

        # CHECAR ESTA OPCION QEU AGRUPE LOS NOMBRES CON LA SUMA DE SUS VALORES 
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

        #ESTA OPCION ESTA BIEN
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

        #ESTA OPCION ESTA BIEN TAMBIEN
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
        
        #ESTA OPCION ESTA BIEN  FALTA HACER EL .UNIQUE
        elif self.ui.graficaBarras.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0:
                try:
                    self.ui.errorarchivo.setText("")
                    notas=pd.read_csv(excel,encoding='utf-8')
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

        # AQUI FALTA HACER EL CODIGO DE TENDENCIA GRUPAL DE PREFERENCIA VALORES UNICOAS MAXIMO 30 PARA QUE SE VEA BIEN LA GRAFICA
        if self.ui.graficarTenGru.isChecked()==True:
            if len(titulo)>0 and len(etiqueta1)>0 and len(etiqueta2)>0 and len(etiqueta4)>0:
                
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
               
            else:
                self.ui.errorarchivo.setText("Ingrese los datos necesarios")

        
                
           
        

            

        

        
        
            
            

            

        


if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())