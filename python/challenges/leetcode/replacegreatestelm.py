"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


def replaceElements(arr: list[int]) -> list[int]:
    ans = []
    for position in range(len(arr)):
        try:
            ans.append(max(arr[position+1:len(arr)]))
        except:
            ans.append(-1)

    return ans

replaceElements([17,18,5,4,6,1])
replaceElements([400])