#!/usr/bin/python3
# author; Alexander Brockmeier

import timeit

''' three ways of calculating the fibonacci sequence are
    shown for a difference of >30 and 10 times of runs the first approach
    is way to slow.'''

#range(start | stop + 1 | number of `runs` | default-for-sum_ | toggle)
start, stop, times, fib1, fib_one = 1, 1001 + 1, 2, 0, False # no run of fib_one(1) if false

# No1: pure recursion
def fibonacci_1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_1(n-1) + fibonacci_1(n-2)


def loop1(start, stop):
    for n in range(start, stop):
        print(n, ':', fibonacci_1(n))

def callloop1():
    loop1(start, stop)
if fib_one is True:
    fib1 = timeit.timeit(stmt=callloop1, number=times)


#No2: with memoization
fibonacci_cache = {}
def fibonacci_2(n):
    #approx?

    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_2(n-1) + fibonacci_2(n-2)



    # cache n` return
    fibonacci_cache[n] = value
    return value

def loop2(start, stop):
    for n in range(start, stop):
        print(n, ':', fibonacci_2(n))

def callloop2():
    loop2(start, stop)

fib2 = timeit.timeit(stmt=callloop2, number=times)


#No3: with functools` lru_cache
from functools import lru_cache

@lru_cache() # funtion is same as fibonacci_1
def fibonacci_1_b(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_1_b(n-1) + fibonacci_1_b(n-2)


def loop1_b(start, stop):
    for n in range(start, stop):
        print(n, ':', fibonacci_1_b(n))

def callloop1_b():
    loop1_b(start, stop)

fib1_b = timeit.timeit(stmt=callloop1_b, number=times)
fib_sum = fib1 + fib2 + fib1_b


# TODO: append to a list of dicts and/or a log / some yml-file?
print(f'start@: {start}, stop@: {stop}, {times}-runs, fibonacci_1:{fib_one}')
if fib_one is True:
    print(f'fibonacci_1: {fib1}sec.')
print(f'fibonacci_2: {fib2}sec.')
print(f'fibonacci_1_b: {fib1_b}sec.')
print(f'Sum: {fib_sum}')
