print("🧑‍🎓...Student Percentage Manager...📚")

name = input("Enter Name Of Student :")

marks = []
subject = 3

for i in range(subject):
    marks_es = int(input(f"Enter Marks You abtained in {i+1} Subject :"))
    marks.append(marks_es)


total_marks = sum(marks)

percentage = total_marks/3

if percentage >= 40:
    result = "Pass"

else:
    result = "Fail"

print("------ 📚 Result 📚 ------")
print("Name Of Student :",name)
print("Marks :", marks)
print("Total :",total_marks)
print("Percentage :", percentage)
print("Result :", result)