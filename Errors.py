from sympy import *
from math import sqrt
import string

class Errores(object):
	
	def __init__(self):
		x = Symbol('x')
		y = Symbol('y')
		self.f = eval(raw_input('funcion: '))
		self.variables = [x, y]
		self.values = [4,5]
		self.errors = [2,1]

	def Errors(self):

		Error_sq = 0
		for i in range(len(self.variables)):
			Error_sq += ((self.f.diff(self.variables[i])*self.errors[i])**2)
		Error_sq = str(Error_sq)
		Error_sq = string.replace(Error_sq, 'x', str(self.values[0]))
		Error_sq = string.replace(Error_sq, 'y', str(self.values[1]))
		print eval(Error_sq)

		_Error_sq = eval(str(Error_sq))	
		print _Error_sq

		Error = sqrt(_Error_sq)
		return Error

print Errores().Errors()
