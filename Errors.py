from sympy import *
from math import sqrt

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
		Error_sq = Error_sq.evalf(subs={self.variables[0]:self.values[0], self.variables[1]: self.values[1]})
		Error = sqrt(Error_sq)
		return Error

print Errores().Errors()
