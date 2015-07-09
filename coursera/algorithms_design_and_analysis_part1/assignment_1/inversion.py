import fileinput
import tkFileDialog
from array import *
import time

print "Inversion algorithm"
print "Open input file"
file_name = tkFileDialog.askopenfilename()
input_file = open( file_name, "r" )
print "Name of the file: ", input_file.name
print "Opening mode : ", input_file.mode
inp_array = array( "I")
for line in input_file :
	inp_array.append( int( line.strip() ) )
print "Close input file"
input_file.close()

num_elem = len( inp_array )
print "File includes", num_elem, "elements"

print "#1 straight forward algorithm"
start = time.time()
count = 0
#print inp_array[ 0 ], inp_array[ num_elem  - 1 ]  
for i in inp_array : 
	j = i + 1
	for j in inp_array : 
		if i > j :
			count = count + 1

print "Number of inversions:", count
end = time.time()
print "execution time:", end - start, "sec"
