# Given an list of integers called input, return True if any value appears at least twice in the array. Return False if every element in the input list is distinct.
# For example, if the input list was [1,3,5,7,1], then return True because the number 1 shows up twice.
# However, if the input was [1,3,5,7] then return False, because every element of the list is distinct.

def contains_duplicate(input)-> bool:
    return len(input) != len(set(input))

tests = [
    ([1, 3, 5, 7, 1], True),
    ([1, 3, 5, 7], False),
    ([1, 2, 3, -1, 0 , 1, 2], True)
]

for t in tests:
    a = contains_duplicate(t[0])
    assert a == t[1], (t,a)