*FIRST = [1, 2, 3]
(*FIRST,) = [1, 2, 3]
*FIRST, a, b = [1, 2, 3]

import os

open("foo")

def oo(oo=None):
  if oo is None:
    oo = []
  return [*oo]
