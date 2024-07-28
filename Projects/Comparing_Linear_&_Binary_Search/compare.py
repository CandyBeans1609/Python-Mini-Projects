import random
import time

def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return True
    return False

def binary_search(lst, key, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    if lst[mid] == key:
        return mid
    elif key > lst[mid]:
        return binary_search(lst, key, mid + 1, high)
    else:
        return binary_search(lst, key, low, mid - 1)

# Generate a list of random integers
length = 100
lst = random.sample(range(-200, 200), length)  
sorted_list = sorted(lst)  
print("Sorted List:", sorted_list)

key = 7
if key not in sorted_list:
    # If key is not in the list, add it for searching
    sorted_list.append(key)
    sorted_list = sorted(sorted_list)  # Re-sort the list after adding the key

# Linear Search Timing
print("\nLinear Search:")
start = time.time()
linear_search(sorted_list, key)
end = time.time()
print(f"Search time for Linear Search: {(end - start):.6f} seconds")

# Binary Search Timing
print("\nBinary Search:")
start = time.time()
binary_search(sorted_list, key, low=0, high=len(sorted_list) - 1)
end = time.time()
print(f"Search time for Binary Search: {(end - start):.6f} seconds")
