class parent:
	parentattr = 100
	def __init__(self):
		print "calling parent constructer"
	def parentmethod(self):
		print "calling parent method"
	def setattr(self,attr):
		parent.parentattr = attr
	def getattr(self):
		print "paarent attribute: ",parent.parentattr
class child(parent):
	def __init__(self):
		print "calling child constructor"
	def childmethod(self):
		print "calling child method"
c = child()
c.childmethod()
c.parentmethod()
c.setattr(200)
c.getattr()
