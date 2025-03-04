grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
grades["David"] = 88
del grades["Charlie"]

print("Initial Grades:", grades)



for name, grade in grades.items():
    print(f"Name: {name}")
    print(f"Grade: {grade}")

# for name, grade in grades:.items():
   # print(f"Name: {name}\tGrade: {grade}")