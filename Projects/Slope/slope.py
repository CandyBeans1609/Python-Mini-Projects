x1=int(input("Enter first x co-ordinate: "))
y1=int(input("Enter first y co-ordinate: "))

x2=int(input("Enter second x co-ordinate: "))
y2=int(input("Enter second y co-ordinate: "))

print(f'First co-ordinate: ({x1},{y1})')
print(f'Second co-ordinate({x2},{y2})')

slope = (y2-y1)/(x2-x1)
print("The slope is: ",slope)