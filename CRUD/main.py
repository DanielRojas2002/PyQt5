import sqlite3
from sqlite3 import Error
import sys
import os
import time
import webbrowser
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QErrorMessage,QTableWidgetItem
from codigos.creador import Ui_CREADORBD
from codigos.ventanap1 import Ui_VentanaP
from codigos.ventanap2 import Ui_VentanaP2
from codigos.tablas import Ui_CreacionTablas
from codigos.ventanavtablas import Ui_VentanaVisualizadoraTablas
from codigos.ventanaborrartablas import Ui_VentanaBTablas
from codigos.ventanavinsertar import Ui_VentanaValidacionInsertar
from codigos.ventanavborrar import Ui_VentanaValidacionborrar
from codigos.ventanavcambiar import Ui_VentanaValidacioncambiar
from codigos.ventanavseleccionar import Ui_VentanaValidacionseleccionar
from codigos.ventanainformacion import Ui_Ventanainformacion
from codigos.ventanainsertar import Ui_VentanaInsertarRegistros
from codigos.ventanaseleccionar import Ui_VentanaSeleccionar

nombre=""
nombretabla=""
dato=""
ultima=""
sqlinsertar=""
seleccion=""
listaquery=[]
listadatos=[]
listatablas=[]
listavalores=[]
listaValoresInsertar=[]
listavalor=[]
listacampos=[]
diccInsertar={}
listaDescripcion2=[]
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
            otraventana=VentanaVborrar(self)
            otraventana.show()

        elif seleccion=="CAMBIO":
            self.hide()
            otraventana=VentanaVcambiar(self)
            otraventana.show()

        elif seleccion=="SELECCIONAR":
            self.hide()
            otraventana=VentanaVseleccionar(self)
            otraventana.show()

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
            otraventana=VentanaInsertar(self)
            otraventana.show()
        
        else:
            self.ui.error1.setText("No Existe esa Tabla")


    def atras(self):
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
            print(e)

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
                self.ui.tableWidget.setSortingEnabled(True)

            except Error as e:
                print(e)

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
                        self.ui.tableWidget.setSortingEnabled(True)


            except Error as e:
                print(e)









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
            print(e)

        
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
            print(e)



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