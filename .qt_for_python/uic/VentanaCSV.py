# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaCSV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(1360, 715)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaPrincipal.sizePolicy().hasHeightForWidth())
        VentanaPrincipal.setSizePolicy(sizePolicy)
        VentanaPrincipal.setMinimumSize(QSize(1360, 715))
        font = QFont()
        font.setFamily(u"Arial")
        VentanaPrincipal.setFont(font)
        icon = QIcon()
        icon.addFile(u"../multimedia/vector.ico", QSize(), QIcon.Normal, QIcon.Off)
        VentanaPrincipal.setWindowIcon(icon)
        VentanaPrincipal.setStyleSheet(u"")
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(340, 10, 41, 371))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.line.setFont(font1)
        self.line.setStyleSheet(u"color: rgb(200, 82, 13);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 10, 20, 691))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 0, 1341, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 370, 1341, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(1340, 10, 20, 691))
        self.line_6.setFont(font1)
        self.line_6.setStyleSheet(u"color: rgb(200, 82, 13);")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(695, 10, 31, 371))
        self.line_5.setFont(font1)
        self.line_5.setStyleSheet(u"color: rgb(200, 82, 13);")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 690, 1341, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(380, 20, 311, 129))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titulo2 = QLabel(self.layoutWidget)
        self.titulo2.setObjectName(u"titulo2")
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.titulo2.setFont(font2)
        self.titulo2.setStyleSheet(u"\n"
"border:none;\n"
"border-right: 5px solid gray;\n"
"border-left: 5px solid gray;")
        self.titulo2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.titulo2)

        self.encabezados = QListWidget(self.layoutWidget)
        self.encabezados.setObjectName(u"encabezados")

        self.verticalLayout_2.addWidget(self.encabezados)

        self.errorarchivo = QLabel(self.layoutWidget)
        self.errorarchivo.setObjectName(u"errorarchivo")
        font3 = QFont()
        font3.setFamily(u"HP Simplified Light")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.errorarchivo.setFont(font3)
        self.errorarchivo.setFrameShape(QFrame.Box)
        self.errorarchivo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.errorarchivo)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 331, 341))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.imagen = QLabel(self.layoutWidget1)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setMaximumSize(QSize(325, 150))
        self.imagen.setStyleSheet(u"")
        self.imagen.setFrameShape(QFrame.NoFrame)
        self.imagen.setPixmap(QPixmap(u"../../../../../../Desktop/P Git/PYQT5/PyQt5/CSV/multimedia/vector.ico"))
        self.imagen.setScaledContents(True)
        self.imagen.setMargin(0)

        self.verticalLayout.addWidget(self.imagen)

        self.titulo = QLabel(self.layoutWidget1)
        self.titulo.setObjectName(u"titulo")
        font4 = QFont()
        font4.setFamily(u"Arial Black")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.titulo.setFont(font4)
        self.titulo.setStyleSheet(u"")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.splitter = QSplitter(self.layoutWidget1)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.nombreruta = QLineEdit(self.splitter)
        self.nombreruta.setObjectName(u"nombreruta")
        self.nombreruta.setReadOnly(True)
        self.splitter.addWidget(self.nombreruta)
        self.BUSCAR = QPushButton(self.splitter)
        self.BUSCAR.setObjectName(u"BUSCAR")
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setBold(False)
        font5.setWeight(50)
        self.BUSCAR.setFont(font5)
        self.BUSCAR.setCursor(QCursor(Qt.PointingHandCursor))
        self.BUSCAR.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"\n"
