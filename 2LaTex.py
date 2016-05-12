"""
	JGP (Just a Graphics' Printer)

	This program has been develop by Jaime Diez Gonzalez-Pardo in Python in 
	order to facilitate operations in performing laboratory practice (429)

													Version: 4.0
"""

from math import fabs, sqrt, log, exp # import absolute and square root function from math package
import os # import os Miscellaneous operating system interfaces

os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal window

############################################################
########               PROGRAM BODY             ############
############################################################

class Data_Functions:
	def append_Data(self):
		M = [] # inicialize DV data list
		MM = [] # inicialize DV data list
		nameData = raw_input('File directory: ') # introduce directory name
		while not os.path.exists(nameData):  # check if that directory exists
			print 'Sorry that directory does not exist' # if it is not, print an error message
			nameData = raw_input('File directory: ')  # introduce the correct directory name
		fl = open(nameData,'r') # open file as read
		Titles = fl.readline().split( ) # list with the 2 titles
		Xname = Titles[0] # DV title
		Yname = Titles[1] # IV title
		Data = fl.read().split( ) # list with all the data
		for i in xrange(len(Data)/2): # loop to append data
			M.append(float(Data[i*2])) # all par element r DV data
			MM.append(float(Data[2*(i+1) - 1])) # all odd element r IV data
		fl.close()
		return M, MM, Xname, Yname

	def add_Data(self):
		Xname = str(raw_input('Dependent variable: ')) # Dependent variable's name (DV)
		Xmed = str(raw_input('Units: ')) # units of the DV
		Xname += '/'+Xmed
		boolone = True # inicialize the boolean used into the while
		samplex = 1 # inicialize the number of samples of DV

		while boolone : # loop to insert data 
			x = (raw_input('%s x = ' %(samplex))) # introduce a new value

			if str(x) == 'End' or str(x) == 'end' or str(x) == 'Fin' or str(x) == 'fin': # if the new value is 'end', stop the loop
				boolone = False # stop the loop 
			else:
				boolone = True # continue with the loop
				number = False # inicialize the boolean used into the handling exceptions
				while not number:
					try:
						self.Mx.append(float(x)) # append a new element to the lists
						number = True # stop the loop of the exceptions
					except ValueError:
						print 'Sorry, the value is not a float'
						x = (raw_input('%s x = ' %(samplex))) # introduce a new value
				samplex += 1 # plus another sample
		return self.Mx, Xname

	def mistake(self): # add, delete or change an element from lists
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
					element = int(raw_input('In which element??')) # select in which element add the new number
					x = (raw_input('x = ')) # new element
					Mx.insert(element, float(x)) # append the new element
				elif action == 'change': # change option
					element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to change started from 1 instead 0
					x = (raw_input('x = ')) # new element
					Mx.insert(element, float(x)) # append the new element
					del Mx[element-1] # delete the old element
			elif str(correct) == 'y': # choose IV's list
				print My # print the list on screen
				action = str(raw_input('Choose action: ')) # choose between add, delete or change
				if action == 'delete': # delete option
					element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to delete started from 1 instead 0
					del My[element-1] # delete the element
				elif action == 'add': # add option
					element = int(raw_input('In which element??')) # select in which element add the new number
					y = (raw_input('y = ')) # new element
					My.insert(element, float(y)) # append the new element
				elif action == 'change': # change option
					element = int(raw_input('which element do U want to ' + action + ' ?? ')) # element to delete started from 1 instead 0
					y = (raw_input('y = ')) # new element
					My.insert(element, float(y)) # append the new element
					del My[element-1] # delete the old element
			else :
				print 'sorry I can not understand U' # error problem
			correct = raw_input('R all the measures correct?' + '\n' + 'if it is not please write which one is not correct (x or y) ') # return the loo

class Dependent_Variable(Data_Functions):
	def __init__(self, Mx):
		self.Mx = Mx # inicialize the data list of DV

class Independent_Variable(Data_Functions):
	def __init__(self, Mx):
		self.Mx = Mx

