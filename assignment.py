*FIRST = [1, 2, 3]
(*FIRST,) = [1, 2, 3]
*FIRST, a, b = [1, 2, 3]

import os

open("foo")

a = list([i for i in range(10)])


def foo(a=[1]):
  a.append(*a)
  return a
