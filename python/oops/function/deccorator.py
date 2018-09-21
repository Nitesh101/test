def make_bold(fn):
	def wrapped():
		return "<b>" + fn() + "</b>"
	return wrapped
def make_italic(fn):
	def wrapped():
		return "<i>" + fn() + "</i>"
	return wrapped
def make_underlinr(fn):
	def wrapped():
		return "<u>" + fn() + "</u>"
	return wrapped
@make_bold
@make_italic
@make_underlinr
def hello():
	return "hello world"
print (hello())
