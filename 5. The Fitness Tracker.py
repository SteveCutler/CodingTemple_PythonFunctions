# Objective:
# The aim of this assignment is to create a program that tracks fitness activities and calories burned.

# Task 1: Develop a function to log different fitness activities and 
# their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] 
# and duration = [10, 20, 15] where Dancing corresponds 
# to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

def exerciseTracker(**kwargs):
    for exercise, duration in kwargs.items():
        print(f"You did {exercise} for {duration} minutes!")


exerciseTracker(Running ='10', Swimming='20', Biking='30', Weights = '25')



# Task 2: Write a simple function that estimates calories burned based on the 
# activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5

caloriesBurned = 0

def exerciseTracker(**kwargs):
    global caloriesBurned
    for exercise, duration in kwargs.items():
        print(f"You did {exercise} for {duration} minutes!")
        caloriesBurned += (int(duration) * 3.5)


exerciseTracker(Running ='10', Swimming='20', Biking='30', Weights = '25')
print(f"that's a lot of exercise! You burned around {caloriesBurned} calories!")



# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

caloriesBurned = 0

def exerciseSummary(**kwargs):
    global caloriesBurned
    for exercise, duration in kwargs.items():
        print(f"You did {exercise} for {duration} minutes!")
        caloriesBurned += (int(duration) * 3.5)
    print(f"That's a lot of exercise! You burned around {caloriesBurned} calories today!")


exerciseSummary(Running ='10', Swimming='20', Biking='30', Weights = '25')

