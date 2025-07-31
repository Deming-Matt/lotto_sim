import os
import random
import time
# import numbers

# Global variables/dictionaries
compiling_list = {} # Dictionary of all the possible numbers to be drawn, value = number of times drawn
pb_list = {} # Dictionary of power balls to be drawn
total_rounds = 0

n = 1
while n <= 70: #Create dictionary on numbers
    compiling_list[n] = 0
    n += 1

pb = 1
while pb <= 26: #Create Power ball numbers dictionary
    pb_list[pb] = 0
    pb += 1

def num_gen(number_of_balls):
    nums = []
    n = 1
    while n <= number_of_balls: # ''' Create list of balls to be drawn from '''
        nums.append(n)
        n += 1
    return nums

def power_ball(number_of_balls):
    nums = []
    n = 1
    while n <= number_of_balls:
        nums.append(n) # ''' Create powerball list to get random number '''
        n += 1
    return nums

# Randomly choose 5 numbers from list
def balls_chosen():
    list = num_gen(70)
    # ''' Create the list of balls '''
    chosen = []
    while len(chosen) < 5:
    # ''' Loop to pick the balls chosen for that round '''
        rand = random.choice(list)
        if rand == 0:
            # ''' If a 0 is drawn, that "ball" has already been choosen '''
            continue
        chosen.append(list.pop(rand - 1))
        # ''' Move the ball out of the available balls left to be chosen '''
        list.insert(rand - 1, 0)
        # ''' Replace the ball chosen with a 0 '''
    return chosen

def power_ball_chosen():
    list = power_ball(26)
    rand = random.choice(list)
    return int(rand) # ''' Choose a powerball for the round '''

# finding the percentage of times drawn...
def probabilties_of_chosen():
    global total_rounds
    global compiling_list
    global pb_list
    round = 1
# Creates a "drawing" of numbers and a powerball, and adds them to the
# totals(values) of the corresponding dictionaries.
    while round <= 1000:
        list = balls_chosen()
        power_ball = power_ball_chosen()
        pb_list[power_ball] += 1 # Not doing more than one round??
        round += 1
        for x in list:
            compiling_list[x] += 1
    total_rounds += round
    # print(compiling_list)

def percentage_chosen(dict):
    for key, value in compiling_list.items():
        compiling_list[key] = round((value/total_rounds) * 100, 2)
    for key, value in pb_list.items():
        pb_list[key] = round((value/total_rounds) * 100, 2)

def rank(dictionary):
    sorted_by_values_desc = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_by_values_desc.items():
        print(f"{key}: {dictionary[key]}%")

start_time = time.time()
# '''
# Runs the probabilty generator 1000 times with each round having
# 1000 rounds for a total of one million rounds. If another zero is
# added to either set of rounds the amount of time to process is multiplied
# by 10.
# '''
r = 0
while r < 1000:
    probabilties_of_chosen()
    r += 1

# os.system("clear")
print(compiling_list)
print(total_rounds)
percentage_chosen(compiling_list)
print("Number Rankings: ")
rank(compiling_list)
print("Powerball Rankings: ")
rank(pb_list)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"***{elapsed_time:.4f} seconds")
