import itertools


# List for sequence generation
Inputlist = [1, 2, 3]

# Calling the function Cycle from
# itertools and passing list as
# an argument and the function
# returns the iterator object
ListBuffer = itertools.cycle(Inputlist)
SequenceRepeation = 0
SequenceStart = 0
SequenceEnd = len(Inputlist)

for output in ListBuffer:
	if(SequenceStart == 0):
		print("Sequence % d"%(SequenceRepeation + 1))

	# Cycle function iterates through
	# each element and produces the
	# sequence and repeats it the sequence
	print(output, end =" ")

	# Checks the End of the Sequence according
	# to the give input argument
	if(SequenceStart == SequenceEnd-1):
		
		if(SequenceRepeation>= 2):
			break
		else:
			SequenceRepeation+= 1
			SequenceStart = 0
			print("\n")
	else:
		SequenceStart+= 1


