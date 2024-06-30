import time

name = input("Enter your name: ")

# Get current time in local time
current_time = time.localtime()
hour = current_time.tm_hour

# Determine appropriate greeting based on the current hour
if hour >= 12 and hour < 18:
    print(f"Good Afternoon, {name}!")
elif hour < 12:
    print(f"Good Morning, {name}!")
else:
    print(f"Good Night, {name}!")

# Calculate remaining seconds until the end of the day
current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
remaining_seconds = 86400 - current_seconds  # 86400 seconds in a day

print("\nComplete your tasks before the day runs out!!")

# Display countdown timer
while remaining_seconds > 0:
    hours = remaining_seconds // 3600
    minutes = (remaining_seconds % 3600) // 60
    seconds = remaining_seconds % 60

    timer = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(timer, end="\r")
    time.sleep(1)
    remaining_seconds -= 1

print("\nTime's up! Complete your tasks now!!")
