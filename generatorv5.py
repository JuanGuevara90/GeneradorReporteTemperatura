from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.charts.lineplots import LinePlot
import random

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

#Firma
elements.append(Paragraph('<font name="chsFont">Hola</font>', stylesheet['Title']))
elements.append(Spacer(1,1*inch))

doc.build(elements)