# Student Details
name = "Navya"
m1 = 85
m2 = 90
m3 = 75

# Arithmetic Operators
total = m1 + m2 + m3
average = total / 3
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

# Comparison Operators
print("Passed:", average >= 40)
print("Excellent:", average >= 90)

# Assignment Operators
bonus = 0
bonus += 5
bonus *= 2
print("Bonus:", bonus)

# Logical Operators
if average >= 40 and average <= 100:
    print("Student Passed")

if average >= 75 or bonus >= 10:
    print("Good Performance")

if not average < 40:
    print("Eligible for Next Semester")

# Identity Operators
x = 10
y = 10
print(x is y)
print(x is not y)

# Membership Operators
subjects = ["Python", "Java", "DBMS"]
print("Python" in subjects)
print("C" not in subjects)

# Bitwise Operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)

# Conditional Statement
if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 40:
    print("Grade C")
else:
    print("Fail")