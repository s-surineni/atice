def outer(aFun):
	def inner():
		return aFun() + 1
	return inner
	
def aFun():
	return 1