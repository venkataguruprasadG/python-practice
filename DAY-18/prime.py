'''
Challenge 86: Find All Prime Numbers in a Range
Write a function called find_primes that:

Accepts two integers, start and end.

Returns a list of all prime numbers between start and end (inclusive).

For example:

Input: find_primes(10, 20)

Output: `[11, 13, 17,Hints:

A prime number is only divisible by 1 and itself.

Use a helper function to check if a number is prime.

Use a list comprehension to build your list of primes.
'''
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        return False
    return True

def prime_num(start, end):
    return [x for x in range(start, end+1) if is_prime(x)]

print(prime_num(10,20))