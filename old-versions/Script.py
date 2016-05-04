"""
	This program has been develop by Jaime Diez Gonzalez-Pardo in 
	order to facilitate operations in performing laboratory practice

															Version: 2.0
		Update: Be able to change data after have introduced it
"""
from math import fabs # import absolute function from math package
import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package

Title = str(raw_input('Title: ')) # Introduce the title of the practice

Xname = str(raw_input('Dependent variable: ')) # Dependent variable's name
Xmed = str(raw_input('Units: ')) # units of the dependent variable

Mx = np.array([]) # inicialize the array of data
boolone = True # inicialize the boolean used into the while
samplex = 1 # inicialize the number of samples of DV

while boolone : # loop to insert data 
	x = (raw_input('%s x = ' %(samplex))) # introduce a new value
	if str(x) == 'End' or str(x) == 'end' or str(x) == 'Fin' or str(x) == 'fin': # if the new value is 'end', stop the loop
		boolone = False # stop the loop 
	else:
		boolone = True # continue with the loop
		Mx = np.insert(Mx, Mx.size, float(x)) # append a new element to the array
		samplex += 1 # plus another sample


Yname = str(raw_input('independent variable: ')) # IV's name
Ymed = str(raw_input('Units: ')) # units of the independent variable(IV)

My = np.array([]) # inicialize the data array of IV
booltwo = True # inicialize the boolean used into the while
sampley = 1 # inicialize the number of samples of IV

while booltwo : # loop to insert data
	y = (raw_input('%s y = ' %(sampley))) # introduce a new value

	if str(y) == 'End' or str(y) == 'end' or str(y) == 'Fin' or str(y) == 'fin': # if the new value is 'end', stop the loop
		booltwo = False # stop the loop 
	else:
		booltwo = True # continue with the loop
		My = np.insert(My, My.size, float(y)) # append a new element to the array
		sampley += 1 # plus another sample

while Mx.size != My.size: # check if there r the same number of data in DV's array than in IV's one
	
	if Mx.size >= My.size: # More data from DV
		print 'Sorry, U have more measures of %s than %s' %(Xname, Yname)
		mistake() # ejecute mistake function
	else: # More data from IV
		print 'Sorry U have more measures of %s than %s' %(Yname, Xname)
		mistake() # ejecute mistake function



def mistake(): # add, delete or change an element from arrays
	global My, Mx # let use Mx and My variables
	correct = str(raw_input('R all the measures correct?' + '\n' + 'if it is not please write which one is not correct (x or y)')) # choose array
	while str(correct) != 'ok': # loop ejecute mistake while correct is not equal 'ok'
		if str(correct) == 'x': # choose DV's list
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
	c = 3*(10**8)
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
