def decorator(f):
	def inner():
		print('before')
		retval = f()
		print('after')
		return retval
	return inner
@decorator
def example():
	print ('inside')
example()
