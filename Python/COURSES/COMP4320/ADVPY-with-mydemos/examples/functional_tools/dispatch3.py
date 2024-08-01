from functools import singledispatch

@singledispatch
def fun(s):
	print(s)

@fun.register(int)
def _1(s):
	print(s * 2)
 
@fun.register(float)
def _2(s):
	print(s * 5)

@fun.register(list)
def _3(s):
	for i, e in enumerate(s):print(i, e)

fun('GeeksforGeeks')
fun(10)
fun(2.4)
fun(['g', 'e', 'e', 'k', 's'])

