import sqlite3
from sqlite3 import Error
import sys
import os
import time
import webbrowser
from tabulate import tabulate
import datetime
import pandas as pd

from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QErrorMessage,QTableWidgetItem
from codigos.creador import Ui_CREADORBD
from codigos.ventanap1 import Ui_VentanaP
from codigos.ventanap2 import Ui_VentanaP2
from codigos.tablas import Ui_CreacionTablas
from codigos.ventanavtablas import Ui_VentanaVisualizadoraTablas
from codigos.ventanaborrartablas import Ui_VentanaBTablas
from codigos.ventanavinsertar import Ui_VentanaValidacionInsertar
from codigos.ventanavcambiar import Ui_VentanaValidacioncambiar
from codigos.ventanavseleccionar import Ui_VentanaValidacionseleccionar
from codigos.ventanainformacion import Ui_Ventanainformacion
from codigos.ventanainsertar import Ui_VentanaInsertarRegistros
from codigos.ventanaseleccionar import Ui_VentanaSeleccionar
from codigos.ventanavborrarregistro import Ui_VentanaValidacionBorrarRegistros
from codigos.ventanaborrarregistro import Ui_VentanaBorrarRegistro
from codigos.ventanacambiarregistrop1 import Ui_VentanacambiarRegistro
from codigos.ventanamodificarregistro import Ui_VentanaModificarRegistros
from codigos.ventanavtxt import Ui_VentanaValidacionTXT
from codigos.ventanatxt import Ui_VentanaHacerTxt
from codigos.ventanavcsv import Ui_VentanaValidacionCSV
from codigos.ventanacsv import Ui_VentanaHacerCsv


nombre=""
nombretabla=""
dato=""
ultima=""
sqlinsertar=""
seleccion=""
Datoaborrar=""
Datoamodificar=""
valorModificar=""
primarykey=""
campos=""
seleccionTXT=""
seleccionCSV=""
contadorverificacion2=0
contadorvalidacion2=0
listaquery=[]
listadatos=[]
listatablas=[]
listavalores=[]
listaValoresInsertar=[]
listavalor=[]
listavalores2=[]
listacampos=[]
diccInsertar={}
listaDescripcion2=[]
listaPrimarykey2=[]
diccionariocsv={}
contador=0
contador2=1
contadorRegistros=1
contadorverificacion=0
contadorvalidacion=0

class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__()
        self.ui=Ui_VentanaP()
        self.ui.setupUi(self)

        self.ui.ingresar.clicked.connect(self.abrirVentana1)
        self.ui.crearbd.clicked.connect(self.abrirVentana2)
        self.ui.informacion.clicked.connect(self.VentanaInfo)

    def abrirVentana1(self):
        self.hide()
        if len(self.ui.nombrebd.text())>0:
            global nombre
            nombre=self.ui.nombrebd.text()
            db_filename=nombre+".db" 

            db_is_new = not os.path.exists("CRUD/bases/"+db_filename)

            if db_is_new:
                mensaje=QMessageBox()
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setText(f'No Existe la base de datos llamada :\n                      {nombre}')
                mensaje.setWindowTitle("MENSAJE")
                mensaje.exec_()
                
            else:
                self.hide()
                otraventana=Ventana2(self)
                otraventana.show()

        else:
            mensaje=QMessageBox()
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText('Ingrese el nombre de la Base de Datos')
            mensaje.setWindowTitle("MENSAJE")
            mensaje.exec_()

    def abrirVentana2(self):
        self.hide()
        otraventana=VentanaCreador(self)
        otraventana.show()

    def VentanaInfo(self):
        self.hide()
        otraventana=VentanaInfoo(self)
        otraventana.show()

       


class VentanaCreador(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaCreador,self).__init__(parent)
        self.ui=Ui_CREADORBD()
        self.ui.setupUi(self)

        self.ui.crearbd.clicked.connect(self.crear)
        self.ui.regresar.clicked.connect(self.atras)

    def crear(self):
        nombre=self.ui.bdnombre.text()
        db_filename=nombre+".db" 

        db_is_new = not os.path.exists("CRUD/bases/"+db_filename)

        if db_is_new:
            if len(self.ui.bdnombre.text())>0:
                bd=self.ui.bdnombre.text()
                self.ui.resultado.setText(f"La base de datos:{bd} se ha creado")
                try:
                    with sqlite3.connect(f"CRUD/bases/{bd}.db") as conn:
                        pass

                except Error as e:
                    mensaje=QMessageBox()
                    mensaje.setIcon(QMessageBox.Information)
                    mensaje.setText('Trate con otro nombre')
                    mensaje.setWindowTitle("MENSAJE")
                    mensaje.exec_()

            else:
                mensaje=QMessageBox()
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setText('Ingrese el nombre de la Base de Datos')
                mensaje.setWindowTitle("MENSAJE")
                mensaje.exec_()
        else:
            self.ui.resultado.setText("Ya existe ese nombre intente con otro")

         

        

    def atras(self):
        self.parent().show()
        self.close()


class Ventana2(QMainWindow):
    def __init__(self,parent=None):
        super(Ventana2,self).__init__(parent)
        self.ui=Ui_VentanaP2()
        self.ui.setupUi(self)
        global nombre
        self.ui.titulo.setText("Base de Datos:"+nombre)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.enter.clicked.connect(self.ir)


    def ir(self):
        seleccion=self.ui.opciones.itemText(self.ui.opciones.currentIndex())
        if seleccion=="CREAR TABLAS":
            self.hide()
            otraventana=VentanaCreacionTablas(self)
            otraventana.show()

        elif seleccion=="VER TABLAS":
            self.hide()
            otraventana=VentanaVT(self)
            otraventana.show()

        elif seleccion=="ELIMINAR TABLAS":
            self.hide()
            otraventana=VentanaBorrarTablas(self)
            otraventana.show()

        elif seleccion=="ALTA":
            self.hide()
            otraventana=VentanaVInsertar(self)
            otraventana.show()

        elif seleccion=="BAJA":
            self.hide()
            otraventana=VentanaVBorrarRegistros(self)
            otraventana.show()

        elif seleccion=="CAMBIO":
            self.hide()
            otraventana=VentanaVcambiar(self)
            otraventana.show()

        elif seleccion=="SELECCIONAR":
            self.hide()
            otraventana=VentanaVseleccionar(self)
            otraventana.show()

        elif seleccion=="TXT":
            self.hide()
            otraventana=VentanaVTxt(self)
            otraventana.show()

        elif seleccion=="CSV":
            self.hide()
            otraventana=VentanaVCsv(self)
            otraventana.show()

    def atras(self):
        self.parent().show()
        self.close()

class VentanaVCsv(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVCsv,self).__init__(parent)
        self.ui=Ui_VentanaValidacionCSV()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)
        
       
        global nombre
        contador4=0
        global listavalores
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador4+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

    	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)

    def ir(self):
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=VentanaCSV(self) #AQUI VA LA VENTA CSV
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")


    def atras(self):
        self.parent().show()
        self.close()


