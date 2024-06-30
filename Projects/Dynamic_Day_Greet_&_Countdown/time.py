import time

name=input("Enter your name")

from time import strftime

curr_time=time.strptime("%H:%M:%S")
hour=int(time.strftime("%H"))
if (hour>=12 and hour<18):
    print("Good Afternoon ",name)
elif(hour<12):
    print("Good Morning ",name)
else:
    print("Good Night ",name)
