# example.py - Python. Run it:  python3 example.py   (Windows: python example.py)
# Same program as example.js. Compare the two side by side.

# variables
name = "Asha"
age = 21
is_student = True            # True / False

# f-string
print(f"{name} is {age}")

# if / elif / else, and / or / not
if age >= 18 and is_student:
    print("Adult student")
elif age >= 18:
    print("Adult")
else:
    print("Minor")

# for loop
for i in range(3):
    print(i)

# function
def add(a, b):
    return a + b

print(add(3, 4))

# list and dict
fruits = ["apple", "mango"]
person = {"name": "Asha", "city": "Toronto"}
print(fruits[0], person["city"])

# == compares values
print(5 == 5)