"")
        self.splitter.addWidget(self.BUSCAR)

        self.verticalLayout.addWidget(self.splitter)

        self.verCSV = QRadioButton(self.layoutWidget1)
        self.verCSV.setObjectName(u"verCSV")
        font6 = QFont()
        font6.setFamily(u"Arial Black")
        font6.setBold(True)
        font6.setWeight(75)
        self.verCSV.setFont(font6)

        self.verticalLayout.addWidget(self.verCSV)

        self.graficaPastel = QRadioButton(self.layoutWidget1)
        self.graficaPastel.setObjectName(u"graficaPastel")
        self.graficaPastel.setFont(font6)

        self.verticalLayout.addWidget(self.graficaPastel)

        self.graficaBarras = QRadioButton(self.layoutWidget1)
        self.graficaBarras.setObjectName(u"graficaBarras")
        self.graficaBarras.setFont(font6)

        self.verticalLayout.addWidget(self.graficaBarras)

        self.graficaTenInd = QRadioButton(self.layoutWidget1)
        self.graficaTenInd.setObjectName(u"graficaTenInd")
        self.graficaTenInd.setFont(font6)

        self.verticalLayout.addWidget(self.graficaTenInd)

        self.graficarTenGru = QRadioButton(self.layoutWidget1)
        self.graficarTenGru.setObjectName(u"graficarTenGru")
        self.graficarTenGru.setFont(font6)

        self.verticalLayout.addWidget(self.graficarTenGru)

        self.Estadistica = QRadioButton(self.layoutWidget1)
        self.Estadistica.setObjectName(u"Estadistica")
        self.Estadistica.setFont(font6)

        self.verticalLayout.addWidget(self.Estadistica)

        self.masopciones = QRadioButton(self.layoutWidget1)
        self.masopciones.setObjectName(u"masopciones")
        self.masopciones.setFont(font6)

        self.verticalLayout.addWidget(self.masopciones)

        self.realizar = QPushButton(self.layoutWidget1)
        self.realizar.setObjectName(u"realizar")
        self.realizar.setFont(font5)
        self.realizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.realizar.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.realizar)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 390, 1321, 301))
        self.tableWidget.setStyleSheet(u"")
        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(360, 150, 351, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(380, 170, 311, 191))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tituloGrafica = QLabel(self.layoutWidget2)
        self.tituloGrafica.setObjectName(u"tituloGrafica")
        font7 = QFont()
        font7.setFamily(u"Arial Black")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.tituloGrafica.setFont(font7)
        self.tituloGrafica.setFrameShape(QFrame.Box)
        self.tituloGrafica.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.tituloGrafica)

        self.titulo_Grafico = QLineEdit(self.layoutWidget2)
        self.titulo_Grafico.setObjectName(u"titulo_Grafico")
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(8)
        self.titulo_Grafico.setFont(font8)

        self.verticalLayout_3.addWidget(self.titulo_Grafico)

        self.etiqueta_nombre = QLineEdit(self.layoutWidget2)
        self.etiqueta_nombre.setObjectName(u"etiqueta_nombre")

        self.verticalLayout_3.addWidget(self.etiqueta_nombre)

        self.etiqueta_valor = QLineEdit(self.layoutWidget2)
        self.etiqueta_valor.setObjectName(u"etiqueta_valor")

        self.verticalLayout_3.addWidget(self.etiqueta_valor)

        self.etiqueta_usuario = QLineEdit(self.layoutWidget2)
        self.etiqueta_usuario.setObjectName(u"etiqueta_usuario")

        self.verticalLayout_3.addWidget(self.etiqueta_usuario)

        self.etiqueta_tiempo = QLineEdit(self.layoutWidget2)
        self.etiqueta_tiempo.setObjectName(u"etiqueta_tiempo")

        self.verticalLayout_3.addWidget(self.etiqueta_tiempo)

        self.GRAFICAR = QPushButton(self.layoutWidget2)
        self.GRAFICAR.setObjectName(u"GRAFICAR")
        self.GRAFICAR.setFont(font5)
        self.GRAFICAR.setCursor(QCursor(Qt.PointingHandCursor))
        self.GRAFICAR.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.GRAFICAR)

        self.tableDescripcion = QTableWidget(self.centralwidget)
        self.tableDescripcion.setObjectName(u"tableDescripcion")
        self.tableDescripcion.setGeometry(QRect(720, 80, 611, 291))
        self.tableDescripcion.setStyleSheet(u"")
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(720, 30, 611, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cantidad_registros = QLabel(self.layoutWidget3)
        self.cantidad_registros.setObjectName(u"cantidad_registros")
        self.cantidad_registros.setMinimumSize(QSize(145, 0))
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        font9.setWeight(75)
        self.cantidad_registros.setFont(font9)
        self.cantidad_registros.setStyleSheet(u"border-radius:8px;\n"
"border:1.5px solid black;")
        self.cantidad_registros.setAlignment(Qt.AlignCenter)
        self.cantidad_registros.setMargin(0)

        self.horizontalLayout_2.addWidget(self.cantidad_registros)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.color_ventanas = QPushButton(self.layoutWidget3)
        self.color_ventanas.setObjectName(u"color_ventanas")
        self.color_ventanas.setFont(font5)
        self.color_ventanas.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_ventanas.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.color_ventanas)

        self.color_botones = QPushButton(self.layoutWidget3)
        self.color_botones.setObjectName(u"color_botones")
        self.color_botones.setFont(font5)
        self.color_botones.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_botones.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}")

        self.horizontalLayout.addWidget(self.color_botones)

        self.tipo_fuente = QPushButton(self.layoutWidget3)
        self.tipo_fuente.setObjectName(u"tipo_fuente")
        self.tipo_fuente.setFont(font5)
        self.tipo_fuente.setCursor(QCursor(Qt.PointingHandCursor))
        self.tipo_fuente.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}")

        self.horizontalLayout.addWidget(self.tipo_fuente)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        VentanaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"VECTOR CASA DE BOLSA SA DE CV", None))
        self.titulo2.setText(QCoreApplication.translate("VentanaPrincipal", u"ENCABEZADOS DEL CSV:", None))