class VentanaCSV(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaCSV,self).__init__(parent)
        self.ui=Ui_VentanaHacerCsv()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.elegir.clicked.connect(self.elegir)
        self.ui.hacertcsv.clicked.connect(self.CSV)
        self.ui.datoabuscar.setDisabled(True)
        self.ui.hacertcsv.setDisabled(True)
        self.ui.mensaje.setText("")
        self.ui.nombrecampo.setText("")
        

        global nombre
        global nombretabla
        global listaDescripcion2
        global seleccionCSV
        global diccionariocsv
        seleccionCSV=""
        diccionariocsv={}


        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
       

        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion2.append(x)

                for campo in listaDescripcion2:
                    self.ui.combocampos.addItem(str(campo))

                self.ui.combocampos.addItem("Todos")

        except Error as e :
            self.ui.mensaje.setText(e)
        
        


    def elegir(self):
        global seleccionCSV
        seleccionCSV=self.ui.combocampos.itemText(self.ui.combocampos.currentIndex())

        if len(seleccionCSV)>0:
            self.ui.mensaje.setText("")
            self.ui.datoabuscar.setEnabled(True)
            self.ui.hacertcsv.setEnabled(True)
            self.ui.nombrecampo.setText("Campo Seleccionado:"+seleccionCSV)
            

        else:
            self.ui.nombrecampo.setText("Eliga un campo")
            self.ui.mensaje.setText("Eliga una Opciones del Combobox")

        if seleccionCSV=="Todos":
            self.ui.datoabuscar.setDisabled(True)

        else:
            self.ui.datoabuscar.setEnabled(True)


    def CSV(self):
        global seleccionCSV
        global listaDescripcion2
        global nombretabla
        global diccionariocsv
        

        if seleccionCSV=="Todos":
            self.ui.datoabuscar.setDisabled(True)
            contador=0
            contador2=0
            contadorregistro=0
            lista=[]
            
            
            sql="SELECT * FROM "+nombretabla

            try:
                base=(f"CRUD/bases/{nombre}.db")
                with sqlite3.connect(base) as conn:
                    c=conn.cursor()
                    c.execute(sql)
                    registros=c.fetchall()

                
                for elemento in registros:
                    salto=len(elemento)
         
                    contador=contador+1 
                    lista.append(registros[contadorregistro])
                    contadorregistro=contadorregistro+1

                         
                if contador==0:
                    listaregistro=[]
                    contadorregistro=0
                    self.ui.mensaje.setText("No se encontro registros")

                else: 
                    listafinal=[]
                    for x in lista:
                        for y in x:
                            listafinal.append(y)
                           
                    listaFINAL=[]
                    inicio=0
                
                    for x in range(1,salto+1):
                        listaFINAL.append(list(listafinal[inicio::salto]))
                        inicio=inicio+1

                    
                    for elemento in listaFINAL:
                        diccionariocsv[listaDescripcion2[contador2]]=elemento
                        contador2=contador2+1

                    diccionarioCSV=pd.DataFrame(diccionariocsv)

                    tiempo=datetime.datetime.now()
                    TIEMPO=tiempo.strftime('_%M_%S')
                    cadena=""
                    cadena="CRUD/Reportes/Reporte_por_"+"TODOS_"+nombretabla+TIEMPO+".csv"
                    
                    diccionarioCSV.to_csv(cadena, index=None, mode="a", header=not os.path.isfile(cadena))
                  
                    
                    self.ui.mensaje.setText("El Reporte CSV esta hecho")
                    

            except Error as e:
                self.ui.mensaje.setText(e)

            

        else:
            self.ui.datoabuscar.setEnabled(True)
            contador=0
            contador2=0
            contadorregistro=0
            lista=[]
        
            sql="SELECT * FROM "+nombretabla+" WHERE "+seleccionCSV+"= :"+seleccionCSV
            dato=self.ui.datoabuscar.text()

            if len(dato)>0:
                self.ui.mensaje.setText("")

                valor={seleccionCSV:dato}
                try:
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sql,valor)
                        registros=c.fetchall()

                
                    for elemento in registros:
                        salto=len(elemento)
            
                        contador=contador+1 
                        lista.append(registros[contadorregistro])
                        contadorregistro=contadorregistro+1
                
                    if contador==0:
                        self.ui.mensaje.setText("No se encontro registros")

                    else:
                        listafinal=[]
                        for x in lista:
                            for y in x:
                                listafinal.append(y)
                            
                        listaFINAL=[]
                        inicio=0
                    
                        for x in range(1,salto+1):
                            listaFINAL.append(list(listafinal[inicio::salto]))
                            inicio=inicio+1

                        
                        for elemento in listaFINAL:
                            diccionariocsv[listaDescripcion2[contador2]]=elemento
                            contador2=contador2+1

                        diccionarioCSV=pd.DataFrame(diccionariocsv)

                        tiempo=datetime.datetime.now()
                        TIEMPO=tiempo.strftime('_%M_%S')
                        cadena=""
                        cadena="CRUD/Reportes/Reporte_por_"+seleccionCSV+"_"+dato+"_"+nombretabla+TIEMPO+".csv"
                        
                        diccionarioCSV.to_csv(cadena, index=None, mode="a", header=not os.path.isfile(cadena))
                        self.ui.mensaje.setText("El Reporte CSV esta hecho")
                        
                except Error as e:
                    self.ui.mensaje.setText(e)

            else:
                self.ui.mensaje.setText("Ingrese el valor a buscar")
                 

    def atras(self):
        self.parent().show()
        self.close()



