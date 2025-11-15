# Python program to demonstrate
# dispatch decorator

from multipledispatch import dispatch


@dispatch(int)
def func(x):
	return x * 2

@dispatch(float)
def func(x):
	return x / 2

# Driver code
print(func(2))
print(func(2.0))
print(func('c'))