#Average
print("Enter student marks")
student_marks = input().split()

#convert to int
for index in range(0, len(student_marks)):
    student_marks[index] = int(student_marks[index])

#total marks
total_marks = 0
for mark in student_marks:
    total_marks += mark
student_count = len(student_marks)
avg = int(total_marks/student_count)
print(f"No, of students: {student_count} and total marks : {total_marks} and average marks : {avg}")
