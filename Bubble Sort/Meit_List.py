def custom_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if (students[j][3] < students[j+1][3] or 
               (students[j][3] == students[j+1][3] and students[j][1] < students[j+1][1]) or 
               (students[j][3] == students[j+1][3] and students[j][1] == students[j+1][1] and students[j][2] > students[j+1][2]) or 
               (students[j][3] == students[j+1][3] and students[j][1] == students[j+1][1] and students[j][2] == students[j+1][2] and students[j][0] > students[j+1][0])):
                students[j], students[j+1] = students[j+1], students[j]

def make_merit_list(n, student_data):
    custom_sort(student_data)
    for student in student_data[:8]:
        print(student[0])

# Input reading
n = int(input())  # Number of students
students = []
for _ in range(n):
    line = input().strip().split()
    name = line[0]
    height = int(line[1])
    weight = int(line[2])
    iq = int(line[3])
    students.append((name, height, weight, iq))

# Prepare and print the merit list
make_merit_list(n, students)
