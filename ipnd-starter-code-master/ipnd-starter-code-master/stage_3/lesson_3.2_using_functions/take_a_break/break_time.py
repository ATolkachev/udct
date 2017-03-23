# Lesson 3.2: Use Functions
# Mini-Project: Take a Break
import webbrowser
import time
# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
def time_for_break():
    webbrowser.open("http://google.com")
    time.sleep(4)
    time_for_break()

time_for_break()
