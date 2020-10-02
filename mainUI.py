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
import pandas
from PyQt5.QtGui import QPixmap
import os
import sys
#Librerias Reporte
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Image, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.charts.lineplots import LinePlot
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
        
        path1 = os.path.join(base_path, "imagen1.jpeg")
        path2 = os.path.join(base_path, "imagen2.jpeg")


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 747)
        #MainWindow.setStyleSheet("background-color: blue;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAbrir.setGeometry(QtCore.QRect(280, 30, 300, 32))
        self.pushButtonAbrir.setObjectName("pushButtonAbrir")

        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 100, 800, 600))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 22))
        self.menubar.setObjectName("menubar")
    
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.pushButtonAbrir.clicked.connect(self.mybutton_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def mybutton_clicked(self):
        try:
            #Nombre de encabezados del archivo CSV
            self.variables()
            filename= QtWidgets.QFileDialog.getOpenFileName()
            df = pandas.read_csv(filename[0])
            #Graficar valores
            x=(df['n'])
            y=df[self.TEMPERATURA_]
            y2=df[self.TEMPERATURA2_]
            y3=df[self.TEMPERATURA3_]
            y4=df[self.TEMPERATURA4_]
            self.graphicsView.plot(x, y,pen='#2196F3')
            self.graphicsView.plot(x, y2,pen='#eff321')
            self.graphicsView.plot(x, y3,pen='#f32121')
            self.graphicsView.plot(x, y4,pen='#21f340')
            self.graphicsView.setLabel("bottom", "Tiempo / Centigrado")
            #Generar reporte
            self.generatedReport(df)
        except NameError:
            print("error: "+NameError)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEMPERATURA"))
        MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
        self.pushButtonAbrir.setText(_translate("MainWindow", "Open file and report generator"))
        self.graphicsView = self.graphicsView.addPlot(row=1, col=1)

    def generatedReport(self,df):


        #Image
        filename = './cap.png'

        #pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("Reporte_"+str(datetime.today().strftime('%Y-%m-%d'))+"_.pdf")

        #Imagen
        #elements.append(Image(filename, width=1*inch, height=1*inch))
        #elements.append(Spacer(1,1*inch))

        #Titulo
        elements.append(Paragraph('<font >REPORTE DE TEMPERATURA</font>', stylesheet['Title']))
        elements.append(Spacer(1,1*inch))

        #Descripcion
        elements.append(Paragraph('<font color=red >MADERAS DEL ORIENTE</font>', stylesheet['BodyText']))
        elements.append(Spacer(1,1*inch))
        elements.append(Spacer(1,1*inch))

        #Datos para el Gráfico

        lista_temp1=[]
        lista_temp2=[]
        lista_temp3=[]
        lista_temp4=[]
        lista_total=[]
        lista_temp1.append((0,0))
        lista_temp2.append((0,0))
        lista_temp3.append((0,0))
        lista_temp4.append((0,0))

        data_table= []
        cabecera=[]
        cabecera.append('No')
        cabecera.append('Fecha')
        cabecera.append('Hora')
        cabecera.append('Temp 1')
        cabecera.append('Temp 2')
        cabecera.append('Temp 3')
        cabecera.append('Temp 4')
        data_table.append(cabecera)

        
        for index, row in df.iterrows():
            c_1= (row['n'],row['Temp1'])
            c_2= (row['n'],row['Temp2'])
            c_3= (row['n'],row['Temp3'])
            c_4= (row['n'],row['Temp4'])
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
            data_table.append(array_aux)

        lista_total.append(lista_temp1)
        lista_total.append(lista_temp2)
        lista_total.append(lista_temp3)
        lista_total.append(lista_temp4)

        



        drawing = Drawing(400, 200)
        lp = LinePlot()
        lp.x = 100
        lp.y = 100
        lp.height = 100
        lp.width = 300
        lp.data = lista_total
        lp.joinedLines = 1
        #lp.lineLabelFormat = '%2.0f' 
        lp.strokeColor = colors.black
        lp.xValueAxis.valueMin = 0 
        lp.xValueAxis.valueMax = 5000
        lp.xValueAxis.valueStep = 1000
        #lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5] 
        lp.xValueAxis.labelTextFormat = '%2.1f'
        lp.yValueAxis.valueMin = 0 
        lp.yValueAxis.valueMax = 90 
        lp.yValueAxis.valueStep = 10
        lp.lines[0].strokeColor=  colors.red
        lp.lines[1].strokeColor=  colors.blue
        lp.lines[2].strokeColor=  colors.black
        lp.lines[3].strokeColor=  colors.green

        drawing.add(lp)

        elements.append(drawing)

        #Tabla

        style_table = TableStyle([
            ('BACKGROUND',(0,0),(6,0),colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(3,120),'CENTER'),
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())