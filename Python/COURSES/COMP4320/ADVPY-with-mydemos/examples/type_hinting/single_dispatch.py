import functools


class Twistable:
    pass


class Person:
    pass


@functools.singledispatch
def wound(x):
    print(f'The {x} feels that hurts')


@wound.register
def _(x: Twistable):
    print(f'Wind the {type(x).__name__}')

@wound.register
def anything(x: Person):
    print(f'{type(x).__name__} needs some time off to relax')


wound("Enemy")
wound(Twistable())
wound(Person())
