"""
	This program has been develop by Jaime Diez Gonzalez-Pardo in 
	order to facilitate operations in performing laboratory practice
"""

from math import sqrt, sin, pi, degrees, radians
import numpy as np
import matplotlib.pyplot as plt

Title = str(raw_input('Title: '))

Xname = str(raw_input('Dependent variable: '))
Xmed = str(raw_input('Units: '))

Mx = np.array([])

boolone = True

while boolone :
	x = (raw_input('x = '))
	if str(x) == 'End' or str(x) == 'end' or str(x) == 'Fin' or str(x) == 'fin':
		boolone = False
	else:
		boolone = True
		Mx = np.insert(Mx, Mx.size, float(x))


Yname = str(raw_input('independent variable: '))
Ymed = str(raw_input('Units: '))

My = np.array([])

booltwo = True 

while booltwo :
	y = (raw_input('y = '))
	if str(y) == 'End' or str(y) == 'end' or str(y) == 'Fin' or str(y) == 'fin':
		booltwo = False
	else:
		booltwo = True
		My = np.insert(My, My.size, float(y))

if Mx.size != My.size:
	print 'THERE ARE NOT THE SAME NUMBER OF MEASURES OF %s THAN  %s' %(Xname, Yname)

else:
	class Graphics(object):

		#docstring for Grafica#
		VX = Mx
		VY = My

		
		def save(self):
			w = 0
			fl = open('/home/jaime/Escritorio/'+Title+'.ods', 'w')
			for x in xrange(1):
				fl.write(Xname+'/'+Xmed+ "\t" + Yname+'/'+Ymed + "\n")
				for i in range(Mx.size):
					fl.write((str(Mx.item(w)) + "\t" + str(My.item(w)) + "\n"))
					w += 1
				fl.close()

		def slope(self):

			x_median = Mx.sum() / Mx.size
			x_i = Mx - x_median
			a = x_i * My
			xx_i = x_i**2
			m = a.sum() / xx_i.sum()
			return m

		def intercept(self):
			Mxx = Mx**2
			Mxy = Mx*My
			qwerty = (My.sum()*Mxx.sum()-Mx.sum()*Mxy.sum()) / (Mx.size*Mxx.sum() - (Mx.sum())**2)
			return qwerty

		def graph(self):

			xes = np.arange(Mx.min(),Mx.max(), ((Mx.max()-Mx.min())/100))

			yes = Graphics().slope()*xes + Graphics().intercept()

			plt.figure(1)
			plt.subplot(211) 
			plt.plot(Mx, My, 'ro', xes, yes, 'r')
			plt.axis([Mx.min(), Mx.max(), My.min(), My.max()])
			plt.title(Title)
			plt.xlabel(Xname)
			plt.ylabel(Yname)
			plt.show()

			f2 = plt.figure(figsize=(12.0, 20.0))

		def medianX(self):
			p = np.sum(Mx) / Mx.size
			return p

		def medianY(self):
			u = np.sum(My) / My.size
			return u

Graphics().graph()
Graphics().save()
print 'Los valores medios de X y para Y son:' + '\n' + '\t' + ' <x>= %sm y <y>= %ss' %(Graphics().medianX(), Graphics().medianY())
print 'La ecuación de la recta obtenida por el ajuste por mínimos cuadrados es' + '\n' + '\t' + 'y= (%s) x + (%s)' %(Graphics().slope(), Graphics().intercept()) 
