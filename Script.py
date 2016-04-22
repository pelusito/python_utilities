"""
	This program has been develop by Jaime Diez Gonzalez-Pardo in 
	order to facilitate operations in performing laboratory practice

									Version: 2.0
		Update: Be able to change data after have introduced it
"""
from math import fabs
import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package

c = 3**8

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

while Mx.size != My.size:
	
	if Mx.size >= My.size:
		print 'Sorry, U have more measures of %s than %s' %(Xname, Yname)
		mistake()
	else:
		print 'Sorry U have more measures of %s than %s' %(Yname, Xname)
		mistake()



def mistake():
	global My, Mx
	correct = str(raw_input('R all the measures correct?' + '\n' + 'if it is not please write which one is not correct (x or y)'))
	while str(correct) != 'ok':
		if str(correct) == 'x':
			print Mx
			action = str(raw_input('Choose action: '))
			element = float(raw_input('which element do U want to' + action + ' ?? '))
			if action == 'delete':
				Mx = Mx.delete(My, element)
			elif action == 'add':
				y = (raw_input('y = '))
				Mx = np.insert(Mx, element, float(x))
			elif action == 'change':
				y = (raw_input('y = '))
				Mx = np.insert(Mx, element, float(x))
				Mx = np.delete(Mx, element-1)
		elif str(correct) == 'y':
			print My
			action = str(raw_input('Choose action: '))
			element = float(raw_input('which element is not correct??'))
			if action == 'delete':
				My = np.delete(My, element)
			elif action == 'add':
				y = (raw_input('y = '))
				My = np.insert(My, element, float(y))
			elif action == 'change':
				y = (raw_input('y = '))
				My = np.insert(My, element, float(y))
				My = np.delete(My, element-1)
		else :
			print 'sorry I can not understand U'
		correct = raw_input('R all the measures correct?' + '\n' + 'if it is not please write which one is not correct (x or y)')

def orderMagnitude(w):
	global Mx, My
	array = (raw_input('In which data? '))
	if str(array) == 'Mx':
		Mx = Mx *(10**(w))
	elif str(array) == 'My':
		 My = My *(10**(w))

def frequencyWavelength():
	global Mx
	Mx = Mx *(10**(-9))
	Mx = c / Mx

def save():
	w = 0
	fl = open('/home/jaime/Escritorio/'+Title+'.ods', 'w')
	for x in xrange(1):
		fl.write(Xname+'/'+Xmed+ "\t" + Yname+'/'+Ymed + "\n")
		for i in range(Mx.size):
			fl.write((str(Mx.item(w)) + "\t" + str(My.item(w)) + "\n"))
			w += 1
		fl.close()

def slope():

	x_median = Mx.sum() / Mx.size
	x_i = Mx - x_median
	a = x_i * My
	xx_i = x_i**2
	m = a.sum() / xx_i.sum()
	return m

def intercept():
	Mxx = Mx**2
	Mxy = Mx*My
	qwerty = (My.sum()*Mxx.sum()-Mx.sum()*Mxy.sum()) / (Mx.size*Mxx.sum() - (Mx.sum())**2)
	return qwerty

def graph():
	xes = np.arange(Mx.min(),Mx.max(), ((Mx.max()-Mx.min())/100))
	yes = slope()*xes + intercept()

	maxy = My.max() + fabs(My.item(My.size-1)-My.item(My.size-2))*0.5
	miny = My.min() + fabs(My.item(1)-My.item(0))*0.5
	maxx = Mx.max() + fabs(Mx.item(Mx.size-1)-Mx.item(Mx.size-2))*0.5
	minx = Mx.min() - fabs(Mx.item(1)-Mx.item(0))*0.5

	yerr = float(raw_input("The %s's error " %(Yname)))

	plt.figure(1)
	plt.errorbar(Mx, My, yerr=yerr, fmt='ro', ecolor='r') 
	plt.plot(Mx, My, 'ro', xes, yes, 'r')
	plt.axis([minx, maxx, miny, maxy])
	plt.title(Title)
	plt.xlabel(Xname)
	plt.ylabel(Yname)
	plt.show()

	f2 = plt.figure(figsize=(12.0, 20.0))

def medianX():
	p = np.sum(Mx) / Mx.size
	return p

def medianY():
	u = np.sum(My) / My.size
	return u

def printer():
	print 'Los valores medios de X y de Y son:' + "\n" + "\t" + ' <x>= %sm y <y>= %ss' %(medianX(), medianY())
	print 'La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n' + '\t' + 'y = %sx + %s' %(slope(), intercept())
