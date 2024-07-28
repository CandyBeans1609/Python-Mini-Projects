import random
import time

def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binary_search(lst, key, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(lst) - 1

    if high < low:
        return -1

    mid = (low + high) // 2
    if lst[mid] == key:
        return mid
    elif key < lst[mid]:
        return binary_search(lst, key, low, mid - 1)
    else:
        return binary_search(lst, key, mid + 1, high)

length = 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3 * length, 3 * length))
sorted_list = sorted(list(sorted_list))

print("\nLinear Search:")
start = time.time()
for target in sorted_list:
    linear_search(sorted_list, target)
end = time.time()
print("Linear search time: ", (end - start), "seconds")

print("\nBinary Search:")
start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print("Binary search time: ", (end - start), "seconds\n")
