#!/usr/bin/python
def beep():
   print "\a"

# ask for the pace count
answer = raw_input("Enter your pace count  ")
# reply with the pace 
print "You entered " + str(answer) + " paces"
# print out the equation
print "Calculating = 100/paces"
# calculate
ft = 100/int(answer)

beep()

print str(ft) + " feet/pace"
