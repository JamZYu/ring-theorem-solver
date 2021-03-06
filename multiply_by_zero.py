from z3 import *
from itertools import permutations, product
from copy import deepcopy
import argparse


parser = argparse.ArgumentParser(description='Instantiation with certain depth')
parser.add_argument('--depth', dest='depth',
                    default=2,
                    help='depth for instantiation')
depth = int(parser.parse_args().depth)



s = Solver()

one = Int('one')
zero = Int('zero')
# constant d where d * 0 != 0
d = Int('d')

# addition
f = Function('f', IntSort(), IntSort(), IntSort())
# multiplication
g = Function('g', IntSort(), IntSort(), IntSort())
# addition inverse
i = Function('i', IntSort(), IntSort())

func_terms = [f, g, i]
ground_terms = [one, zero, d]

depth_one_terms = [one, zero, d]
for constant in ground_terms:
    depth_one_terms.append(i(constant))
for c1, c2 in product(ground_terms, repeat=2):
    depth_one_terms.append(f(c1, c2))
    depth_one_terms.append(g(c1, c2))

depth_two_terms = depth_one_terms + [i(g(zero, d))]

print("-- Checking for instantiation with depth {}".format(depth))

s.add(Or(
    g(zero, d) != zero,
    g(d, zero) != zero
))

selected_terms = [ground_terms, depth_one_terms, depth_two_terms][depth]

for x,y,z in product(selected_terms, repeat=3):
    s.add(
        f(f(x,y),z) == f(x, f(y,z))
    )
    s.add(
        g(g(x,y),z) == g(x, g(y,z))
    )
    s.add(
        g(x, f(y,z)) == f(g(x,y), g(x,z))
    )
    s.add(
        g(f(x,y), z) == f(g(x,z), g(y,z))
    )

for x,y in product(selected_terms, repeat=2):
    s.add(
        f(x,y) == f(y,x)
    )

for x in selected_terms:
    s.add(And(
        f(x,zero) == x,
        f(zero,x) == x
    ))
    s.add(And(
        f(x, i(x)) == zero, 
        f(i(x), x) == zero
    ))

print(s.check())