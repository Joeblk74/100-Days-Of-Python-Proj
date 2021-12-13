#String Manipulation
print("Hello" + " " + "Andrew")
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
input("What is your name?")
#The Python Input Function
print (len(input ("What is your name?")))
#Python Variables
name = "Jack"
print(name)

name = "Andrew"
print(name)


name = input("What is your name?")
length = len(name)
print(length) 

#1.4 Excercise
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

print("Welcome to the Band Name Generator!")
name_one = input("What is the name of the city you grew up in?\n")
name_two = input("What is the name of your favorite pet?\n")
band_name = name_one + " " + name_two
print("Congratulations! Your new band name is " + band_name)