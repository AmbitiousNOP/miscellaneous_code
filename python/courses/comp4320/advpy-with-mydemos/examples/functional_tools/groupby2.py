# function to remove all consecutive duplicates
# from a string 

from itertools import groupby

def removeAllConsecutive(input):
	
	# group all consecutive characters based on their
	# order in string 
 	# we are only concerned about first character of each consecutive substring
	# in given string, so key value will work for us
	# and we will join these keys without space to
	# generate resultant string
	result = []
	for (key,group) in groupby(input):
		result.append(key)

	print (''.join(result))
	
# Driver program
if __name__ == "__main__":    
	input = 'aaaaabbbbbbccaaab' 
	removeAllConsecutive(input) 
