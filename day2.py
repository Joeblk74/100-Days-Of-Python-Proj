#Data Types

#String

print("Hello"[4])

print("123" + "345")

#Integer

print(123 + 345)

123_456_789

#Float

3.14159

#Boolean

True
False

# num_char = len(input("what is your name?"))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+ str(100))

two_digit_number = input("Type a two digit number: ")

print(type(two_digit_number))
# two_digit_int = int(two_digit_number)
# print(two_digit_int)
a = two_digit_number[0]
b = two_digit_number[1]
print(int(a) + int(b))

#Mathmatical Operations

3 + 5
7 - 4
3 * 2
6 / 3
# Exponents
2 ** 2

# PEMDASLR
# ()
# **
# * /
# + -
# 3 *

print(3 + 3 + 3 - 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)
