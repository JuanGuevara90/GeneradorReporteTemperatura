# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
import pandas
from PyQt5.QtGui import QPixmap
import os

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
            self.variables()
            #Nombre de encabezados del archivo CSV
            

            filename= QtWidgets.QFileDialog.getOpenFileName()
            df = pandas.read_csv(filename[0])


            #Graficar valores
            

            self.graphicsView.plot(x=(df['n']), y=df[self.TEMPERATURA_], pen='#2196F3')

            self.graphicsView.setLabel("bottom", "Tiempo / Centigrado")

            self.generatedReport(df)
        except NameError:
            print("error: "+NameError)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RECAHOLT"))
        MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
        self.pushButtonAbrir.setText(_translate("MainWindow", "Open file and report generator"))
        self.graphicsView = self.graphicsView.addPlot(row=1, col=1)

    def generatedReport(self,df,persona,values_ST_T,contPuls):
        #Valores D1
        D1_max= df[self.D1_].max()
        Time_D1=df.query("D1 == '{0}'".format(D1_max))
        int_timeD1= float(Time_D1["x"].values[0])

        ST_D1= values_ST_T[self.D1_]['d1_INTERVAL_1_MAX']
        Time_ST_D1=self.d1_INTERVAL_1.query("D1 == '{0}'".format(ST_D1))
        int_time_ST_D1= float(Time_ST_D1["x"].values[0])

        T_D1= values_ST_T[self.D1_]['d1_INTERVAL_2_MAX']
        Time_T_D1=self.d1_INTERVAL_2.query("D1 == '{0}'".format(T_D1))
        int_time_T_D1= float(Time_T_D1["x"].values[0])

        P_D1= values_ST_T[self.D1_]['d1_INTERVAL_3_MAX']
        Time_P_D1=self.d1_INTERVAL_3.query("D1 == '{0}'".format(P_D1))
        int_time_P_D1= float(Time_P_D1["x"].values[0])
        
        #Valores D2

        D2_max= df[self.D2_].max()
        Time_D2=df.query("D2 == '{0}'".format(D2_max))
        int_timeD2= float(Time_D2["x"].values[0])

        ST_D2= values_ST_T[self.D2_]['d2_INTERVAL_1_MAX']
        Time_ST_D2=self.d2_INTERVAL_1.query("D2 == '{0}'".format(ST_D2))
        int_time_ST_D2= float(Time_ST_D2["x"].values[0])
        
        T_D2= values_ST_T[self.D2_]['d2_INTERVAL_2_MAX']        
        Time_T_D2=self.d2_INTERVAL_2.query("D2 == '{0}'".format(T_D2))
        int_time_T_D2= float(Time_T_D2["x"].values[0])

        P_D2= values_ST_T[self.D2_]['d2_INTERVAL_3_MAX']        
        Time_P_D2=self.d2_INTERVAL_3.query("D2 == '{0}'".format(P_D2))
        int_time_P_D2= float(Time_P_D2["x"].values[0])

        #Valores D3

        D3_max= df[self.D3_].max()
        Time_D3=df.query("D3 == '{0}'".format(D3_max))
        int_timeD3= float(Time_D3["x"].values[0])

        ST_D3= values_ST_T[self.D3_]['d3_INTERVAL_1_MAX']
        Time_ST_D3=self.d3_INTERVAL_1.query("D3 == '{0}'".format(ST_D3))
        int_time_ST_D3= float(Time_ST_D3["x"].values[0])
        
        T_D3= values_ST_T[self.D3_]['d3_INTERVAL_2_MAX']        
        Time_T_D3=self.d3_INTERVAL_2.query("D3 == '{0}'".format(T_D3))
        int_time_T_D3= float(Time_T_D3["x"].values[0])

        P_D3= values_ST_T[self.D3_]['d3_INTERVAL_3_MAX']        
        Time_P_D3=self.d3_INTERVAL_3.query("D3 == '{0}'".format(P_D3))
        int_time_P_D3= float(Time_P_D3["x"].values[0])

        #Valores AVF

        AVF_max= df[self.AVF_].max()
        Time_AVF=df.query("AVF == '{0}'".format(AVF_max))
        int_timeAVF= float(Time_AVF["x"].values[0])

        ST_AVF= values_ST_T[self.AVF_]['avf_INTERVAL_1_MAX']
        Time_ST_AVF=self.avf_INTERVAL_1.query("AVF == '{0}'".format(ST_AVF))
        int_time_ST_AVF= float(Time_ST_AVF["x"].values[0])
        
        T_AVF= values_ST_T[self.AVF_]['avf_INTERVAL_2_MAX']        
        Time_T_AVF=self.avf_INTERVAL_2.query("AVF == '{0}'".format(T_AVF))
        int_time_T_AVF= float(Time_T_AVF["x"].values[0])

        P_AVF= values_ST_T[self.AVF_]['avf_INTERVAL_3_MAX']        
        Time_P_AVF=self.avf_INTERVAL_3.query("AVF == '{0}'".format(P_AVF))
        int_time_P_AVF= float(Time_P_AVF["x"].values[0])

        #Valores AVR

        AVR_max= df[self.AVR_].min()
        Time_AVR=df.query("AVR == '{0}'".format(AVR_max))
        int_timeAVR= float(Time_AVR["x"].values[0])

        ST_AVR= values_ST_T[self.AVR_]['avr_INTERVAL_1_MAX']
        Time_ST_AVR=self.avr_INTERVAL_1.query("AVR == '{0}'".format(ST_AVR))
        int_time_ST_AVR= float(Time_ST_AVR["x"].values[0])
        

        T_AVR= values_ST_T[self.AVR_]['avr_INTERVAL_2_MAX']      
        Time_T_AVR=self.avr_INTERVAL_2.query("AVR == '{0}'".format(T_AVR))
        int_time_T_AVR= float(Time_T_AVR["x"].values[0])

        P_AVR= values_ST_T[self.AVR_]['avr_INTERVAL_3_MAX']      
        Time_P_AVR=self.avr_INTERVAL_3.query("AVR == '{0}'".format(P_AVR))
        int_time_P_AVR= float(Time_P_AVR["x"].values[0])

        #Valores AVL

        AVL_max= df[self.AVL_].max()
        Time_AVL=df.query("AVL == '{0}'".format(AVL_max))
        int_timeAVL= float(Time_AVL["x"].values[0])

        ST_AVL= values_ST_T[self.AVL_]['avl_INTERVAL_1_MAX']
        Time_ST_AVL=self.avl_INTERVAL_1.query("AVL == '{0}'".format(ST_AVL))
        int_time_ST_AVL= float(Time_ST_AVL["x"].values[0])
        
        T_AVL= values_ST_T[self.AVL_]['avl_INTERVAL_2_MAX']        
        Time_T_AVL=self.avl_INTERVAL_2.query("AVL == '{0}'".format(T_AVL))
        int_time_T_AVL= float(Time_T_AVL["x"].values[0])

        P_AVL= values_ST_T[self.AVL_]['avl_INTERVAL_3_MAX']        
        Time_P_AVL=self.avl_INTERVAL_3.query("AVL == '{0}'".format(P_AVL))
        int_time_P_AVL= float(Time_P_AVL["x"].values[0])
        
        # ###################################
        # Content
        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")

        path5 = os.path.join(base_path, 'Report.pdf')

        fileName = path5

        documentTitle = 'ECG REPORT'
        title = 'ECG REPORT'
        subTitle = 'Name:'+persona["Nombre"] +" Age:"+persona["Edad"] +" Gender:"+persona["Genero"]

        textLines = [
        'D1 / R:'+str(float(D1_max))+'     ST: '+str(float(ST_D1))+'     T: '+str(float(T_D1))+'     P: '+str(float(P_D1)),
        'Time: '+str(float(int_timeD1)) +'  Time: '+str(float(int_time_ST_D1))+'  Time: '+str(float(int_time_T_D1))+'  Time: '+str(float(int_time_P_D1)),
        'D2 / R:'+str(float(D2_max))+'     ST: '+str(float(ST_D2))+'     T: '+str(float(T_D2)) +'     P: '+str(float(P_D2)),
        'Time: '+str(float(int_timeD2)) +'  Time: '+str(float(int_time_ST_D2))+'  Time: '+str(float(int_time_T_D2))+'  Time: '+str(float(int_time_P_D2)),
        'D3 / R:'+str(float(D3_max))+'     ST: '+str(float(ST_D3))+'     T: '+str(float(T_D3))+'     P: '+str(float(P_D3)),
        'Time: '+str(float(int_timeD3)) +'  Time: '+str(float(int_time_ST_D3))+'  Time: '+str(float(int_time_T_D3))+'  Time: '+str(float(int_time_P_D3)),
        'aVF / R:'+str(float(AVF_max)) +'     ST: '+str(float(ST_AVF))+'     T: '+str(float(T_AVF))+'     P: '+str(float(P_AVF)),
        'Time: '+str(float(int_timeAVF)) +'  Time: '+str(float(int_time_ST_AVF))+'  Time: '+str(float(int_time_T_AVF))+'  Time: '+str(float(int_time_P_AVF)),
        'aVR / R:'+str(float(AVR_max)) +'     ST: '+str(float(ST_AVR))+'     T: '+str(float(T_AVR))+'     P: '+str(float(P_AVR)),
        'Time: '+str(float(int_timeAVR)) +'  Time: '+str(float(int_time_ST_AVR))+'  Time: '+str(float(int_time_T_AVR))+'  Time: '+str(float(int_time_P_AVR)),
        'aVL / R:'+str(float(AVL_max)) +'     ST: '+str(float(T_AVL))+'     T: '+str(float(ST_AVL))+'     P: '+str(float(P_AVL)),
        'Time: '+str(float(int_timeAVL)) +'  Time: '+str(float(int_time_ST_AVL))+'  Time: '+str(float(int_time_T_AVL))+'  Time: '+str(float(int_time_P_AVL)),
        ]
        # ###################################
        # 0) Create document 
        from reportlab.pdfgen import canvas 

        pdf = canvas.Canvas(fileName)
        pdf.setTitle(documentTitle)

        #self.drawMyRuler#(pdf)
        # ###################################
        # 1) Title :: Set fonts 
        # # Print available fonts
        # for font in pdf.getAvailableFonts():
        #     print(font)

        # Register a new font
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase import pdfmetrics

        try:
            base_path= sys._MEIPASS
        except Exception:
            base_path=os.path.abspath(".")
        


        path4 = os.path.join(base_path, 'SakBunderan.ttf')
        print(path4)


        pdfmetrics.registerFont(
            TTFont('abc', path4)
        )
        pdf.setFont('abc', 36)
        pdf.drawCentredString(300, 770, title)

        # ###################################
        # 2) Sub Title 
        # RGB - Red Green and Blue
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290,720, subTitle)

        # ###################################
        # 3) Draw a line
        pdf.line(30, 710, 550, 710)

        # ###################################
        # 4) Text object :: for large amounts of text
        from reportlab.lib import colors

        text = pdf.beginText(40, 680)
        text.setFont("Courier", 13)
        text.setFillColor(colors.red)
        val=True
        for line in textLines:
            text.textLine(line)
            if val:
                text.setFillColor(colors.black)
                val=False
            else :
                text.setFillColor(colors.red)
                val=True
                text.textLine("")

        #Valor maximo de X
        value_max_X=float(df["x"].max())/3600
        text.textLine("")
        text.textLine("")
        text.textLine("")
        text.textLine("")
        text.setFillColor(colors.blue)
        truncate = "%.6f" % value_max_X
        text.textLine('Connetion time: '+str(truncate) +" h")
        text.textLine("")
        text.textLine('Heart rate: '+str(round(contPuls)*10) +" bpm")
    

        pdf.drawText(text)
        pdf.save()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


 
 
   


 