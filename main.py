
import os
import random
import numbers

compiling_list = {}
total_rounds = 0
nums = []
n = 1
while n <= 70:
    nums.append(n)
    compiling_list[n] = 0
    n += 1
# print(nums)
# print(compiling_list)
round = 0
while round < 100:
    x = 0
    while x < 5:
        rand = random.choice(nums)
        popped = nums.pop(rand - 1)
        nums.insert(rand - 1, 0)
        if popped == 0:
            continue
        compiling_list[popped] += 1
        x += 1
    round += 1


print(compiling_list)
# # Randomly choose 5 numbers from list
# chosen = []
# while len(chosen) < 5:
#     chosen.append(random.choice()
    # rand = random.choice(list)
    # chosen.append(list.pop([random.choice(list)]))
# print(chosen)
# # finding the percentage of times drawn...
# while total_rounds <= 1000:
#     list = balls_chosen()
#     total_rounds += 1
#     for x in list:
#         compiling_list[x] = ((compiling_list(x) + 1)/total_rounds).round(2)
