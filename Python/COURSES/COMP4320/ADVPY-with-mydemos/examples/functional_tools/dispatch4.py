from functools import singledispatch
from decimal import Decimal

@singledispatch
def fun(s):
	print(s)

@fun.register(float)
@fun.register(Decimal)
def _3(s):
	print(round(s, 2))

fun(2.34)
fun(Decimal(4.897))
fun('hey')

print(fun.registry.keys())

print(fun.registry[float])
print(fun.registry[Decimal])
print(fun.registry[object])