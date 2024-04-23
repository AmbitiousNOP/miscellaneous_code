"""
Given a string of roman numerals. 
Return the equivalent number.
"""

def romanToInt(s:str) -> int:
    romanTranslation = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000,
                        }
    translation = 0
    
    # for char in s
    # if next char is larger
    # than char is negative (aka subtract)
    # else add
    for position, char in enumerate(s):
        try:
            if romanTranslation[char] < romanTranslation[s[position + 1]]:
                translation -= romanTranslation[char]
            else:
                translation += romanTranslation[char]
        except:
            translation += romanTranslation[char]
    return translation

# Top leet code solution
def topRomanToInt(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,}

    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]

    return res

print(romanToInt("IV"))
print(romanToInt("VII"))
print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))


