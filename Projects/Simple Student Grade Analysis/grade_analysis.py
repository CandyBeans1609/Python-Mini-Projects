from functools import reduce

students = [
    {"name":"Ross" , "grades":45},
    {"name":"Rachel" , "grades":87},
    {"name":"Monica" , "grades":70},
    {"name":"Chandler" , "grades":69},
    {"name":"Joey" , "grades":96},
    {"name":"Richard" , "grades":74},
    {"name":"Susan" , "grades":58},
    {"name":"Carol" , "grades":66},
    {"name":"Phoebe" , "grades":83},
]

# Extract grades using map
grades = list(map(lambda x: x['grades'], students))

# Calculate the total grades using reduce
total_grades = reduce(lambda acc, x: acc + x, grades, 0)

average_grade = total_grades / len(grades)

threshold = 80
students_above_threshold = list(filter(lambda x: x['grades'] > threshold, students))

# Sort students by grades in descending order
sorted_students = sorted(students, key=lambda x: x['grades'], reverse=True)

print(f"Average Grade: {average_grade}\n")
print("Students Above Threshold:\n")
for student in students_above_threshold:
    print(student)
print("\nSorted Students by Grade:\n")
for student in sorted_students:
    print(student)
