print("========== STUDENT GRADE CALCULATOR ==========")

name = input("Enter Student Name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n========== RESULT ==========")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
