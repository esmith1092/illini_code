from turtle import *

def circle():
	color('blue', 'orange')
	begin_fill()
	while True:
		left(9)
		forward(30)
		if abs(pos()) < 1:
			break
	end_fill()
	done()

		
circle()