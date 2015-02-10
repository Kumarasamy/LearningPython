from sys import argv

script,name,age = argv
height = raw_input("Your height ")
print script
print "name %s"  % name
print "Age %s " % age
print "Height %s" % int(height)
