# You are given an integer array nums, where each element in it is a single digit (0-9).

# The triangular sum of nums is the value of the only element present in nums after the following process terminates:

#     Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new integer array newNums of length n - 1.
#     For each index i, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes the modulo operator.
#     Replace the array nums with newNums.
#     Repeat the entire process starting from step 1.

# Return the triangular sum of nums.
def triangular_sum(nums):
    n = len(nums)
    new_nums = []
    if n == 1:
        return nums[0]
    for i in range(n-1):
        new_nums.append((nums[i] + nums[i+1]) % 10)
    return triangular_sum(new_nums)

tests = [
	([1,3,5,7], 2),
	([9,7,5,3], 8),
    ([2], 2),
	([1,9], 0),
	([9,8,7,6,5,4,3,2,1], 0)
]
for t in tests:
    x, y = t
    assert triangular_sum(x) == y, y