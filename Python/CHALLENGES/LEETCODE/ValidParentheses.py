"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s:str) -> bool:
    # loop through the str
    arr = ["[]", "()", "{}"] #valid 

    # creates list of every other elem in string
    everyTwo = list(s[j: j + 2] for j in range(0, len(s), 2))
    
    # check if a list contains anything other than whats in arr
    if not any(x in everyTwo for x in arr):
        print("False")
    else:
        print("True")


    # if ( or { or [ 
    # must be followed by ) or } or ]




def neetcode(s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


print(neetcode("({)}()"))
print(neetcode("({}("))
print(neetcode("(){}"))





