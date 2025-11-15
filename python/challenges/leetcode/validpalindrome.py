"""
Given a string s, return true if it is a palindrome, or false otherwise.

"""

def isPalindrome(s: str) -> bool:
    # convert to lovercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    # remove all special characters 
    return s[::-1] == s


print(isPalindrome("A man, a plan, a canal"))
print(isPalindrome("racecar"))
print(isPalindrome("0P"))
