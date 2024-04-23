"""
Given an array of strings strs, 
group the anagrams together. 
You can return the answer in any order.
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # sort each string by alphabet
    # if item1 = item2 we know they are the anagrams.
    # append to dict {"aet": ['eat','tea','ate'], "abt": ['bat'], etc}
    # print list of dict values
    dict = {}
    for i in strs:
        sorted_word = ''.join(sorted(i))
        try:
            dict[sorted_word] += [i]
        except:
            dict[sorted_word] = [i]
    
    return [k for k in dict.values()]


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
