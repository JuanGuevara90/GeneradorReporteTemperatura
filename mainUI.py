# -*- coding: utf-8 -*-

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

class Ui_MainWindow(object):

    def variables(self):
        self.N_='n'
        self.FECHA_='fecha'
        self.HORA_='hora'
        self.TEMPERATURA_='temperatura'

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
            self.graphicsView.plot(x=(df['n']), y=df[self.TEMPERATURA_], pen='#2196F3')
            self.graphicsView.setLabel("bottom", "Tiempo / Centigrado")
            #Generar reporte
            self.generatedReport(df)
        except NameError:
            print("error: "+NameError)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RECAHOLT"))
        MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
        self.pushButtonAbrir.setText(_translate("MainWindow", "Open file and report generator"))
        self.graphicsView = self.graphicsView.addPlot(row=1, col=1)

    def generatedReport(self,df):


        #Image
        filename = './cap.png'

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo2.pdf")

        #Imagen
        elements.append(Image(filename, width=1*inch, height=1*inch))
        elements.append(Spacer(1,1*inch))

        #Titulo
        elements.append(Paragraph('<font >REPORTE DE TEMPERATURA</font>', stylesheet['Title']))
        elements.append(Spacer(1,1*inch))

        #Descripcion
        elements.append(Paragraph('<font color=red >Que tal</font>', stylesheet['BodyText']))

        #Grafico
        drawing = Drawing(400, 200)
        data = [
        ((1,1), (2,2), (2.5,1), (3,3), (4,5)), 
        ]
        lp = LinePlot()
        lp.x = 50
        lp.y = 50
        lp.height = 125
        lp.width = 300
        lp.data = data
        lp.joinedLines = 1
        #lp.lineLabelFormat = '%2.0f' 
        lp.strokeColor = colors.black
        lp.xValueAxis.valueMin = 0 
        lp.xValueAxis.valueMax = 20
        #lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5] 
        lp.xValueAxis.labelTextFormat = '%2.1f'
        lp.yValueAxis.valueMin = 0 
        lp.yValueAxis.valueMax = 7 
        lp.yValueAxis.valueStep = 1
        drawing.add(lp)

        elements.append(drawing)

        #Tabla

        style_table = TableStyle([
            ('BACKGROUND',(0,0),(3,0),colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(3,120),'CENTER'),
            ('FONTNAME',(0,0),(-1,0),'Courier-Bold')

        ])

        data_table=[
            ['No', 'Fecha', 'Hora','Temperatura / Centigrados'],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [1,'2/1/2020','12:00',20],
            [2,'2/1/2020','12:00',20],
        ]
        table = Table(data_table)
        table.setStyle(style_table)
        elements.append(table)

        elements.append(Spacer(1,1*inch))
        elements.append(Spacer(1,1*inch))

        #Firma
        elements.append(Paragraph('<font name="chsFont">Hola</font>', stylesheet['Title']))
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