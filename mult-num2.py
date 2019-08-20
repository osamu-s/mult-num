#!/usr/bin/env python3

from functools import reduce

def mul_list(nl):
    return reduce((lambda x, y: x * y), nl)

def num_mult(count, n, nnum):
    if n < 10:
        return (count, nnum)
    return num_mult(count +1, mul_list(map(int, list(str(n)))), nnum)

def max_digits(d):
    gl = (num_mult(0, n, n) for n in range(10**(d-1), 10**d))
    mx = max(gl, key=(lambda x: x[0]))
    return mx

# print(max((num_mult(n) for n in range(10, 10000000)),
#          key=lambda x:x[0]))
# print (num_mult(99))
# print(sorted((num_mult(n) for n in range(10, 10000)), key=lambda x:x[0]))

for i in range(8, 9):
    print(max_digits(i))