class VentanaVTxt(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVTxt,self).__init__(parent)
        self.ui=Ui_VentanaValidacionTXT()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)
        
       
        global nombre
        contador4=0
        global listavalores
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador4+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

    	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)

    def ir(self):
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=VentanaTXT(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")


    def atras(self):
        self.parent().show()
        self.close()



class VentanaTXT(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaTXT,self).__init__(parent)
        self.ui=Ui_VentanaHacerTxt()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.elegir.clicked.connect(self.elegir)
        self.ui.hacertxt.clicked.connect(self.TXT)
        self.ui.datoabuscar.setDisabled(True)
        self.ui.hacertxt.setDisabled(True)
        self.ui.mensaje.setText("")
        self.ui.nombrecampo.setText("")
        

        global nombre
        global nombretabla
        global listaDescripcion2
        global seleccionTXT
        seleccionTXT=""


        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
       

        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion2.append(x)

                for campo in listaDescripcion2:
                    self.ui.combocampos.addItem(str(campo))

                self.ui.combocampos.addItem("Todos")

        except Error as e :
            self.ui.mensaje.setText(e)
        
        


    def elegir(self):
        global seleccionTXT
        seleccionTXT=self.ui.combocampos.itemText(self.ui.combocampos.currentIndex())

        if len(seleccionTXT)>0:
            self.ui.mensaje.setText("")
            self.ui.datoabuscar.setEnabled(True)
            self.ui.hacertxt.setEnabled(True)
            self.ui.nombrecampo.setText("Campo Seleccionado:"+seleccionTXT)
            

        else:
            self.ui.nombrecampo.setText("Eliga un campo")
            self.ui.mensaje.setText("Eliga una Opciones del Combobox")

        if seleccionTXT=="Todos":
            self.ui.datoabuscar.setDisabled(True)

        else:
            self.ui.datoabuscar.setEnabled(True)


    def TXT(self):
        global seleccionTXT
        global listaDescripcion2
        global nombretabla

        if seleccionTXT=="Todos":
            self.ui.datoabuscar.setDisabled(True)
            contador=0
            datos=[]
            datos.append(listaDescripcion2)
            sql="SELECT * FROM "+nombretabla

            try:
                base=(f"CRUD/bases/{nombre}.db")
                with sqlite3.connect(base) as conn:
                    c=conn.cursor()
                    c.execute(sql)
                    registros=c.fetchall()

            
                for elemento in registros:
                    contador=contador+1
            
                if contador==0:
                    self.ui.mensaje.setText("No se encontro registros")

                else:
                    tiempo=datetime.datetime.now()
                    TIEMPO=tiempo.strftime('Dia:%d Mes:%m Año:%Y Hora:%H Minuto:%M Segundo:%S')
                    cadena=""
                    cadena="CRUD/Reportes/Reporte_por_"+"TODOS_"+nombretabla+".txt"
                    archivoA=open(cadena ,'a',encoding="utf-8")
                    archivoA.write("\n")
                    archivoA.write("-"*20+"Buscado por : "+"Todos"+":"+" Tabla_"+nombretabla+" ( "+TIEMPO+")"+"-"*20)
                    archivoA.write("\n")
                    for conjunto in registros:
                        datos.append(conjunto)

                   
                    archivoA.write(tabulate(datos))
                    archivoA.write("\n")
                    archivoA.write("-"*100)
                    archivoA.close()
                    
                    self.ui.mensaje.setText("El Reporte TXT esta hecho")

            except Error as e:
                self.ui.mensaje.setText(e)

        else:
            self.ui.datoabuscar.setEnabled(True)
            contador=0
            datos=[]
            datos.append(listaDescripcion2)
            sql="SELECT * FROM "+nombretabla+" WHERE "+seleccionTXT+"= :"+seleccionTXT
            dato=self.ui.datoabuscar.text()

            if len(dato)>0:

                valor={seleccionTXT:dato}
                try:
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sql,valor)
                        registros=c.fetchall()

                
                    for elemento in registros:
                        contador=contador+1
                
                    if contador==0:
                        self.ui.mensaje.setText("No se encontro registros")

                    else:
                        
                        
                        tiempo=datetime.datetime.now()
                        TIEMPO=tiempo.strftime('Dia:%d Mes:%m Año:%Y Hora:%H Minuto:%M Segundo:%S')
                        cadena=""
                        cadena="CRUD/Reportes/Reporte_por_"+seleccionTXT+"_"+dato+"_"+nombretabla+".txt"
                        archivoA=open(cadena ,'a',encoding="utf-8")
                        archivoA.write("\n")
                        archivoA.write("-"*20+"Buscado por : "+seleccionTXT+":"+dato+" Tabla_"+nombretabla+" ("+TIEMPO+")"+"-"*20)
                        archivoA.write("\n")
                        for conjunto in registros:
                            datos.append(conjunto)

                    
                        archivoA.write(tabulate(datos))
                        archivoA.write("\n")
                        archivoA.write("-"*100)
                        archivoA.close()
                        
                        self.ui.mensaje.setText("El Reporte TXT esta hecho")

                except Error as e:
                    self.ui.mensaje.setText(e)

            else:
                self.ui.mensaje.setText("Ingrese el valor a buscar")

                
        

    def atras(self):
        self.parent().show()
        self.close()


class VentanaInfoo(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaInfoo,self).__init__(parent)
        self.ui=Ui_Ventanainformacion()
        self.ui.setupUi(self)
        self.ui.GIT.clicked.connect(self.irgit)
        self.ui.FACE.clicked.connect(self.irface)
        self.ui.regresar.clicked.connect(self.atras)

    def irgit(self):
        url="https://github.com/DanielRojas2002"
        webbrowser.open_new(url)

    def irface(self):
        url="https://www.facebook.com/profile.php?id=100008378837298"
        webbrowser.open_new(url)

    def atras(self):
        self.parent().show()
        self.close()
        
        


