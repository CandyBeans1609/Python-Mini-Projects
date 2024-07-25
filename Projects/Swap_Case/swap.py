swapped=[]
def swap(s):
    for char in s:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)
    return ''.join(swapped)
    

s=input("Enter a string: ")
print("\nInput string:  ",s)
print("Output string: ",swap(s))
