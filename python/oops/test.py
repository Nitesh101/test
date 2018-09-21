"""
#multiple inheritance
class First(object):
	def __init__(self):
	  super(First,self).__init__()
          print("first")
class Second(object):
	def __init__(self):
	  super(Second,self).__init__()
          print("second")
class Third(Second,First):
	def __init__(self):
	  super(Third,self).__init__()
          print ("third")
Third();
"""
class value(object):
	pass
class input(value):
	pass 
print issubclass(input,value)
