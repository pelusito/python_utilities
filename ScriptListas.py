"""
	This program has been develop by Jaime Diez Gonzalez-Pardo in 
	order to facilitate operations in performing laboratory practice

															Version: 2.0
		Update: Be able to change data after have introduced it
"""

from math import fabs, sqrt # import absolute and square root function from math package
import os # import os Miscellaneous operating system interfaces
import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package
 
def mistake(): # add, delete or change an element from lists
	global My, Mx # let use Mx and My variables
	correct = str(raw_input('R all the measures correct?' + '\n' + 'if it is not please write which one is not correct (x or y) ')) # choose list
	while str(correct) != 'ok': # loop ejecute mistake while correct is not equal 'ok'
		if str(correct) == 'x': # choose DV's list
			print Mx # print the list on screen
			action = str(raw_input('Choose action: ')) # choose between add, delete or change
			if action == 'delete': # delete option
				element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to delete started from 1 instead 0
				del Mx[element-1] # delete the element 
			elif action == 'add': # add option
				x = (raw_input('x = ')) # new element
				Mx.append(float(x)) # append the new element
			elif action == 'change': # change option
				element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to change started from 1 instead 0
				x = (raw_input('x = ')) # new element
				Mx.append(float(x)) # append the new element
				del Mx[element-1] # delete the old element
		elif str(correct) == 'y': # choose IV's list
			print My # print the list on screen
			action = str(raw_input('Choose action: ')) # choose between add, delete or change
			if action == 'delete': # delete option
				element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to delete started from 1 instead 0
				del My[element-1] # delete the element
			elif action == 'add': # add option
				y = (raw_input('y = ')) # new element
				My.append(float(y)) # append the new element
			elif action == 'change': # change option
				element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to delete started from 1 instead 0
				y = (raw_input('y = ')) # new element
				My.append(float(y)) # append the new element
				del My[element-1] # delete the old element
		else :
			print 'sorry I can not understand U' # error problem
		correct = raw_input('R all the measures correct?' + '\n' + 'if it is not please write which one is not correct (x or y) ') # return the loop

def orderMagnitude(w): # change the order of magnitude to w
	global Mx, My # let use Mx and My variables
	lists = (raw_input('In which data? ')) # choose list
	if str(lists) == 'Mx': # choose DV's list
		for i in xrange(len(Mx)): # loop that go over element by element the DV list
			Mx[i] = Mx[i] *(10**(w)) # multiply each element by 10 to w
	elif str(lists) == 'My': # choose IV's list
		for i in xrange(len(My)): # loop that go over element by element the DV list
			My[i] = My[i] *(10**(w)) # multiply each element by 10 to w

def frequencyWavelength(): # convert frequency to wavelength or vice versa
	global Mx # let use Mx variable
	c = 3*(10**8) # set light speed
	newMx = [] # new list with DV data
	for i in xrange(len(Mx)): # loop that go over element by element the DV list
		newMx.append(Mx[i])
	if Xmed == 'nm':
		newXname = 'Frequency/Hz'
		for i in xrange(len(Mx)): # loop that go over element by element the DV list
			Mx[i] = Mx[i] *(10**(-9)) # multiply each element by 10 to -9
		for i in xrange(len(Mx)): # loop that go over element by element the DV list
			Mx[i] = c / Mx[i] # Convert each element to frequency
		fl = open(Path+Title+'.ods', 'w') # open and create an .ods file
		for x in xrange(1): # loop to write the file
			fl.write(Xname+'/'+Xmed+ "\t" + newXname + '\t' + Yname+'/'+Ymed + "\n") # write a header
			for i in range(len(Mx)): # loop to write element by element to the file
				fl.write((str(Mx[i]) + "\t" + str(newMx[i]) + '\t' + str(My[i]) + "\n")) # write in two colums
			fl.write('\n' + 'Slope' + '\t'+ str(slope()) + '\n')
			fl.write('intercept' + '\t' + str(intercept()) + '\n')
			fl.close() # close file
	else:
		newname = 'Wave Length/nm'
		for i in xrange(len(Mx)): # loop that go over element by element the DV list
			Mx[i] = c / Mx[i] # Convert each element to frequency or wavelength
		fl = open(Path+Title+'.ods', 'w') # open and create an .ods file
		for x in xrange(1): # loop to write the file
			fl.write(Xname+'/'+Xmed+ "\t" + newname + '\t' + Yname+'/'+Ymed + "\n") # write a header
			for i in range(len(Mx)): # loop to write element by element to the file
				fl.write((str(Mx[i]) + "\t" + str(My[i]) + "\n")) # write in two colums
			fl.close() # close file

