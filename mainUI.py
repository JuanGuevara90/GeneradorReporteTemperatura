# -- coding: utf-8 --

#Cambio recien 

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
#Libreria UI
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
from PyQt5.QtWidgets import QMessageBox
import pandas
from PyQt5.QtGui import QPixmap
import os
import sys
import webbrowser
#Librerias Reporte
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Image, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.linecharts import HorizontalLineChart
import random
from datetime import datetime

class Ui_MainWindow(object):

    def variables(self):
        self.N_='n'
        self.FECHA_='fecha'
        self.HORA_='hora'
        self.TEMPERATURA_='Temp1'
        self.TEMPERATURA2_='Temp2'
        self.TEMPERATURA3_='Temp3'
        self.TEMPERATURA4_='Temp4'

    def setupUi(self, MainWindow):
        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        #MainWindow.setStyleSheet("background-color: blue;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAbrir.setGeometry(QtCore.QRect(800, 25, 300, 42))
        self.pushButtonAbrir.setObjectName("pushButtonAbrir")
        #Label Nombre Empresa
        self.label_nom_empre = QtWidgets.QLabel(self.centralwidget)
        self.label_nom_empre.setGeometry(QtCore.QRect(220, 20, 125, 20))
        self.label_nom_empre.setObjectName("label_nom_empresa")
        #self.label_nom_empre.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        #Label Código
        self.label_cod = QtWidgets.QLabel(self.centralwidget)
        self.label_cod.setGeometry(QtCore.QRect(250,50, 50, 20))
        self.label_cod.setObjectName("label_cod")
        #self.label_cod.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        
        #Caja de Texto Nombre Empresa
        self.line_nom_empre = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nom_empre.resize(200, 32)
        self.line_nom_empre.move(360, 10)
        #Caja de Texto Codigo
        self.line_cod = QtWidgets.QLineEdit(self.centralwidget)
        self.line_cod.resize(200, 32)
        self.line_cod.move(360, 45)    

        var_x=200
        var_y=830

        #Labels Sensores
        self.label_sensor1 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor1.setGeometry(QtCore.QRect(var_x+220,var_y, 150, 20))
        self.label_sensor1.setObjectName("label_sensor1")
        self.label_sensor1.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.label_sensor1.setStyleSheet('color: blue')

        self.label_sensor2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor2.setGeometry(QtCore.QRect(var_x+380,var_y, 150, 20))
        self.label_sensor2.setObjectName("label_sensor2")
        self.label_sensor2.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.label_sensor2.setStyleSheet('color: yellow')

        self.label_sensor3 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor3.setGeometry(QtCore.QRect(var_x+540,var_y, 150, 20))
        self.label_sensor3.setObjectName("label_sensor3")
        self.label_sensor3.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.label_sensor3.setStyleSheet('color: red')

        self.label_sensor4 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor4.setGeometry(QtCore.QRect(var_x+700,var_y, 150, 20))
        self.label_sensor4.setObjectName("label_sensor4")
        self.label_sensor4.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
        self.label_sensor4.setStyleSheet('color: green')

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 100, 1300, 700))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 22))
        self.menubar.setObjectName("menubar")

        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButtonAbrir.clicked.connect(self.mybutton_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def mybutton_clicked(self,MainWindow):
        try:

            msg = QMessageBox()
            msg.setWindowTitle("Alerta")
            if self.line_nom_empre.text()=='' or self.line_cod.text()=='':
                msg.setText("Por favor ingreso los campos requeridos")
                x = msg.exec_()
            else:
                #Nombre de encabezados del archivo CSV
                self.variables()
                filename= QtWidgets.QFileDialog.getOpenFileName()
                if filename[0]!='':
                    dirReport=os.path.dirname(filename[0])
                    df = pandas.read_csv(filename[0])
                    #Graficar valores
                    const= df['Hora'][0]
                    tiempo_aux=[]
                    format = '%H:%M:%S'
                    for index, row in df.iterrows():
                        diff = (datetime.strptime(str(row['Hora']), format) - datetime.strptime(str(const), format))/60
                        total_minu = round(diff.total_seconds(),1)
                        tiempo_aux.append(total_minu)
                    
                    x=tiempo_aux
                    y=df[self.TEMPERATURA_]
                    y2=df[self.TEMPERATURA2_]
                    y3=df[self.TEMPERATURA3_]
                    y4=df[self.TEMPERATURA4_]
                    self.graphicsView.plot(x, y,pen='#2196F3')
                    self.graphicsView.plot(x, y2,pen='#eff321')
                    self.graphicsView.plot(x, y3,pen='#f32121')
                    self.graphicsView.plot(x, y4,pen='#21f340')
                    self.graphicsView.setLabel("bottom", "X = Tiempo (Minutos) / Y = Grados (Centigrados)")
                    #Generar reporte
                    self.generatedReport(df,dirReport)
                else:
                    msg.setText("Por favor seleccionar el archivo CSV")
                    x = msg.exec_()

        except Exception as e:
            msg.setText("Por favor seleccione el archivo correcto")
            x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEMPERATURA"))
        MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
        self.pushButtonAbrir.setText(_translate("MainWindow", "Abrir archivo y generar reporte"))
        self.graphicsView = self.graphicsView.addPlot(row=1, col=1)
        self.label_cod.setText(_translate("MainWindow", "Código:"))
        self.label_nom_empre.setText(_translate("MainWindow", "Nombre de Empresa:"))
        self.label_sensor1.setText(_translate("MainWindow", "--- Sensor #1 ---"))
        self.label_sensor2.setText(_translate("MainWindow", "--- Sensor #2 ---"))
        self.label_sensor3.setText(_translate("MainWindow", "--- Sensor #3 ---"))
        self.label_sensor4.setText(_translate("MainWindow", "--- Sensor #4 ---"))

    def generatedReport(self,df,dirReport):

        #Valores de cajas de texto
        nom_empre = self.line_nom_empre.text()
        codigo_text = self.line_cod.text()

        #Image
        filename = './cap.png'

        #pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")
        
        fecha= str(datetime.today().strftime('%Y-%m-%d'))

        address= "Reporte_"+fecha+"_.pdf"
        path = os.path.join(dirReport, address)

        doc = SimpleDocTemplate(path)

        #Imagen
        #elements.append(Image(filename, width=1*inch, height=1*inch))
        #elements.append(Spacer(1,1*inch))

        #Titulo
        elements.append(Paragraph('<font >REPORTE DE TEMPERATURA</font>', stylesheet['Title']))

        #Descripcion
        elements.append(Paragraph('<font >DATOS GENERALES</font>', stylesheet['BodyText']))
        elements.append(Paragraph('<font >Empresa: '+nom_empre+'</font> <font >         Código:  '+codigo_text+'</font>', stylesheet['BodyText']))
        elements.append(Paragraph('<font >Fecha:  '+fecha+'</font>', stylesheet['BodyText']))
        elements.append(Paragraph('<font ></font>', stylesheet['BodyText']))
        
        #Descripcion Ejes
        elements.append(Paragraph('<font >DESCRIPCIÓN GRÁFICO</font>', stylesheet['BodyText']))
        elements.append(Paragraph('<font >      Eje Y = Grados Centigrados / Eje X = Tiempo Minutos</font>', stylesheet['BodyText']))
        elements.append(Paragraph('<font color=blue>        -- Sensor #1 --</font> <font color=yellow>-- Sensor #2 --</font> <font color=red>-- Sensor #3 --</font> <font color=green>-- Sensor #4 --</font>', stylesheet['BodyText']))
        elements.append(Spacer(1,1*inch))

        

        #Datos para el Gráfico

        lista_temp1=[]
        lista_temp2=[]
        lista_temp3=[]
        lista_temp4=[]
        lista_total=[]

        data_table= []
        cabecera=[]
        cabecera.append('No')
        cabecera.append('Fecha')
        cabecera.append('Hora')
        cabecera.append('Temp 1')
        cabecera.append('Temp 2')
        cabecera.append('Temp 3')
        cabecera.append('Temp 4')
        cabecera.append('Tiempo / Minutos')
        data_table.append(cabecera)

        const= df['Hora'][0]

        format = '%H:%M:%S'
        for index, row in df.iterrows():
            diff = (datetime.strptime(str(row['Hora']), format) - datetime.strptime(str(const), format))/60
            total_minu = round(diff.total_seconds(),1)
            c_1= (total_minu,row['Temp1'])
            c_2= (total_minu,row['Temp2'])
            c_3= (total_minu,row['Temp3'])
            c_4= (total_minu,row['Temp4'])
            lista_temp1.append(c_1)
            lista_temp2.append(c_2)
            lista_temp3.append(c_3)
            lista_temp4.append(c_4)
            array_aux=[]
            array_aux.append(row['n'])
            array_aux.append(row['Fecha'])
            array_aux.append(row['Hora'])
            array_aux.append(row['Temp1'])
            array_aux.append(row['Temp2'])
            array_aux.append(row['Temp3'])
            array_aux.append(row['Temp4'])
            array_aux.append(total_minu)
            data_table.append(array_aux)

        lista_total.append(lista_temp1)
        lista_total.append(lista_temp2)
        lista_total.append(lista_temp3)
        lista_total.append(lista_temp4)

        elements.append(Spacer(1,1*inch))
        elements.append(Spacer(1,1*inch))

        drawing = Drawing(400, 200)
        lp = LinePlot()
        lp.x = 100
        lp.y = 100
        lp.height = 300
        lp.width = 300
        lp.data = lista_total
        lp.joinedLines = 1
        #lp.lineLabelFormat = '%2.0f' 
        lp.strokeColor = colors.black
        lp.xValueAxis.valueMin = 0 
        lp.xValueAxis.valueMax = 100
        lp.xValueAxis.valueStep = 10
        #lp.xValueAxis.valueSteps =listHora_aux
        lp.xValueAxis.labelTextFormat = '%2.1f'
        lp.yValueAxis.valueMin = 0 
        lp.yValueAxis.valueMax = 90 
        lp.yValueAxis.valueStep = 5
        lp.lines[0].strokeColor=  colors.blue
        lp.lines[1].strokeColor=  colors.yellow
        lp.lines[2].strokeColor=  colors.red
        lp.lines[3].strokeColor=  colors.green

        drawing.add(lp)

        elements.append(drawing)

        #Tabla
        elements.append(Paragraph('<font >DESCRIPCIÓN TABLA</font>', stylesheet['BodyText']))
        elements.append(Paragraph('<font ></font>', stylesheet['BodyText']))

        style_table = TableStyle([
            ('BACKGROUND',(0,0),(7,0),colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(7,120),'CENTER'),
            ('FONTNAME',(0,0),(-1,0),'Courier-Bold')

        ])

        table = Table(data_table)
        table.setStyle(style_table)
        elements.append(table)

        elements.append(Spacer(1,1*inch))
        elements.append(Spacer(1,1*inch))

        #Firma
        #elements.append(Paragraph('<font >Hola</font>', stylesheet['Title']))
        elements.append(Spacer(1,1*inch))

        doc.build(elements)
        msg = QMessageBox()
        msg.setWindowTitle("Alerta")
        msg.setText("Correcta Generación de Reporte !!!")
        x = msg.exec_()

#if __name__ == "__main__":
#    import sys
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()