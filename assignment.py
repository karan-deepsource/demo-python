import os

(*FIRST, ) = [1, 2, 3]
(*FIRST, ) = [1, 2, 3]
*FIRST, a, b = [1, 2, 3]

open("foo")


def foo(foo=None):
    if foo is None:
        foo = []
    return [*foo]
