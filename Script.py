from math import sqrt, sin, pi, degrees, radians
import numpy as np
import matplotlib.pyplot as plt

Xname = str(raw_input('Variable dependiente: '))
Xmed = str(raw_input('Unidades: '))

x = (raw_input('x= '))

Mx = np.matrix([])

boolone = True

while boolone :
	Mx = np.matrix ([Mx, float(x)])
	x = (raw_input('x= '))
	if str(x) == 'fin':
		boolone = False
	else:
		boolone = True


Yname = str(raw_input('Variable independiente: '))
Ymed = str(raw_input('Unidades: '))
y = (raw_input('y= '))

My = np.matrix([])

booltwo = True 

while booltwo :
	My = np.matrix ([My, float(y)])
	y = (raw_input('y= '))
	if str(y) == 'fin':
		booltwo = False
	else:
		booltwo = True

if Mx.size != My.size:
	print 'NO HAY EL MISMO NUMERO DE DATOS DE %s QUE DE %s' %(Xname, Yname)

else:
	class Grafica(object):

		#docstring for Grafica#
		Titulo = str(raw_input('Titulo: '))
		VX = Mx
		VY = My

		
		def guardar(self):
			w = 0
			fl = open('/home/jaime/Escritorio/Table.ods', 'w')
			for i in range(Mx.size):
				fl.write(Xname+'/'+Xmed+ "\t" + Yname+'/'+Ymed + "\n")
				while w <= Mx.size:
					fl.write((str(Mx.item(w)) + "\t" + str(My.item(w)) + "\n"))
					w += 1
				fl.close()

		def pendiente(self):

			x_median = float(Mx.sum()) / float(Mx.size)
			x_i = Mx - x_media
			a = x_i * My
			xx_i = x_i**2
			m = float(a.sum()) / float(xx_i.sum())
			return m

		def ordenada(self):
			Mxx = Mx**2
			Mxy = Mx*My
			qwerty = (float(My.sum())*float(Mxx.sum())-float(Mx.sum())*float(Mxy.sum())) / (float(Mx.size)*float(Mxx.sum()) - (float(Mx.sum()))**2)
			return qwerty

		def grafica(self):

			xes = range(Mx.min(),Mx.max(), ((Mx.max()-Mx.min())/100))

			yes = Grafica().pendiente()*xes + Grafica().ordenada()

			f2 = plt.figure(figsize=(12.0, 20.0))

			plt.figure(1)
			plt.subplot(211)
			plt.plot(Mx, My, 'ro', xes, yes, 'r')
			plt.axis([Mx.min()])
			plt.title(Titulo)
			plt.xlabel(Xname)
			plt.ylabel(Yname)
			plt.show()

		def medianX(self):
			return float(Mx.sum()) / float(Mx.size)

		def medianY(self):
			return float(My.sum()) / float(My.size)

print Grafica().medianX()
