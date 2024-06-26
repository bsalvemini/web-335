"""
Author: Brandon Salvemini
Date: 6/25/2024
File Name: Salvemini_lemonadeStandSchedule.py
Description: Python program that outputs a schedule for a lemonade stand
"""

# List of tasks
tasks = ["Purchase supplies", "Make Lemonade", "Set up stand", "Sell Lemonade", "Clean up"]

# for loop to iterate over each task in the tasks list
for task in tasks:
  print(task) # Print the task

# Extra print statement to put a blank line after the last task
print()

# List of week days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# for loop to iterate over each week day in the days list
for day in days:
  if day == "Saturday" or day == "Sunday": # If day is Saturday or Sunday
    print(f"{day}: It's a day off. You should rest.") # Print day off message
  elif day == "Monday": # If day is Monday
    print(f"{day}: {tasks[0]}") # Print the week day and the task for that day from the tasks list
  elif day == "Tuesday": # If day is Tuesday
    print(f"{day}: {tasks[1]}") # Print the week day and the task for that day from the tasks list
  elif day == "Wednesday": # If day is Wednesday
    print(f"{day}: {tasks[2]}") # Print the week day and the task for that day from the tasks list
  elif day == "Thursday": # If day is Thursday
    print(f"{day}: {tasks[3]}") # Print the week day and the task for that day from the tasks list
  elif day == "Friday": # If day is Friday
    print(f"{day}: {tasks[4]}") # Print the week day and the task for that day from the tasks list
