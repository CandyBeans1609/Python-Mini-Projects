arr1 = [[1, 2],
        [3, 4]]
arr2 = [[0, 3],
        [1, 2]]
result = [[0, 0], 
         [0, 0]]

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

print("arr1 :")
print_matrix(arr1)

print("arr 2:")
print_matrix(arr2)

for i in range(len(arr1)):  
    for j in range(len(arr1[0])):  
        result[i][j] = arr1[i][j] + arr2[i][j]

print("Result of arr1 + arr2:")
print_matrix(result)
