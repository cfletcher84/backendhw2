# Decisions at the Crossroad

number = input("Enter a number: ")
number_int = int(number)

if number_int > 0:
    print("The number is positive.")
elif number_int == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# The Greatest Showdown
# Task 1

num1 = input("Please enter number one. : ")
num2 = input("Please enter number two. : ")
num3 = input("Please enter number three. : ")
num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

if num1_int > num2_int and num1_int > num3_int:
    print("The highest number is ", num1)
elif num2_int > num1_int and num2_int > num3_int:
    print("The highest number is ", num2)
elif num3_int > num2_int and num3_int > num1_int:
    print("The highest number is ", num3)

# Task 2
    
num1 = input("Please enter number one. : ")
num2 = input("Please enter number two. : ")
num3 = input("Please enter number three. : ")
num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

if num1_int > num2_int and num1_int > num3_int:
    print("The highest number is ", num1)
elif num2_int > num1_int and num2_int > num3_int:
    print("The highest number is ", num2)
elif num3_int > num2_int and num3_int > num1_int:
    print("The highest number is ", num3)
if num1_int < num2_int and num1_int < num3_int:
    print("The lowest number is ", num1)
elif num2_int < num1_int and num2_int < num3_int:
    print("The lowest number is ", num2)
elif num3_int < num2_int and num3_int < num1_int:
    print("The lowest number is ", num3)
    
# Task 3

num1 = input("Please enter number one. : ")
num2 = input("Please enter number two. : ")
num3 = input("Please enter number three. : ")
num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

if num1 == num2 and num2 == num3:
    print("All of your numbers are the same!")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two of your numbers are the same!")
if num1_int > num2_int and num1_int > num3_int:
    print("The highest number is ", num1)
elif num2_int > num1_int and num2_int > num3_int:
    print("The highest number is ", num2)
elif num3_int > num2_int and num3_int > num1_int:
    print("The highest number is ", num3)
if num1_int < num2_int and num1_int < num3_int:
    print("The lowest number is ", num1)
elif num2_int < num1_int and num2_int < num3_int:
    print("The lowest number is ", num2)
elif num3_int < num2_int and num3_int < num1_int:
    print("The lowest number is ", num3)
    
# Leap Year Explorer

user_year = input("What is the year? : ")
year_int = int((user_year))

if year_int %  4 == 0 and not year_int % 100 == 0 or year_int % 400 == 0:
    print("This is a leap year!")
elif year_int % 4 == 0 and year_int % 100 == 0:
    print("This is not a leap year!")
