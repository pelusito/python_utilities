from math import sqrt, sin, pi, degrees, radians
import numpy as np
import matplotlib.pyplot as plt

Title = str(raw_input('Title: '))

Xname = str(raw_input('Dependent variable: '))
Xmed = str(raw_input('Units: '))

x = (raw_input('x= '))

Mx = np.array([])

boolone = True

while boolone :
	Mx = np.insert(Mx, Mx.size, float(x)) #kdvsjnlsnak
	x = (raw_input('x= '))
	if str(x) == 'End':
		boolone = False
	else:
		boolone = True


Yname = str(raw_input('independent variable: '))
Ymed = str(raw_input('Units: '))
y = (raw_input('y= '))

My = np.array([])

booltwo = True 

while booltwo :
	My = np.insert(My, My.size, float(y))
	y = (raw_input('y= '))
	if str(y) == 'End':
		booltwo = False
	else:
		booltwo = True

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

			x_median = float(Mx.sum()) / float(Mx.size)
			x_i = Mx - x_median
			a = x_i * My
			xx_i = x_i**2
			m = float(a.sum()) / float(xx_i.sum())
			return m

		def intercept(self):
			Mxx = Mx**2
			Mxy = Mx*My
			qwerty = (float(My.sum())*float(Mxx.sum())-float(Mx.sum())*float(Mxy.sum())) / (float(Mx.size)*float(Mxx.sum()) - (float(Mx.sum()))**2)
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
			p = np.sum(Mx)
			u = Mx.size
			print p/u

		def medianY(self):
			p = np.sum(My)
			u = My.size
			print p/u

Graphics().save()