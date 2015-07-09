import fileinput
import tkFileDialog
from array import *
import time

print "Inversion algorithm"
algorithm =[ "Straight forward algorithm", "Divide and conquer algorithm" ]

while True :
	try :
		print "Available options"
		for idx, val in enumerate( algorithm ) :
			print idx, val		

		choose_algorithm = int(raw_input("Choose algorithm: "))
		print algorithm[ choose_algorithm ] , "is chosen"
		break
	except :
		print "Oops!  That was not a valid number.  Try again..."

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

if choose_algorithm == 0 :
	print "#1 straight forward algorithm"
	start = time.time()
	count = 0
  
	for i in inp_array : 
		j = i + 1
		for j in inp_array : 
			if i > j :
				count = count + 1

	print "Number of inversions:", count
	end = time.time()
	print "Execution time:", end - start, "sec"
elif choose_algorithm == 1 :
	print "#2 divide and conquer algorithm"
	def merge_sort( arr, len ) :	
		print arr
		i = len / 2 + len % 2
		j = len / 2
		lhs = arr[ 0:i ]
		rhs = arr[ len - j: ]
        	if i > 1 :
        		merge_sort( lhs, i )
			merge_sort( rhs, j )	

	merge_sort( inp_array, num_elem )
