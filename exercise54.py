


#Problem 5.4
#Name: Patrick Kennedy


def is_triangle(a, b, c):
	if ((a+b) < c):
		print "It can be a triangle!"
	elif((b+c) < a):
		print "It can be a triangle!"
	elif((c+a) < b):
		print "it can be a tringle!"
	else:
		print "Can't be a triangle!"


def user_triangle():
	a = int (raw_input('enter a side of a triangle:')) 
	b = int (raw_input('enter a side of a triangle:')) 
	c = int (raw_input('enter a side of a triangle:')) 
	is_triangle(a, b, c)


user_triangle()





























wait_for_user()
