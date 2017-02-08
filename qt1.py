# Ejemplo grilla

#from PyQt4 import QtGui
import PyQt4.QtGui as QG
import sys

# ----------------------------------------------------------------
class Ventana(QG.QWidget):

	def __init__(self):
		super(Ventana, self).__init__()

		# Cambia titutlo de ventana
		self.setWindowTitle("Ejemplo PyQt")

		# redimencionar ventana
		self.resize(400,400) # longitud x,  longitud y

		# mover ventana
		self.move(150,100) # derecha,  arriba

		# cambiar icono
		self.setWindowIcon(QG.QIcon('Publico/icon.png'))

		# etiquetas
		label = QG.QLabel('<h2><i>MI PRIMER CALCULADORA</i></h2>', self)
		label.setGeometry(120,6,300,50)
		
		# cuadro de texto
		line_edit = QG.QLineEdit()

		# botones
		bs = QG.QPushButton('Salir', self)
		bb = QG.QPushButton('Borrar', self)
		b1 = QG.QPushButton('1', self)
		b2 = QG.QPushButton('2', self)
		b3 = QG.QPushButton('3', self)
		b4 = QG.QPushButton('4', self)
		b5 = QG.QPushButton('5', self)
		b6 = QG.QPushButton('6', self)
		b7 = QG.QPushButton('7', self)
		b8 = QG.QPushButton('8', self)
		b9 = QG.QPushButton('9', self)
		b0 = QG.QPushButton('0', self)
		bp = QG.QPushButton('.', self)
		ba = QG.QPushButton('+', self)
		br = QG.QPushButton('-', self)
		bm = QG.QPushButton('*', self)
		bd = QG.QPushButton('/', self)
		bi = QG.QPushButton('=', self)

		bs.setGeometry(100,70,70,25)  # pos x, pos y, longx, longy
		bb.setGeometry(230,70,70,25)		

		# layout
		layout_vertical = QG.QVBoxLayout(self)
		layout_vertical.addWidget(label)
		layout_vertical.addWidget(line_edit)

		grilla = QG.QGridLayout()
		grilla.addWidget(bs,0,0)
		grilla.addWidget(bb,0,1)
		grilla.addWidget(b7,1,0)
		grilla.addWidget(b8,1,1)
		grilla.addWidget(b9,1,2)
		grilla.addWidget(b4,2,0)
		grilla.addWidget(b5,2,1)
		grilla.addWidget(b6,2,2)
		grilla.addWidget(b1,3,0)
		grilla.addWidget(b2,3,1)
		grilla.addWidget(b3,3,2)
		grilla.addWidget(b0,4,0)
		grilla.addWidget(bp,4,1)
		grilla.addWidget(bi,4,2)
		grilla.addWidget(bd,1,3)
		grilla.addWidget(bm,2,3)
		grilla.addWidget(br,3,3)
		grilla.addWidget(ba,4,3)
		
		layout_vertical.addLayout(grilla)

		# layout_horizontal = QG.QHBoxLayout(self)
		# layout_horizontal.addWidget(label)
		# layout_horizontal.addWidget(boton1)
		# layout_horizontal.addWidget(boton2)
		# layout_horizontal.addWidget(line_edit)		
		
		# self.setLayout(layout_horizontal)

# ----------------------------------------------------------------	

app = QG.QApplication(sys.argv)

ven = Ventana()
ven.show()

app.exec_() # mantiene viva la aplicacion
sys.exit()  # termina proceso al cerrar aplicacion


"""
Si iniciamos con QWidget la ventana puede ser redimencionada 
a mano, pero si iniciamos con QDialog la ventana siempre tiene
el tamano definido.
"""