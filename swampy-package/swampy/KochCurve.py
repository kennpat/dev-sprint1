#Question 5.6: Koch Curve

from TurtleWorld import *
from math import *


world = TurtleWorld()
bob = Turtle()
print bob


def drawKoch(turt, length):

	if length < 3:
		fd(turt, 5)		
		return
	m = length/3.0
	
	#fd(turt, length)
	drawKoch(turt, m)
	lt(turt, 60)	
	drawKoch(turt, m)
	#fd(turt, length)
	rt(turt, 120)
	drawKoch(turt, m)
	#fd(turt, length2)
	lt(turt, 60)
	drawKoch(turt, m)
	


bob.delay = .001

howfar = 100

for i in range (3):
	drawKoch(bob, howfar)
	





wait_for_user()