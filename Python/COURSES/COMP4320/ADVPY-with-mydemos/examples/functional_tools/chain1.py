'''
1.
The odd numbers and even numbers are in separate lists. 
Combine them to form a new single list.
'''

from itertools import chain

# a list of odd numbers
odd = [1, 3, 5, 7, 9]
# a list of even numbers
even = [2, 4, 6, 8, 10]
#oddsevens = list(list(odd.extend(even)).extend(odd)).extend
# chaining odd and even numbers
numbers = list(chain(odd, even))
print(numbers)

'''
2.
 Some of the consonants are in a list. 
 The vowels are given in a list. 
 Combine them and also sort them. 
'''

# some consonants
consonants = ['d', 'f', 'k', 'l', 'n', 'p']
# some vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# resultatnt list
res = list(chain(consonants, vowels))

# sorting the list
res.sort()
print(res)


'''
3.
Each String is considered to be an iterable and 
each character in it is considered to be an element in the iterator. 
Thus every character is yielded
'''

res = list(chain('ABC', 'DEF', 'GHI', 'JKL'))
print(res)

''''
4.
'''

st1 = "Spam"
st2 = "Ham"
st3 = "Eggs"

res = list(chain(st1, st2, st3))
print("before joining :", res)

ans = ''.join(res)
print("After joining :", ans)


'''
5.
 Now consider a list like the one given below : 

li=['123', '456', '789']
You are supposed to calculate the sum of the list 
taking every single digit into account. 
So the answer should be : 

        1+2+3+5+6+7+8+9 = 45
'''

li = ['123', '456', '789']

res = list(chain.from_iterable(li))

print("res =", res, end ="\n\n")

new_res = list(map(int, res))

print("new_res =", new_res)

print("\nsum =", sum(new_res))
