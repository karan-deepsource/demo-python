*FIRST = [1, 2, 3]
(*FIRST,) = [1, 2, 3]
*FIRST, a, b = [1, 2, 3]

import os

open("foo")

a = list(range(10))


def foo(a=None):
  if a is None:
    a = [1]
  a.append(*a)
  return a
