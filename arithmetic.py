class mathfunc:
	def __init__(self, a, b):
		self.a = float(a)
		self.b = float(b)

	def funcadd(self):
		print "\n Addition 		:", self.a+self.b;

	def funcsub(self):
		print " Substraction 		:", self.a-self.b;

	def funcmultiply(self):
		print " Multiplication 	:", self.a*self.b;

	def funcdivide(self):
		print " Division 		:", self.a/self.b;  

	def __del__(self):			
		class_name = self.__class__.__name__	