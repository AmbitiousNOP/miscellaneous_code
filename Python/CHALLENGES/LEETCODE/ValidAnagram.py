"""
Given two strings s and t, return true if 
t is an anagram of s, and false otherwise.
"""

def isAnagram(s: str, t:str) -> bool:
    # create a list of t letters
    # re create s
    # pop used letter from list
    
    letters = list(t)

    # s = anagram
    # t = nagaram
    # letters = [n, a, g, a, r, a, m]
    # loop: 
    # for l in s:
        # if l in letters:
            # pop l from letter
            # continue 
        # else
            # return false
    for l in s:
        if l in letters:
            letters.remove(l)
        else:
            return "False"
    
    if len(letters) > 0:
        return "False"
    else:
        return "True"
        

print(isAnagram("anagram", "naaram"))
print(isAnagram("a", "ab"))