#if QT_CONFIG(tooltip)
        self.encabezados.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\">Aqui saldran los Encabezados del CSV</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.errorarchivo.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\">Aqui saldran los Posibles Errores</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.errorarchivo.setText("")
        self.imagen.setText("")
        self.titulo.setText(QCoreApplication.translate("VentanaPrincipal", u"GRAFICAS DE PROMOCION", None))
#if QT_CONFIG(tooltip)
        self.BUSCAR.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Buscar Archivo CSV</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BUSCAR.setText(QCoreApplication.translate("VentanaPrincipal", u"BUSCAR", None))
#if QT_CONFIG(tooltip)
        self.verCSV.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Esta opcion:</span></p><p align=\"center\">Abre el CSV y te muestra los Encabezados para despues poder Graficar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.verCSV.setText(QCoreApplication.translate("VentanaPrincipal", u"Checar Encabezados y Checar el CSV", None))
#if QT_CONFIG(tooltip)
        self.graficaPastel.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Grafica en formato Pastel:</span></p><p align=\"center\">Sirve para representar la proporcion de observaciones que estan en cada categoria.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.graficaPastel.setText(QCoreApplication.translate("VentanaPrincipal", u"Graficar Pastel", None))
#if QT_CONFIG(tooltip)
        self.graficaBarras.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Grafica en formato Barras:</span></p><p align=\"center\">Sirve para representar o ilustrar una cantidad de datos para un mejor entendimiento de los mismos</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.graficaBarras.setText(QCoreApplication.translate("VentanaPrincipal", u"Graficar Barras", None))
#if QT_CONFIG(tooltip)
        self.graficaTenInd.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Grafico en formato Lineal(Tendencia):</span></p><p align=\"center\">Sirve para representar una serie de datos que han sido recolectados atravez del tiempo:</p><p align=\"center\">(De un solo Usuario)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.graficaTenInd.setText(QCoreApplication.translate("VentanaPrincipal", u"Graficar Tendencia (Individual)", None))
#if QT_CONFIG(tooltip)
        self.graficarTenGru.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Grafico en formato Lineal(Tendencia):</span></p><p align=\"center\">Sirve para representar una serie de datos que han sido recolectados atravez del tiempo:</p><p align=\"center\">(GENERAL)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.graficarTenGru.setText(QCoreApplication.translate("VentanaPrincipal", u"Graficar Tendencia (Grupal)", None))
#if QT_CONFIG(tooltip)
        self.Estadistica.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Estadistica Descriptiva</span></p><p align=\"center\">Se podra ver la Estadistiva Descriptiva del CSV</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Estadistica.setText(QCoreApplication.translate("VentanaPrincipal", u"Ver Estadistica Descriptiva", None))
#if QT_CONFIG(tooltip)
        self.masopciones.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Estadistica Descriptiva</span></p><p align=\"center\">Se podra ver la Estadistiva Descriptiva del CSV</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.masopciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Mas Opciones", None))
#if QT_CONFIG(tooltip)
        self.realizar.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Actualizar Opcion</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.realizar.setText(QCoreApplication.translate("VentanaPrincipal", u"ACTUALIZACION", None))
        self.tituloGrafica.setText("")
#if QT_CONFIG(tooltip)
        self.titulo_Grafico.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ingrese el Nombre del Grafico</span></p><p align=\"center\">(El que usted desee)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.titulo_Grafico.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.etiqueta_nombre.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ingrese el nombre de la Etiqueta </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.etiqueta_valor.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ingrese el nombre de la Etiqueta del valor</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.etiqueta_usuario.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ingrese el nombre del Usuario a buscar</span></p><p align=\"center\">(Ingreselo exactamente como esta abajo)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.etiqueta_tiempo.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ingrese el nombre de la Etiqueta donde esta el Tiempo</span></p><p align=\"center\">(Las Fechas)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.GRAFICAR.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-weight:600;\">Graficar CSV</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.GRAFICAR.setText(QCoreApplication.translate("VentanaPrincipal", u"GRAFICAR", None))
        self.cantidad_registros.setText("")
#if QT_CONFIG(tooltip)
        self.color_ventanas.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p>Cambiar el Color de todas las Ventanas</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.color_ventanas.setText(QCoreApplication.translate("VentanaPrincipal", u"COLOR VENTANAS", None))
#if QT_CONFIG(tooltip)
        self.color_botones.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p>Cambiar el Color de todos los Botones</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.color_botones.setText(QCoreApplication.translate("VentanaPrincipal", u"COLOR BOTONES", None))
#if QT_CONFIG(tooltip)
        self.tipo_fuente.setToolTip(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p>Cambiar el Color de todos los Botones</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tipo_fuente.setText(QCoreApplication.translate("VentanaPrincipal", u"FUENTE LETRAS", None))
    # retranslateUi