class VentanaCreacionTablas(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaCreacionTablas,self).__init__(parent)
        self.ui=Ui_CreacionTablas()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.poner_lista.clicked.connect(self.lista)
        self.ui.quitar_lista.clicked.connect(self.quitarlista)
        self.ui.borrar.clicked.connect(self.borrar)
        self.ui.crear.clicked.connect(self.crear)
        global contador2
        global nombre
        self.ui.nombre.setText("Nombre del Campo "+str(contador2)+" :")
        self.ui.exito.setText("")
        self.ui.tablascreadas.clear()

        contador5=0
        sql="SELECT name FROM sqlite_master WHERE type='table';"
        contadortablas=0

        base=(f"CRUD/bases/{nombre}.db")
        with sqlite3.connect(base) as conn:
            c = conn.cursor()
            c.execute(sql)
            tablas=c.fetchall()
            
            for t in tablas:
                for x in t:
                    contador5=contador5+1
                    contadortablas=contadortablas+1
                    if contador5==1:
                        self.ui.tablascreadas.addItem("Tablas Actualmente ya creadas(No repita los nombres)")
                    self.ui.tablascreadas.addItem("Tabla "+str(contadortablas)+" :"+x)

            if contador5==0:
                self.ui.tablascreadas.addItem("Actualmente no existen tablas :(")


    def lista(self):
        global contador2

        if len(self.ui.nombredato.text())>0:
            self.ui.error2.setText("")
            self.ui.error4.setText("")
            contador2=contador2+1
            self.ui.nombre.setText("Nombre del Campo "+str(contador2)+" :")
            
            seleccion=self.ui.tipo.itemText(self.ui.tipo.currentIndex())
            lista=self.ui.nombredato.text()+" "+seleccion
            lista2=self.ui.nombredato.text()+" "+seleccion
            self.ui.valores.addItem(lista)
            global listaquery
            listaquery.append(lista2)
            self.ui.nombredato.setText("")
            self.ui.exito.setText("")
            

        else:
            self.ui.error2.setText("Ingresa el nombre del Campo")
            self.ui.exito.setText("")


    def quitarlista(self):
        global listadatos
        global listaquery
        global contador
        global contador2

        if contador2>0:
            contador2=contador2-1
            contador=contador-1

        else:
            contador=0
            contador2=1

        if contador2>0:
            self.ui.nombre.setText("Nombre del Campo "+str(contador2)+" :")

        listadatos=listaquery
        
        try:
            listadatos.pop()

        except:
            self.ui.error4.setText("No Hay valores en la Lista")

        for elemento in listadatos:
            self.ui.valores.addItem(elemento)
            
        listaquery=listadatos
        
        self.ui.exito.setText("")
        
    def crear(self):
        self.ui.exito.setText("")
        global listaquery
        global contador
        global contador2
        global nombre
        

        for elemento in listaquery:
            contador=contador+1
        
        if contador>=1:
            self.ui.error3.setText("")
        else:
            self.ui.error3.setText("Al menos tiene que agregar un Campo")

        if len(self.ui.nombretabla.text())>0:
            self.ui.error1.setText("")
        else:
            self.ui.error1.setText("Ingresa el nombre de la tabla")


        if len(self.ui.nombretabla.text())>0 and contador>=1:
            listaQUERY=[]
            contador3=1
            verificacion=0
            sql=""
            paso1="CREATE TABLE IF NOT EXISTS "
            parentesisizq="( "
            parentesisder=")"

            for elemento in listaquery:
                verificacion=verificacion+1


            for elemento in listaquery:
                if verificacion>contador3:
                    listaQUERY.append(elemento+",")
                    contador3=contador3+1
                    
                else:
                    listaQUERY.append(elemento)

           

            for elemento in listaQUERY:
                sql=sql+elemento

            
            try:
                base=(f"CRUD/bases/{nombre}.db")
                with sqlite3.connect(base) as conn:
                    t=self.ui.nombretabla.text()
                    tabla=t
                    c = conn.cursor()

                    query=paso1+tabla+parentesisizq+sql+parentesisder+";"
                    c.execute(query)
                    contador2=1

                    self.ui.exito.setText("TABLA CREADA Regresar(<-)")
                    self.ui.valores.clear()
                    self.ui.nombre.setText("Nombre del Campo "+str(contador2)+" :")
                    self.ui.nombretabla.setText("")
                    listaquery=[]
                    contador=0
                    
            except Error as e:
                self.ui.exito.setText("Ingreso mal un dato")

        contador5=0

        sql="SELECT name FROM sqlite_master WHERE type='table';"
        contadortablas=0
        self.ui.tablascreadas.clear()
        base=(f"CRUD/bases/{nombre}.db")
        with sqlite3.connect(base) as conn:
            c = conn.cursor()
            c.execute(sql)
            tablas=c.fetchall()
            
            for t in tablas:
                for x in t:
                    contador5=contador5+1
                    contadortablas=contadortablas+1
                    if contador5==1:
                        self.ui.tablascreadas.addItem("Tablas Actualmente ya creadas(No repita los nombres)")
                    self.ui.tablascreadas.addItem("Tabla "+str(contadortablas)+" :"+x)
                    

            if contador5==0:
                self.ui.tablascreadas.addItem("Actualmente no existen tablas :(")
            
                            
            

                
    def borrar(self):
        global listaquery 
        global contador
        global contador2
        contador2=1
        listaquery=[]
        contador=0
        self.ui.nombre.setText("Nombre del Campo "+str(contador2)+" :")
        self.ui.exito.setText("")
    
    def atras(self):
        global listaquery 
        global contador
        global contador2
        listaquery=[]
        contador=0
        contador2=1
        self.ui.exito.setText("")
        self.parent().show()
        self.close()
        

class VentanaVT(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVT,self).__init__(parent)
        self.ui=Ui_VentanaVisualizadoraTablas()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        sql="SELECT name FROM sqlite_master WHERE type='table';"
        global nombre
        contador5=0
        contadortabla=1

        base=(f"CRUD/bases/{nombre}.db")
        with sqlite3.connect(base) as conn:
            c = conn.cursor()
            c.execute(sql)
            tablas=c.fetchall()
            
            for t in tablas:
                for x in t:
                    contador5=contador5+1
                    self.ui.nombrestablas.addItem("El nombre de la Tabla "+str(contadortabla)+" es : "+x)
                    contadortabla=contadortabla+1

            if contador5==0:
                self.ui.nombrestablas.addItem("No existen Tablas tiene que crear tablas")

            self.ui.numerotablas.setText("Numero de Tablas encontradas:"+str(contador5))




    def atras(self):
        self.parent().show()
        self.close()


class VentanaBorrarTablas(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaBorrarTablas,self).__init__(parent)
        self.ui=Ui_VentanaBTablas()
        self.ui.setupUi(self) 
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.borrar.clicked.connect(self.borrar)
        self.ui.tablascreadas.itemClicked.connect(self.paso1)
        global nombre
        contador4=0
        global listatablas

        sql="SELECT name FROM sqlite_master WHERE type='table';"
        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador4+1
                        self.ui.tablascreadas.addItem(x)
                        listatablas.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

    def paso1(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.tablaaborrar.setText(dato)


    def borrar(self):
        global nombre
        global listatablas
        contador4=0
        self.ui.tablascreadas.clear()
        tabla=self.ui.tablaaborrar.text()
        try:
            listatablas.remove(tabla)
        except:
            self.ui.mensaje.setText("NO EXISTE ESA TABLA")


        for x in listatablas:
            contador4=contador4+1
            self.ui.tablascreadas.addItem(x)

        if contador4==0:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")
        try:
            base=(f"CRUD/bases/{nombre}.db")
            tabla=self.ui.tablaaborrar.text()
            sql='DROP TABLE %s' % tabla
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                
                self.ui.mensaje.setText("SE BORRO LA TABLA SATISFACTORIAMENTE")
        except:
            self.ui.mensaje.setText("NO EXISTE ESA TABLA")



    def atras(self):
        self.parent().show()
        self.close()


class VentanaVInsertar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVInsertar,self).__init__(parent)
        self.ui=Ui_VentanaValidacionInsertar()
        self.ui.setupUi(self)
        global nombre
        contador4=0
        global listavalores
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador4+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)
	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)

    def ir(self):
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=VentanaInsertar(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")
        


    def atras(self):
        self.parent().show()
        self.close()


class VentanaVborrar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVborrar,self).__init__(parent)
        self.ui=Ui_VentanaValidacionborrar()
        self.ui.setupUi(self)
        global nombre
        contador4=0
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)


    def ir(self):
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=VentanaInsertar(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")
	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)

    
    def atras(self):
        self.parent().show()
        self.close()


