*FIRST = [1, 2, 3]
(*FIRST,) = [1, 2, 3]
*FIRST, a, b = [1, 2, 3]

import os

open("foo")


import sys

def foo(a=[1]):
  a.append(*a)
  return a
