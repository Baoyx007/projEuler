# -*- coding: utf-8 -*-
__author__ = 'PCPC'

n = 0


def fib_even():
    a, b = 1, 2
    while 1:
        if a%2==0:
            yield a
        a, b = b, a + b

sum=0
for n in fib_even():
    print(n)
    if sum>4000000:
        break
    sum+=n

print(sum)
