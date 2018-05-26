def outer(aFun):
	print 'this must be printed'
	def inner():
		print 'lemme print here'
		ret = aFun() + 1
		print 'the value returned is ' + str(ret)
		return ret
	return inner
	
def aFun():
	return 1
	
aFun = outer(aFun)

aFun()