class VentanaVcambiar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVcambiar,self).__init__(parent)
        self.ui=Ui_VentanaValidacioncambiar()
        self.ui.setupUi(self)
        global nombre
        contador4=0
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)
	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)

    def ir(self):
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=VentanaCambiarRegistroP1(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")


    def atras(self):
        self.parent().show()
        self.close()

class VentanaCambiarRegistroP1(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaCambiarRegistroP1,self).__init__(parent)
        self.ui=Ui_VentanacambiarRegistro()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)

        self.ui.listaid.itemClicked.connect(self.mostrar)
        self.ui.irmodificar.clicked.connect(self.irmodificar1)
        self.ui.Actualizar.clicked.connect(self.Actualizar)
        self.ui.mensaje.setText("")

        global nombre
        global nombretabla
        global primarykey
        global listaPrimarykey2

        global verdad

     

        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
        listaDescripcion3=[]
        primarykey=""
        listaPrimarykey=[]
        listaPrimarykey2=[]
        
        
        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion3.append(x)

                primarykey=listaDescripcion3[0]

        except Error as e:
            self.ui.mensaje.setText(e)

        try:
            sql="SELECT "+primarykey+" FROM "
            sql=sql+nombretabla+";"

            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for dato in tablas:
                    for x in dato:
                        listaPrimarykey.append(x)

                for elemento in listaPrimarykey:
                    x=self.ui.listaid.addItem(primarykey+": "+str(elemento))
                    listaPrimarykey2.append(x)

        except Error as e:
            self.ui.mensaje.setText(e)
            

        sql2="SELECT * FROM "
        sql2=sql2+nombretabla+";"
        contador=0
        lista=[]

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql2)
                tablas=c.fetchall()

                for t in tablas:
                    contador=contador+1
                    lista.append(t)

            
            columnas=len(lista[0])
            

            filas=contador
            self.ui.tableWidget.setRowCount(filas)
            self.ui.tableWidget.setColumnCount(columnas)

            fila=0
            for registro in lista:
                columna=0
                for elemento in registro:
                    celda=QTableWidgetItem(str(elemento))
                    self.ui.tableWidget.setItem(fila,columna,celda)
                    columna=columna+1
                fila=fila+1

            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion3)
    
            

        except Error as e:
            self.ui.mensaje.setText(e)

        except:
            self.ui.mensaje.setText("No Existen Registros aun")

    def mostrar(self):
        global Datoamodificar
        Datoamodificar=self.ui.listaid.currentItem().text()
        self.ui.datoamodificar.setText(Datoamodificar)

    def irmodificar1(self):
        global Datoamodificar
        global valorModificar
        valorModificar=""
        self.ui.mensaje.setText("")
        try:
            datorenglon=self.ui.datoamodificar.text()
            if len(datorenglon)>0:
                    DatoAModificar=self.ui.datoamodificar.text()
                    valorModificar=DatoAModificar.split(":")
                    self.ui.mensaje.setText("")
                    self.hide()
                    otraventana=VentanaMODIFICAR(self)
                    otraventana.show()

            else:
                self.ui.mensaje.setText("Seleccione el Dato a Modificar")

        except:
            self.ui.mensaje.setText("e")


    def Actualizar(self):
        self.ui.tableWidget.clear()
        self.ui.listaid.clear()
        self.ui.mensaje.setText("")
        self.ui.datoamodificar.setText("")

        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
        listaDescripcion3=[]
        primarykey=""
        listaPrimarykey=[]
        listaPrimarykey2=[]
        
        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion3.append(x)

                primarykey=listaDescripcion3[0]

        except Error as e:
            self.ui.mensaje.setText(e)

        try:
            sql="SELECT "+primarykey+" FROM "
            sql=sql+nombretabla+";"

            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for dato in tablas:
                    for x in dato:
                        listaPrimarykey.append(x)

                for elemento in listaPrimarykey:
                    x=self.ui.listaid.addItem(primarykey+": "+str(elemento))
                    listaPrimarykey2.append(x)

        except Error as e:
            self.ui.mensaje.setText(e)
            

        sql2="SELECT * FROM "
        sql2=sql2+nombretabla+";"
        contador=0
        lista=[]

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql2)
                tablas=c.fetchall()

                for t in tablas:
                    contador=contador+1
                    lista.append(t)

            
            columnas=len(lista[0])
            

            filas=contador
            self.ui.tableWidget.setRowCount(filas)
            self.ui.tableWidget.setColumnCount(columnas)

            fila=0
            for registro in lista:
                columna=0
                for elemento in registro:
                    celda=QTableWidgetItem(str(elemento))
                    self.ui.tableWidget.setItem(fila,columna,celda)
                    columna=columna+1
                fila=fila+1

            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion3)
           
            

        except Error as e:
            self.ui.mensaje.setText(e)

        except:
            self.ui.mensaje.setText("No Existen Registros aun")


    def atras(self):
        self.parent().show()
        self.close()

class VentanaMODIFICAR(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaMODIFICAR,self).__init__(parent)
        self.ui=Ui_VentanaModificarRegistros()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.guardar.clicked.connect(self.derecha)
        self.ui.Campos.itemClicked.connect(self.seleccioncampo)
        self.ui.insertar.clicked.connect(self.insertar)
    
        global valorModificar
        global nombre
        global nombretabla       
        global primarykey
        global listaPrimarykey2
        global contadorverificacion2
        global contadorvalidacion2
        global listavalores2
        global listacampos

        listacampos=[]
        listavalores2=[]

        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
        listaDescripcion3=[]
        primarykey=""
        listaPrimarykey=[]
        listaPrimarykey2=[]
        contadorverificacion2=0
        contadorvalidacion2=0
        
        
        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion3.append(x)
                        
                        
                primarykey=listaDescripcion3[0]

        except Error as e:
            self.ui.mensaje.setText(e)

        try:
            for campo in listaDescripcion3[1::]:
                self.ui.Campos.addItem(str(campo))
                contadorverificacion2=contadorverificacion2+1

        except:
            self.ui.mensaje.setText("AQUI")

        
        valor={valorModificar[0]:valorModificar[1]}
        sql="SELECT * FROM "
        sql=sql+nombretabla+" WHERE "+valorModificar[0]+"= :"+valorModificar[0]

        
        contador=0
        lista=[]

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql,valor)
                tablas=c.fetchall()

                for t in tablas:
                    contador=contador+1
                    lista.append(t)

            
            columnas=len(lista[0])
            

            filas=contador
            self.ui.tableWidget.setRowCount(filas)
            self.ui.tableWidget.setColumnCount(columnas)

            fila=0
            for registro in lista:
                columna=0
                for elemento in registro:
                    celda=QTableWidgetItem(str(elemento))
                    self.ui.tableWidget.setItem(fila,columna,celda)
                    columna=columna+1
                fila=fila+1

            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion3)
    
            

        except Error as e:
            self.ui.mensaje.setText(e)

        except:
            self.ui.mensaje.setText("No Existen Registros aun")


    def seleccioncampo(self):
        global dato
        dato=""
        dato=self.ui.Campos.currentItem().text()
        self.ui.campo.setText(dato)

    def derecha(self):
        global dato
        global listacampos
        global contadorvalidacion2
        global listavalores2
        
        
        if len(self.ui.campo.text())>0 and len(self.ui.valor.text())>0:
            campo=self.ui.campo.text()
            valor=self.ui.valor.text()
            listavalores2.append(valor)
            listacampos.append(campo)

            
            contadorvalidacion2=contadorvalidacion2+1
            
            
            self.ui.error.setText("")
            self.ui.campo.setText("")
            self.ui.Campos.takeItem(self.ui.Campos.currentRow())
            self.ui.valorcampo.addItem(campo+": "+valor)
            self.ui.valor.clear()
            
        else:
            self.ui.error.setText("Seleccione el campo y/o el valor")

    def insertar(self):
        global nombre
        global nombretabla
        global listacampos
        global listavalores2
        global valorModificar
        global campos
        
        global contadorverificacion2
        global contadorvalidacion2  
        global sqlinsertar

        campos=""
        sqlinsertar=""
        listavaloresregulados=[]
        
        
        try:
            if contadorverificacion2==contadorvalidacion2:

                for x in listacampos:
                    listavaloresregulados.append(x+" = ? , ")
                    

                listavaloresregulados.pop()

                longitud=len(listavaloresregulados)

                ultimovalor=listacampos[longitud]

                listavaloresregulados.append(ultimovalor+" = ? ")

                for campo in listavaloresregulados:
                    campos=campos+campo

                
                sqlinsertar="UPDATE "+nombretabla+" SET "+campos+" WHERE "+primarykey+" = ? ;"
                listavalores2.append(valorModificar[1])
                tuplavalores=tuple(listavalores2)
            
                try:
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sqlinsertar,tuplavalores)
                        self.ui.exito.setText("Se Aplico La Modificacion (Regresar <--)")
                        self.ui.tableWidget.clear()


                        
                        

                except Error as e:
                    self.ui.error.setText(e)
                    self.ui.exito.setText("No se Pudo Aplicar las Modificaciones")
                

            else:
                self.ui.error.setText("Faltan Campos Tiene que agregar todos los\nCampos")


        except:
            self.ui.error.setText("ERROR")
            
       
    
    def atras(self):

        global listacampos
        listacampos=[]
        global listavalores2
        global valorModificar
        global campos
        
        global contadorverificacion2
        global contadorvalidacion2  
        global sqlinsertar
        
        contadorverificacion2=0
        contadorvalidacion2=0
        listavalores2=[]
        valorModificar=[]
        
        sqlinsertar=""
        campos=""

        self.ui.Campos.clear()
        self.ui.exito.setText("")

        self.parent().show()
        self.close()


