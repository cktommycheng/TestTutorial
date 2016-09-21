# calculating f(x) using the first expression
# f(x) = 3.95*x*(1-x)
def f1(x, n=1) :
	# check the domain of x, else raise an error
	if(x > 1 or x < 0) :
		print("Invalid value of x !")
		return None
	else :
		# recursive step
		if(n > 1) :
			return f1(3.95*x - 3.95*(x**2), n-1)
		# base case
		else :
			return 3.95*x*(1-x)



# calculating f(x) using the first expression
# f(x) = 3.95*x - 3.95*x*x
def f2(x, n=1) :
	# check the domain of x, else raise an error
	if(x > 1 or x < 0) :
		print("Invalid value of x !")
		return None
	else :
		# recursive step
		if(n > 1) :
			return f2(3.95*x - 3.95*(x**2), n-1)
		# base case
		else :
			return 3.95*x - 3.95*(x**2)



# calculating f(x) using the first expression
# f(x) = 3.95*(x-x*x)
def f3(x, n=1) :
	# check the domain of x, else raise an error
	if(x > 1 or x < 0) :
		print("Invalid value of x !")
		return None
	else :
		# recursive step
		if(n > 1) :
			return f3(3.95*x - 3.95*(x**2), n-1)
		# base case
		else :
			return 3.95*(x-(x**2))



print(f1(0.9, 100), f2(0.9, 100), f3(0.9, 100))