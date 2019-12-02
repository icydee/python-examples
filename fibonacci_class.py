# fibonacci as a class

class fib_exception(Exception):
    pass

class Fibonacci:

	class __Fibonacci:
		def __init__(self):
			self.array = [1,1]

	instance = None

	def __init__(self):
		if not Fibonacci.instance:
			Fibonacci.instance = Fibonacci.__Fibonacci()
	def __getattr__(self, name):
		return getattr(self.instance, name)

	def calc(self, index):

		n = int(index)
		if n < 0 or n != index:
			raise fib_exception()
		elif n <= len(self.array):
			return self.array[n-1]
		else:
			print ("calc %s" % index)
			temp_fib = self.calc(n-2) + self.calc(n-1)
			self.array.append(temp_fib)
			return temp_fib
