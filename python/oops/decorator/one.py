def a_new_decorator(a_func):
	def wrapthefunction():
		print("I am doing before some thing")
		a_func()
		print("I am doing after something")
	return wraphtefunction
@a_new_decorator
def function():
	print ("
