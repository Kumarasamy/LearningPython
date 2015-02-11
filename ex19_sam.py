from sys import argv
from os.path import exists

def copy(file,tofile):
	print "%s is exists %s" % (file,exists(file))
	indata = open(file).read()
	print "length ",len(indata)
	outfile = open(tofile ,"w" )
	outfile.write(indata)
	outfile.close()

file = "ex15.py"
out_file = "output.txt"
script , file1 ,file2 = argv
copy(file1,file2)
	
