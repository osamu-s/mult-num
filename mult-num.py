#!/usr/bin/env python3

from functools import reduce

def mul_list(nl):
    return reduce((lambda x, y: x * y), nl)

def num_mult(nnum):
    n = nnum
    count = 0
    while n > 9:
        count += 1
        n = mul_list(map(int, list(str(n))))
    return (count, nnum)

def max_digits(d):
    gl = [num_mult(n) for n in range(10**(d-1), 10**d)]
    mx = max(gl, key=(lambda x: x[0]))[0]
    return list(filter((lambda x: x[0] == mx), gl))

# print(max((num_mult(n) for n in range(10, 10000000)),
#          key=lambda x:x[0]))
# print (num_mult(99))
# print(sorted((num_mult(n) for n in range(10, 10000)), key=lambda x:x[0]))

for i in range(2, 8):
    print(max_digits(i))