class VentanaVBorrarRegistros(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVBorrarRegistros,self).__init__(parent)
        self.ui=Ui_VentanaValidacionBorrarRegistros()
        self.ui.setupUi(self)
        self.ui.error1.setText("")

        global nombre
        

        contador4=0
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)
	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)


    def ir(self):
        self.ui.error1.setText("")
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=ventanaborrarregistro(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")

   
    def atras(self):
        self.parent().show()
        self.close()

        
class ventanaborrarregistro(QMainWindow):
    def __init__(self,parent=None):
        super(ventanaborrarregistro,self).__init__(parent)
        self.ui=Ui_VentanaBorrarRegistro()
        self.ui.setupUi(self)
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.listaid.itemClicked.connect(self.mostrar)
        self.ui.BORRAR.clicked.connect(self.borrar)
        self.ui.Actualizar.clicked.connect(self.Actualizar)
        self.ui.mensaje.setText("")

        global nombre
        global nombretabla
        global primarykey
        global listaPrimarykey2

        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
        listaDescripcion3=[]
        primarykey=""
        listaPrimarykey=[]
        listaPrimarykey2=[]
        
        
        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion3.append(x)

                primarykey=listaDescripcion3[0]

        except Error as e:
            self.ui.mensaje.setText(e)

        try:
            sql="SELECT "+primarykey+" FROM "
            sql=sql+nombretabla+";"

            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for dato in tablas:
                    for x in dato:
                        listaPrimarykey.append(x)

                for elemento in listaPrimarykey:
                    x=self.ui.listaid.addItem(primarykey+": "+str(elemento))
                    listaPrimarykey2.append(x)

        except Error as e:
            self.ui.mensaje.setText(e)
            

        sql2="SELECT * FROM "
        sql2=sql2+nombretabla+";"
        contador=0
        lista=[]

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql2)
                tablas=c.fetchall()

                for t in tablas:
                    contador=contador+1
                    lista.append(t)

            
            columnas=len(lista[0])
            

            filas=contador
            self.ui.tableWidget.setRowCount(filas)
            self.ui.tableWidget.setColumnCount(columnas)

            fila=0
            for registro in lista:
                columna=0
                for elemento in registro:
                    celda=QTableWidgetItem(str(elemento))
                    self.ui.tableWidget.setItem(fila,columna,celda)
                    columna=columna+1
                fila=fila+1

            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion3)
    
            

        except Error as e:
            self.ui.mensaje.setText(e)

        except:
            self.ui.mensaje.setText("No Existen Registros aun")

    def mostrar(self):
        global Datoaborrar
        Datoaborrar=self.ui.listaid.currentItem().text()
        self.ui.datoaborrar.setText(Datoaborrar)

    def Actualizar(self):
        self.ui.tableWidget.clear()
        self.ui.listaid.clear()
        self.ui.mensaje.setText("")
        self.ui.datoaborrar.setText("")

        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
        listaDescripcion3=[]
        primarykey=""
        listaPrimarykey=[]
        listaPrimarykey2=[]
        
        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion3.append(x)

                primarykey=listaDescripcion3[0]

        except Error as e:
            self.ui.mensaje.setText(e)

        try:
            sql="SELECT "+primarykey+" FROM "
            sql=sql+nombretabla+";"

            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for dato in tablas:
                    for x in dato:
                        listaPrimarykey.append(x)

                for elemento in listaPrimarykey:
                    x=self.ui.listaid.addItem(primarykey+": "+str(elemento))
                    listaPrimarykey2.append(x)

        except Error as e:
            self.ui.mensaje.setText(e)
            

        sql2="SELECT * FROM "
        sql2=sql2+nombretabla+";"
        contador=0
        lista=[]

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql2)
                tablas=c.fetchall()

                for t in tablas:
                    contador=contador+1
                    lista.append(t)

            
            columnas=len(lista[0])
            

            filas=contador
            self.ui.tableWidget.setRowCount(filas)
            self.ui.tableWidget.setColumnCount(columnas)

            fila=0
            for registro in lista:
                columna=0
                for elemento in registro:
                    celda=QTableWidgetItem(str(elemento))
                    self.ui.tableWidget.setItem(fila,columna,celda)
                    columna=columna+1
                fila=fila+1

            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion3)
           
            

        except Error as e:
            self.ui.mensaje.setText(e)

        except:
            self.ui.mensaje.setText("No Existen Registros aun")
        

    def borrar(self):
        global Datoaborrar
        global primarykey
        try:

        
            if len(Datoaborrar)>0:
                DatoABorrar=self.ui.datoaborrar.text()
                valor=DatoABorrar.split(":")
                
                self.ui.mensaje.setText("")
                base=(f"CRUD/bases/{nombre}.db")
                
                sql="DELETE  FROM "+nombretabla+" WHERE "+primarykey+" = :"+primarykey
                valor={primarykey:valor[1]}
                

                try:
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sql,valor)
                        conn.commit()
                        self.ui.mensaje.setText("El Registro se Borro")

                except Error as e:
                    self.ui.mensaje.setText(e)

            else:
                self.ui.mensaje.setText("Seleccione el Dato a Borrar")
        except:
            self.ui.mensaje.setText("")
            

    def atras(self):
        global Datoaborrar
        Datoaborrar=""
        self.parent().show()
        self.close()


