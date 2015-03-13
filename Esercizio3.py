#!/usr/bin/python

def fatt(n):
	if n<=1:
		return 1
	else:
		return n*fatt(n-1)


class punto:
	def __init__(self,_x=0,_y=0):
		self.x = _x
		self.y = _y
		print "Oggetto Costruito"


if __name__ == '__main__':

	print fatt(4)
	
	a=punto(4,4)
	b=punto(3,3)