def save(): # save lists into a .ods archive in /home/jaime/Documentos/Data/ path
	fl = open(Path+Title+'.ods', 'w') # open and create an .ods file
	for x in xrange(1): # loop to write the file
		fl.write(Xname+'/'+Xmed+ "\t" + Yname+'/'+Ymed + "\n") # write a header
		for i in range(len(Mx)): # loop to write element by element to the file
			fl.write((str(Mx[i]) + "\t" + str(My[i]) + "\n")) # write in two colums
		fl.close() # close file

def slope(): # Calculate the slope of a linear graph (IV to DV)
	xless = [] # inicialize a list DV-Xmean
	a = [] # inicialize a list 
	xxi = [] # inicialize a list xless*xless
	for i in xrange(len(Mx)): # loop append a new element to lists 
		xless.append(Mx[i] - medianX())
		a.append(xless[i] * My[i])
		xxi.append(xless[i]**2)
	return sum(a) / sum(xxi) # return the slope

def intercept(): # calculate the intercept of the graph 
	Mxx = [] # inicialize a list for DV*DV
	Mxy = [] # inicialize a list for DV*IV
	for i in xrange(len(Mx)): # loop that append an element 
		Mxx.append(Mx[i]**2)
		Mxy.append(Mx[i]*My[i])
	return (sum(My)*sum(Mxx)-sum(Mx)*sum(Mxy)) / (len(Mx)*sum(Mxx) - (sum(Mx))**2) # return intercept

def graph(): # print the graph
	xes = np.arange(min(Mx),max(Mx), ((max(Mx)-min(Mx))/100)) # create an array to represent the straight graphic on X axis
	yes = slope()*xes + intercept() # create a list to represent the straght graphic on Y axis

	maxy = max(My) + fabs(My[len(My)-1]-My[len(My)-2])*0.5 # Max value for y axis 
	miny = min(My) - fabs(My[1]-My[0])*0.5 # Min value for y axis
	maxx = max(Mx) + fabs(Mx[len(Mx)-1]-Mx[len(Mx)-2])*0.5 # max value for x axis
	minx = min(Mx) - fabs(Mx[1]-Mx[0])*0.5 # min value for x axis

	yerr = float(raw_input("The %s's error " %(Yname))) # error for IV

	# Represent the graphic
	fig = plt.figure()
	plt.errorbar(Mx, My, yerr=yerr, fmt='ro', ecolor='r') 
	plt.plot(Mx, My, 'ro', xes, yes, 'r')
	plt.axis([minx, maxx, miny, maxy])
	plt.title(Title)
	plt.xlabel(Xname+'/'+Xmed)
	plt.ylabel(Yname+'/'+Ymed)
	fig.savefig(Path+Title+'.png')
	plt.show()

	f2 = plt.figure(figsize=(12.0, 20.0))

def printer(): # Print means and the graph equation 
	fl = open(Path+Title+'.txt','w')
	for x in xrange(1):
		fl.write('Los valores medios de X y de Y son:' + "\n")
		fl.write('\t' + ' <x>= ' + str(medianX()) + 'm y <y>= ' + str(medianY()) + 's'+'\n')
		fl.write('La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n')
		fl.write('\t' + 'y = ' + str(slope()) + 'x + ' + str(intercept()) + '\n')
	print 'Los valores medios de X y de Y son:' + "\n" + "\t" + ' <x>= %sm y <y>= %ss' %(medianX(), medianY())
	print 'La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n' + '\t' + 'y = %sx + %s' %(slope(), intercept())

def errors(): # calculate errors of slope and intercept
	yerr = float(raw_input("The %s's error " %(Yname))) # error for IV

	Mxx = [] # inicialize a list for DV*DV

	for i in xrange(len(Mx)): # loop that append an element into Mxx
		Mxx.append(Mx[i]**2)

	Sm = yerr * sqrt(len(Mx) / (len(Mx)*sum(Mxx) - sum(Mx)**2)) # slope error
	Sb = yerr * sqrt(sum(Mxx) / (len(Mx)*sum(Mxx) - sum(Mx)**2)) # intercept error

	print 'The slope error is: Sm = %s and the intercept error is: Sb = %s' %(Sm,Sb)

