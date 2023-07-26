#Day 2 Interactive Excercises

#Excercise 1 - Data Types - Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Answer:

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
print(int(two_digit_number[0]) + int(two_digit_number[-1]))
####################################
#Write your code below this line 👇


#Exercise 2 - BMI Calculator - Write a program that calculates the Body Mass Index (BMI) from a user's weight and height (as a whole number)

#Answer

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
print(int(float(weight) / float(height) ** 2))
#Write your code below this line 👇


#Exercise 3 - Life in Weeks

#Answer

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
total_time_remaining = 90 - int(age)

months_remaining = total_time_remaining * 12
weeks_remaining = total_time_remaining * 52
days_remaining = total_time_remaining * 365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

#Write your code below this line 👇

#Day 2 Project: Tip Calculator

#Answer

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip/100)
cost_per_person = total_bill / people
print(round(cost_per_person, 2))
