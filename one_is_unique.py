from z3 import *

s = Solver()

one = Int('one')
zero = Int('zero')
# constant c as another multiplication identity
c = Int('c')

# addition
f = Function('f', IntSort(), IntSort(), IntSort())
# multiplication
g = Function('g', IntSort(), IntSort(), IntSort())
# addition inverse
i = Function('i', IntSort(), IntSort())

ground_term = [one, zero, c]

for x in ground_term:
    s.add(And(
        g(x, one) == x,
        g(one, x) == x
        ))

for x in ground_term:
    s.add(And(
        g(x, c) == x,
        g(c, x) == x,
        c != one
    ))

print(s.check())