def medianX(): # return the mean of DV
	return sum(Mx) / len(Mx) # return the DV mean

def medianY(): # return the mean of IV
	return sum(My) / len(My)

Title = str(raw_input('Title: ')) # Introduce the title of the practice
Path = './Escritorio/Python/'+Title+'/'
dir = os.path.dirname(Path)
if not os.path.exists(Path):
	os.makedirs(Path)


Xname = str(raw_input('Dependent variable: ')) # Dependent variable's name (DV)
Xmed = str(raw_input('Units: ')) # units of the DV

Mx = [] # inicialize the data list of DV
boolone = True # inicialize the boolean used into the while
samplex = 1 # inicialize the number of samples of DV

while boolone : # loop to insert data 
	x = (raw_input('%s x = ' %(samplex))) # introduce a new value

	if str(x) == 'End' or str(x) == 'end' or str(x) == 'Fin' or str(x) == 'fin': # if the new value is 'end', stop the loop
		boolone = False # stop the loop 
	else:
		boolone = True # continue with the loop
		Mx.append(float(x)) # append a new element to the list
		samplex += 1 # plus another sample

Yname = str(raw_input('independent variable: ')) # IV's name
Ymed = str(raw_input('Units: ')) # units of the independent variable(IV)

My = [] # inicialize the data list of IV
booltwo = True # inicialize the boolean used into the while
sampley = 1 # inicialize the number of samples of IV

while booltwo : # loop to insert data
	y = (raw_input('%s y = ' %(sampley))) # introduce a new value

	if str(y) == 'End' or str(y) == 'end' or str(y) == 'Fin' or str(y) == 'fin': # if the new value is 'end', stop the loop
		booltwo = False # stop the loop 
	else:
		booltwo = True # continue with the loop
		My.append(float(y)) # append a new element to the list
		sampley += 1 # plus another sample

while len(Mx) != len(My): # check if there r the same number of data in DV's list than in IV's one
	
	if len(Mx) >= len(My): # More data from DV
		print 'Sorry, U have more measures of %s than %s' %(Xname, Yname)
		mistake() # ejecute mistake function
	else: # More data from IV
		print 'Sorry U have more measures of %s than %s' %(Yname, Xname)
		mistake() # ejecute mistake function

print 'Mistake'+' | '+'Order of Magnitude'+' | '+'Frequency to Wavelength'+' | '+'Save'+' | '+'Graph'+' | '+'Printer'+' | '+'Errors'+'\n' # print functions available

function = str(raw_input('Choose function: ')) # select one function

print ' ' # blank space

while function != 'close': # loop to select function. if the function es close, stop the program

	if function == 'Mistake' or function == 'mistake':
		mistake() # ejecute mistake() function
	elif function == 'Order of Magnitude' or function == 'order of magnitude' or function == 'Order of magnitude' or function == 'order of Magnitude' :
		q = float(raw_input('Order??')) # ask the order of Magnitude
		orderMagnitude(q) # ejecute orderMagnitude() function with q argument
	elif function == 'Frequency to Wavelength' or function == 'frequency to Wavelength' or function == 'Frequency to wavelength' or function == 'frequency to wavelength':
		frequencyWavelength() # ejecute frequencyWavelength() function
	elif function == 'Save' or function == 'save':
		save() # ejecute save()function
	elif function == 'Graph' or function == 'graph':
		graph() # ejecute graph() function
	elif function == 'Printer' or function == 'printer':
		printer() # ejecute printer() function
	elif function == 'Errors':
		errors() # ejecute errors() function
	else:
		print 'sorry I can not understand U'+'\n' # print a message
	
	function = str(raw_input('Choose function: ')) # ask again for a function

fl = open('./1.csv', 'w') # open and create an .ods file
for x in xrange(1): # loop to write the file
	fl.write(Xname+'/'+Xmed+ "\t" + Yname+'/'+Ymed + "\n") # write a header
	for i in range(len(Mx)): # loop to write element by element to the file
		fl.write((str(Mx[i]) + "\t" + str(My[i]) + "\n")) # write in two colums
	fl.close() # close file
