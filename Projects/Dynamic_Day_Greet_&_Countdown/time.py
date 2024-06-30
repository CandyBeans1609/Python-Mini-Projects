import time

name = input("Enter your name: ")

from time import strftime

curr_time = strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

if hour >= 12 and hour < 18:
    print("Good Afternoon,", name)
elif hour < 12:
    print("Good Morning,", name)
else:
    print("Good Night,", name)

time_parts = curr_time.split(':')
hours = int(time_parts[0])
minutes = int(time_parts[1])
seconds = int(time_parts[2])
total_seconds = hours * 3600 + minutes * 60 + seconds

print("\nComplete your tasks before the day runs out!!")

while total_seconds > 0:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    timer = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(timer, end="\r")
    time.sleep(1)
    total_seconds -= 1

print("\nTime's up! Complete your tasks now!!")
