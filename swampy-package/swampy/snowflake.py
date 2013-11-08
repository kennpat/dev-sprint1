from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

bob.delay = .001

pu(bob)
rt(bob, 45)
fd(bob, 300)
lt(bob, 45)
pd(bob)

draw(bob, 10, 10)

wait_for_user()