class VentanaVseleccionar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaVseleccionar,self).__init__(parent)
        self.ui=Ui_VentanaValidacionseleccionar()
        self.ui.setupUi(self)
        global nombre
        contador4=0
        sql="SELECT name FROM sqlite_master WHERE type='table';"

        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

                for t in tablas:
                    for x in t:
                        contador4=contador+1
                        self.ui.tablascreadas.addItem(x)
                        listavalores.append(x)

                if contador4==0:
                    self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        except:
            self.ui.tablascreadas.addItem("No existen Tablas tiene que crear tablas")

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.tablascreadas.itemClicked.connect(self.agregar)
        self.ui.enviar.clicked.connect(self.ir)
	
    def agregar(self):
        dato=self.ui.tablascreadas.currentItem().text()
        self.ui.nombretabla.setText(dato)


    def ir(self):
        global listavalores
        global nombretabla
        validacion=0
        for x in listavalores:
            if self.ui.nombretabla.text()==x:
                validacion=validacion+1
                nombretabla=self.ui.nombretabla.text()
        
        if validacion>0:
            self.hide()
            otraventana=VentanaSelecciona(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")

   
    def atras(self):
        self.parent().show()
        self.close()

class VentanaSelecciona(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaSelecciona,self).__init__(parent)
        self.ui=Ui_VentanaSeleccionar()
        self.ui.setupUi(self)

        self.ui.atras.clicked.connect(self.atras)
        self.ui.realizar.clicked.connect(self.realizar)
        self.ui.seleccionar.clicked.connect(self.seleccionar)
        

        global listaDescripcion2
        global nombre
        global nombretabla

        sql="PRAGMA table_info("
        sql=sql+nombretabla+")"
       

        try:
            listaDescripcion2=[]
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                c.execute(sql)
                tablas=c.fetchall()

        
                for a in tablas:
                    for x in a[1:2]:
                        listaDescripcion2.append(x)

        except Error as e :
            self.ui.titulo2.setText(e)

    def seleccionar(self):
        global seleccion
        global listaDescripcion2
        
        self.ui.titulo2.setText("")
        self.ui.dato.setText("")
        selecciones=self.ui.opciones.itemText(self.ui.opciones.currentIndex())

        if selecciones=="TODOS":
            seleccion="TODOS"
            self.ui.dato.setDisabled(True)
            self.ui.opciones_2.setDisabled(True)
            

        elif selecciones=="Especifico":
            seleccion="Especifico"
            self.ui.dato.setEnabled(True)
            self.ui.opciones_2.setEnabled(True)
            self.ui.opciones_2.clear()
        
            for elemento in listaDescripcion2:
                self.ui.opciones_2.addItem(elemento)

        elif selecciones=="Empiece con...":
            seleccion="Empiece con..."
            self.ui.dato.setEnabled(True)
            self.ui.opciones_2.setEnabled(True)
            self.ui.opciones_2.clear()

            for elemento in listaDescripcion2:
                self.ui.opciones_2.addItem(elemento)

        elif selecciones=="Termine con...":
            seleccion="Termine con..."
            self.ui.dato.setEnabled(True)
            self.ui.opciones_2.setEnabled(True)
            self.ui.opciones_2.clear()

            for elemento in listaDescripcion2:
                self.ui.opciones_2.addItem(elemento)


    def realizar(self):
        global nombre
        global nombretabla
        global seleccion
        global listaDescripcion2
        contador=0
        lista=[]
        
        

        sql2="SELECT * FROM "
        sql2=sql2+nombretabla+";" 

        if seleccion=="TODOS":
            try:
                base=(f"CRUD/bases/{nombre}.db")
                with sqlite3.connect(base) as conn:
                    c=conn.cursor()
                    c.execute(sql2)
                    tablas=c.fetchall()

                    for t in tablas:
                        contador=contador+1
                        lista.append(t)

                
                columnas=len(lista[0])
                

                filas=contador
                self.ui.tableWidget.setRowCount(filas)
                self.ui.tableWidget.setColumnCount(columnas)

                fila=0
                for registro in lista:
                    columna=0
                    for elemento in registro:
                        celda=QTableWidgetItem(str(elemento))
                        self.ui.tableWidget.setItem(fila,columna,celda)
                        columna=columna+1
                    fila=fila+1

                self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion2)
               
                self.ui.titulo2.setText("")

            except Error as e:
                self.ui.titulo2.setText(e)

            except:
                self.ui.titulo2.setText("No se Encontraron registros")

        elif seleccion=="Especifico":
            self.ui.tableWidget.clear()
            contador=0
            lista2=[]
            
            
            if len(self.ui.dato.text())>0:
                dato=self.ui.dato.text()
            
                try:
                    selecciones=self.ui.opciones_2.itemText(self.ui.opciones_2.currentIndex())
                    valor={selecciones:dato}
                    sql="SELECT * FROM "
                    sql=sql+nombretabla+" WHERE "+selecciones+"= :"+selecciones
                    
                    
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sql,valor)
                        registros=c.fetchall()

                
                        for elemento in registros:
                            lista2.append(elemento)
                            contador=contador+1
                    
                        if contador==0:
                            self.ui.titulo2.setText("No se Encontraron registros")

                        if contador>=1:
                            columnas=len(listaDescripcion2)
                    

                            filas=contador
                            self.ui.tableWidget.setRowCount(filas)
                            self.ui.tableWidget.setColumnCount(columnas)

                            fila=0
                            for registro in lista2:
                                columna=0
                                for elemento in registro:
                                    celda=QTableWidgetItem(str(elemento))
                                    self.ui.tableWidget.setItem(fila,columna,celda)
                                    columna=columna+1
                                fila=fila+1

                            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion2)
                            
                            self.ui.titulo2.setText("")

                except Error as e:
                    self.ui.titulo2.setText(e)

                except:
                    self.ui.titulo2.setText("Ingrese el dato a buscar")
            else:
                self.ui.titulo2.setText("Ingrese el dato a buscar")


        elif seleccion=="Empiece con...":
            self.ui.tableWidget.clear()
            contador=0
            lista2=[]
            
            
            if len(self.ui.dato.text())>0:
                dato=self.ui.dato.text()
                datobuscar=str(dato)
            
                try:
                    selecciones=self.ui.opciones_2.itemText(self.ui.opciones_2.currentIndex())
                    sql="SELECT * FROM "
                    sql=sql+nombretabla+" WHERE "+selecciones+" LIKE "+"'%s%%'"
                    
                    
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sql%datobuscar)
                        registros=c.fetchall()

                
                        for elemento in registros:
                            lista2.append(elemento)
                            contador=contador+1
                    
                        if contador==0:
                            self.ui.titulo2.setText("No se Encontraron registros")

                        if contador>=1:
                            columnas=len(listaDescripcion2)
                    

                            filas=contador
                            self.ui.tableWidget.setRowCount(filas)
                            self.ui.tableWidget.setColumnCount(columnas)

                            fila=0
                            for registro in lista2:
                                columna=0
                                for elemento in registro:
                                    celda=QTableWidgetItem(str(elemento))
                                    self.ui.tableWidget.setItem(fila,columna,celda)
                                    columna=columna+1
                                fila=fila+1

                            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion2)
                            
                            self.ui.titulo2.setText("")

                except Error as e:
                    self.ui.titulo2.setText(e)

                except:
                    self.ui.titulo2.setText("Ingrese el dato a buscar")
            else:
                self.ui.titulo2.setText("Ingrese el dato a buscar")

            
        elif seleccion=="Termine con...":
            self.ui.tableWidget.clear()
            contador=0
            lista2=[]
            
            
            if len(self.ui.dato.text())>0:
                dato=self.ui.dato.text()
                datobuscar=str(dato)
            
                try:
                    selecciones=self.ui.opciones_2.itemText(self.ui.opciones_2.currentIndex())
                    sql="SELECT * FROM "
                    sql=sql+nombretabla+" WHERE "+selecciones+" LIKE "+"'%%%s'"
                    
                    
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sql%datobuscar)
                        registros=c.fetchall()

                
                        for elemento in registros:
                            lista2.append(elemento)
                            contador=contador+1
                    
                        if contador==0:
                            self.ui.titulo2.setText("No se Encontraron registros")

                        if contador>=1:
                            columnas=len(listaDescripcion2)
                    

                            filas=contador
                            self.ui.tableWidget.setRowCount(filas)
                            self.ui.tableWidget.setColumnCount(columnas)

                            fila=0
                            for registro in lista2:
                                columna=0
                                for elemento in registro:
                                    celda=QTableWidgetItem(str(elemento))
                                    self.ui.tableWidget.setItem(fila,columna,celda)
                                    columna=columna+1
                                fila=fila+1

                            self.ui.tableWidget.setHorizontalHeaderLabels(listaDescripcion2)
                            
                            self.ui.titulo2.setText("")

                except Error as e:
                    self.ui.titulo2.setText(e)

                except:
                    self.ui.titulo2.setText("Ingrese el dato a buscar")
            else:
                self.ui.titulo2.setText("Ingrese el dato a buscar")


    def atras(self):
        self.parent().show()
        self.close()


