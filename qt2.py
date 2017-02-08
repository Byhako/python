# -*- coding: utf-8 -*-

# Ejemplo cuadro de dialogo

import PyQt4.QtGui as QG 
import sys

# linea = 0

# with open('prueba3.py', 'r') as f:
# 	for l in f:
# 		linea += 1

# 	print(linea)	
# -----------------------------------------------------------------------
class Cuental(QG.QDialog):
	
	def __init__(self):
		super(Cuental, self).__init__()
		
		self.linea = 0

		self.setWindowTitle('Cuenta Lineas')
		self.resize(350,100)
		self.move(400,200)

		vbox = QG.QVBoxLayout(self)

		self.boton = QG.QPushButton('Abrir Archivo')
		self.bsalir = QG.QPushButton('Salir')
		self.label = QG.QLabel(' ')
		self.label.hide()
		self.label2 = QG.QLabel(' ')
		self.label2.hide()

		vbox.addWidget(self.bsalir)
		vbox.addWidget(self.boton)
		vbox.addWidget(self.label)
		vbox.addWidget(self.label2)		

		self.setLayout(vbox)

		self.boton.clicked.connect(self.dialogo)
		self.bsalir.clicked.connect(self.close)

	# * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * * 	
		
	def dialogo(self):
		# abre cuadro de dialogo para abrir archivo
		self.linea = 0
		direc ='/home/ruben/Dropbox/Caja_Python' 
		ext = '(*.py)'
		nombre = QG.QFileDialog.getOpenFileName(self, 'Abrir archivo',direc,ext)	

		if nombre:
			self.abrir_archivo(nombre)

	# * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *
	
	def abrir_archivo(self, nombre):
		with open(nombre, 'r') as f:
			for i in f:
				self.linea += 1

			self.mostrar(self.linea,nombre)

	# * * *   * * *   * * *   * * *   * * *   * * *   * * *   * * *
	
	def mostrar(self, linea, nombre):
		self.label.setText('%s\n' %(nombre))
		self.label2.setText('<h3>El archivo tiene %s lineas.</h3>' %(str(linea)))
		self.label.show()
		self.label2.show()

# -----------------------------------------------------------------------

app = QG.QApplication(sys.argv)
w = Cuental()
w.show()

app.exec_()
sys.exit()