def save(): # save lists into a .ods archive in /home/jaime/Documentos/Data/ path
	fl = open(Path+Title+'.ods', 'w') # open and create an .ods file
	for x in xrange(1): # loop to write the file
		fl.write(Xname + "\t" + Yname + "\n") # write a header
		for i in range(len(Mx)): # loop to write element by element to the file
			fl.write('%g' %(Mx[i]) + "\t" + '%g' %(My[i])+ "\n") # write in two colums
		fl.close() # close file

	fl = open(Path+'LaTex.txt', 'w') # open and create an .ods file
	for x in xrange(1): # loop to write the file
		fl.write('\\begin{table}'+'\n')
		fl.write('\t'+'\\centering'+'\n')
		fl.write('\t'+'\\begin{tabular}'+'\n')
		fl.write('\t'+'\t'+ ' \\'+ '\\\hline'+'\n')
		fl.write('\t'+'\t'+'\\centering'+'\n')
		fl.write('\t'+'\t'+'\t'+Xname + ' & ' + Yname  +' \\'+ '\\\hline'+'\n') # write a header
		for i in range(len(Mx)): # loop to write element by element to the file
			fl.write('\t'+'\t'+'\t'+'%g' %(Mx[i]) + ' & ' + '%g' %(My[i])+ ' \\'+'\\'+'\n') # write in two colums
		fl.write('\t'+'\\end{tabular}'+'\n')
		fl.write('\t'+'\\caption{\\label{Tab:}}'+'\n')
		fl.write('\\end{table}'+'\n')
	fl.close() # close file

##########################################################
##########################################################

print ' | '+'New Proyect'+' | '+'New Table'+' | '+'Open file'+' | '+'Save'+' | '+'\n' # print functions available

function = str(raw_input('Choose function: ')) # select one function

print ' ' # blank space

while function != 'close': # loop to select function. if the function es close, stop the program

	if function == 'New Proyect' or function == 'new proyect' or function == 'New proyect': # start a new proyect
		Title = str(raw_input('Title: ')) # Introduce the title of the practice
		Path = './Escritorio/Python/'+Title+'/'
		dir = os.path.dirname(Path)
		if not os.path.exists(Path):
			os.makedirs(Path)

	elif function == 'Open file' or function == 'open file' or function == 'Open File': # get the data from a file
		Data =Dependent_Variable([]).append_Data() 
		Mx = Data[0]
		My = Data[1]
		Xname = Data[2]
		Yname = Data[3]

		while len(Mx) != len(My): # check if there r the same number of data in DV's list than in IV's one
			if len(Mx) >= len(My): # More data from DV
				print 'Sorry, U have more measures of %s than %s' %(Xname, Yname)
				Data_Functions().mistake() # ejecute mistake function
			else: # More data from IV
				print 'Sorry U have more measures of %s than %s' %(Yname, Xname)
				Data_Functions().mistake() # ejecute mistake function

	elif function == 'New Table' or function == 'new table' or function == 'New table':
		DataX = Independent_Variable([]).add_Data()
		Mx = DataX[0]
		Xname = DataX[1]
		DataY = Independent_Variable([]).add_Data()
		My = DataY[0]
		Yname = DataY[1]

		while len(Mx) != len(My): # check if there r the same number of data in DV's list than in IV's one
			if len(Mx) >= len(My): # More data from DV
				print 'Sorry, U have more measures of %s than %s' %(Xname, Yname)
				Data_Functions().mistake() # ejecute mistake function
			else: # More data from IV
				print 'Sorry U have more measures of %s than %s' %(Yname, Xname)
				Data_Functions().mistake() # ejecute mistake function
		
		os.system('cls' if os.name == 'nt' else 'clear') # clear terminal window

		print ' | '+'New Table'+' | '+'Open file'+' | '+'Save'+' | '+'\n' # print functions available

		print Xname + '\t' + Yname
		for i in xrange(len(Mx)):
			print '%g' %(Mx[i]) + '\t' + '%g' %(My[i])
	
	elif function == 'Save' or function == 'save':
		save() # ejecute save()function

	else:
		print 'sorry I can not understand U'+'\n' # print a message
	
	function = str(raw_input('\n'+'Choose function: ')) # ask again for a function

print ' '