class VentanaInsertar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaInsertar,self).__init__(parent)
        self.ui=Ui_VentanaInsertarRegistros()
        self.ui.setupUi(self)
        global nombre 
        global nombretabla
        global listavalor
        global contadorverificacion
        
       
        dato=""
        self.ui.regresar.clicked.connect(self.atras)
        self.ui.guardar.clicked.connect(self.derecha)
        self.ui.Campos.itemClicked.connect(self.seleccioncampo)
        self.ui.borrartodo.clicked.connect(self.restablecer)
        self.ui.insertar.clicked.connect(self.insertar)
        self.ui.nombretabla.setText("Tabla: "+nombretabla)

    
	
        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                paso1="PRAGMA table_info("
                sql=paso1+nombretabla+")"
                c.execute(sql)
                descripcion=c.fetchall()

                for a in descripcion:
                    for x in a[1:2]:
                        listavalor.append(x)
                        
                for campo in listavalor:
                    self.ui.Campos.addItem(campo)
                    contadorverificacion=contadorverificacion+1
                    
                
        except Error as e:
            sle.ui.error.setText(e)

        
    def seleccioncampo(self):
        global dato
        dato=self.ui.Campos.currentItem().text()
        self.ui.campo.setText(dato)
    
        

    def derecha(self):
        global dato
        global listacampos
        global contadorvalidacion
        global listaValoresInsertar
        global diccInsertar
        
        if len(self.ui.campo.text())>0 and len(self.ui.valor.text())>0:
            campo=self.ui.campo.text()
            valor=self.ui.valor.text()
            diccInsertar[campo]=valor
            listaValoresInsertar.append(valor)
            listaquery.append(":"+campo+",")
            listacampos.append(campo)
            contadorvalidacion=contadorvalidacion+1
            
            
            self.ui.error.setText("")
            self.ui.campo.setText("")
            self.ui.Campos.takeItem(self.ui.Campos.currentRow())
            self.ui.valorcampo.addItem(campo+": "+valor)
            self.ui.valor.clear()
            
        else:
            self.ui.error.setText("Seleccione el campo y/o el valor")


    def insertar(self):
        global contadorRegistros
        global nombre
        global nombretabla
        global listaquery
        global listacampos
        global listaValoresInsertar
        global diccInsertar
        global contadorverificacion
        global contadorvalidacion
        global ultima
        global sqlinsertar
        
        sqlinsertar="INSERT INTO "+nombretabla+" VALUES("
       
        
        try:
            if contadorverificacion==contadorvalidacion:
                
                for x in listaquery[-1:]:
                    listaquery.pop()
                    for letra in x[:-1]:
                        ultima=ultima+letra
                    listaquery.append(ultima)

                for x in listaquery:
                    sqlinsertar=sqlinsertar+x

                sqlinsertar=sqlinsertar+")"
            
                

            
                try:
                    base=(f"CRUD/bases/{nombre}.db")
                    with sqlite3.connect(base) as conn:
                        c=conn.cursor()
                        c.execute(sqlinsertar,diccInsertar)

                        self.ui.exito.setText("Registro "+str(contadorRegistros)+" Insertado")
                        contadorRegistros=contadorRegistros+1
                        self.ui.valorcampo.clear()

                except Error as e:
                    self.ui.exito.setText("Hay un Error respete el tipo de valor\nO ya Existe ese Registro")

            else:
                self.ui.exito.setText("Faltan Campos Tiene que agregar todos los\nCampos")



        except:
            pass
        
        
        

    def restablecer(self):
        global nombre
        global listaquery
        global listavalor
        global diccInsertar
        global ultima
        global contadorverificacion
        global contadorvalidacion
        global sqlinsertar
        contadorverificacion=0
        contadorvalidacion=0
        
        ultima=""
        sqlinsertar=""
        self.ui.Campos.clear()
        self.ui.exito.setText("")
        listaquery=[]
        listavalor=[]
        diccInsertar={}
        
        try:
            base=(f"CRUD/bases/{nombre}.db")
            with sqlite3.connect(base) as conn:
                c=conn.cursor()
                paso1="PRAGMA table_info("
                sql=paso1+nombretabla+")"
                c.execute(sql)
                descripcion=c.fetchall()

                for a in descripcion:
                    for x in a[1:2]:
                        listavalor.append(x)

                for campo in listavalor:
                    self.ui.Campos.addItem(campo)
                    contadorverificacion=contadorverificacion+1
                
                
        except Error as e:
            self.ui.error.setText(e)



    def atras(self):
        global listaquery
        global listavalor
        global dato 
        global listacampos
        global contadorRegistros
        global diccInsertar

        global contadorverificacion
        global contadorvalidacion
        global sqlinsertar
        sqlinsertar=""
        contadorverificacion=0
        contadorvalidacion=0
       
        contadorRegistros=1
        diccInsertar={}
        listaquery=[]
        listavalor=[]
        dato=""
        listacampo=[]
        self.hide()
        self.parent().show()
        self.close()



if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())