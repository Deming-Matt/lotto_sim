import os
import random

# Generate 65 numbers in a list
def num_gen(number_of_balls):
    nums = []
    n = 1
    while n <= number_of_balls:
        nums.append(n)
        n += 1
    # print(nums)
    return nums

num_gen(70)
