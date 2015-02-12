def add(a,b):
	print "ADDING %d + %d " %(a, b)
	return a + b

def subtract(a,b):
	print"SUBTRACTING %d - %d" %(a , b)
	return a - b
def multiply(a,b):
	print "MULTIPLYING %d * %d " %( a,b)
	return a * b
def divide(a,b):
	print"DIVIDING %d / %d" %( a ,b )
	return a / b

def my_fun():
	return "Hello"

print "Let's do some math with just fucntions!"

age = add( 20 ,5)
height = subtract( 78 ,4 )
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d ,Height: %d ,Weight:%d , IQ:%d" % (age,height,weight,iq)


what = add(age,subtract(height,multiply(weight,divide(8,subtract(20,add(iq,2))))))

print "That becomes: ", what , "Can you do it by hand ?"

formula = add( 24 ,divide(34 ,subtract(100 ,1023 )))
print formula


var = my_fun()
print var
