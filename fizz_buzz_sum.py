# Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.
# For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.
# Because 3+5+6+9=23, our function would return 23.

def fizz_buzz_sum(target):
    
    multiples = []
    for m in [3, 5]:
        f = (target-1) // m
        while f >= 1:
            multiples.append(m*f)
            f -= 1
    return sum(set(multiples))
    
# tests
a = fizz_buzz_sum(10)
assert a == 23, a

a = fizz_buzz_sum(16)
assert a == 60, a

a = fizz_buzz_sum(100)
assert a == 2318, a