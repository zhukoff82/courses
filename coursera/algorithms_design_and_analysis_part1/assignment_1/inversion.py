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
	inv_count = 0
  
	for idx_i, val_i in enumerate( inp_array ) : 
#                print idx_i, val_i
		for idx_j, val_j in enumerate( inp_array[ idx_i + 1: ] ) : 
#			print idx_i, val_i, idx_j, val_j
			if val_i > val_j :
				inv_count += 1

	print "Number of inversions:", inv_count
	end = time.time()
	print "Execution time:", end - start, "sec"
elif choose_algorithm == 1 :
	print "#2 divide and conquer algorithm"
	start = time.time()
	def merge_sort( arr, len ) :	
		inv_cnt = 0
		i = len / 2 
		j = len - i
		lhs = arr[ 0:i ]
		rhs = arr[ len - j: ]
        	if i > 0 :
        		inv_cnt = merge_sort( lhs, i )
			inv_cnt += merge_sort( rhs, j )
			inv_cnt += merge( arr, lhs, rhs, i, j )
		return inv_cnt

	def merge( orig_arr, lhs, rhs, len_l, len_r) :
		inv_cnt = 0
		i = 0
		j = 0
		k = 0
		while ( len_l > 0 and len_r > 0 ) :
			if lhs[ j ] <= rhs[ k ] :
				orig_arr[ i ] = lhs[ j ]
				len_l -= 1
				j += 1
			else :
				orig_arr[ i ] = rhs[ k ]
				len_r -= 1
				k += 1
				inv_cnt += len_l 
			i += 1

                while ( len_l > 0 ) :
			orig_arr[ i ] = lhs[ j ]
			len_l -= 1
			j += 1
			i += 1

		while ( len_r > 0 ) :
			orig_arr[ i ] = rhs[ k ]
                        len_r -= 1
			k += 1
			i += 1

		return inv_cnt

	inv_count = merge_sort( inp_array, num_elem )
       	print "Number of inversions: ", inv_count
        end = time.time()
        print "Execution time:", end - start, "sec"
