# Day 1 Interactive Excercises

#Exercise 1 - Printing - Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


#Exercise 2 - Debugging Practice - Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


#Exercise 3 - Input Function - Write a program that prints the number of characters in a user's name.

print(len(input("what is your name?")))


#Exercise 4 - Variables - Write a program that switches the values stored in the variables a and b.


# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#Day 1 Project: Band Name Generator

#1. Create a greeting for your program.
print("Hello Musician!")
print("Tell me about yourself!")

#2. Ask the user for the city that they grew up in.
hometown = input("""What city are you from?
""")

#3. Ask the user for the name of a pet.
pet = input("""What was the name of your first pet?
""")

#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + hometown + " " + pet)

#5. Make sure the input cursor shows on a new line: