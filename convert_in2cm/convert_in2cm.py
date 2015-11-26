def convert_in2cm(inches):
	return inches * 2.54

inch_in = int(raw_input("Enter your measurement:  "))
a = convert_in2cm(inch_in)
print "Your value is " + str(a)
