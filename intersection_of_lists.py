# Write a function to get the intersection of two lists.
# For example, if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3].

def intersection(a, b):
    return []

tests = [
    (([1,2,3,4,5], [0, 1, 3, 7]), [1,3]),
    (([1,2,3], [4,5,6]), []),
]

for t in tests:
    a, s = t
    assert intersection(*a) == s