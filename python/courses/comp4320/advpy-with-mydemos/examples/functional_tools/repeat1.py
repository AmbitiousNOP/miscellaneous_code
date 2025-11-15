# Python code to demonstrate the working of	
# repeat()
		

import itertools
		
# using repeat() to repeatedly print number
print ("Printing the numbers repeatedly : ")
print (list(itertools.repeat(25, 4)))


# using repeat() to repeatedly print string
print(list(map(str.upper,
			itertools.repeat('hamspameggsspam', 3))))



print ("Printing the numbers repeatedly infinity : ")
print (list(itertools.repeat(25)))

print()