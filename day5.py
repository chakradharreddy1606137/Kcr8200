# marks=int(input("Enter your marks:"))

# if marks>=90 and  marks <=100 :
#     print(f"you got A grade {marks}")
# elif marks>=80 :
#     print(f"You got B grade {marks}")
# elif marks>=70 :
#     print(f"You got C grade {marks}")
# elif marks>=60 :
#     print(f"You got D grade {marks}")
# elif marks>=50 :
#     print(f"You got E grade {marks}") 
# elif marks>=40 :
#     print(f"You got EE grade {marks}")  
# elif marks<=34 and marks>0:
#     print("you fail in exam")
# else:
#     print("You have entered wrong details")
    
# num=int(input("ENter your number:"))
# print("even") if num%2==0 else print("odd")

''' Exercises:'''
''' Vowel Checker:
1 .Write a Python program that takes a character as input and checks whether 
it is a vowel or not. Use the 
if-else statement'''
# char=input("Enter your character:")
# if char in "aeiouAEIOU":
#     print("its vowel")
# else:
#     print("its not vowels")
# print("Vowels") if char in "aeiouAEIOU" else print("not vowels")
'''Age Group Classification
 Write a program that takes an age as input and classifies the person into 
one of the following age groups:
 Child: 012 years
 Teenager: 1317 years
 Adult: 1864 years
 Senior: 65 years and older'''

# age=int(input("Enter your age:"))
# if age<0:
#     print("its a invalid number")
# elif age<=12 and age>=0:
#     print(f"your a child beacause you age is {age}")
# elif age<=17:
#     print(f"you are a teenager because you age is {age} ")
# elif age<=64:
#     print(f"your are a adult because youre age is {age}")
# else:
#     print(f"you are a senior citizen you're age is {age}")
   
''' 3.Number Classifier:
 Write a program that takes an integer as input and classifies it as positive, 
negative, or zero. Use the 
if-elif-else statement.''' 
# new_numer=int(input("Enter you number:"))
# if new_numer>0:
#     print("its a positive number")
# elif new_numer<0:
#     print("its a negative number")
# else:
#     print("its a zero")

'''4 Leap Year Checker:
 Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400'''
# year=int(input("Enter year :"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(f"its a leap year {year}")
#         else:
#             print("its a not a leap year")
#     else:
#         print(f"its a leap year {year}")
# else:
#     print("its not a leap year")

'''5 .Calculator:
Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation.'''
# num_1=int(input("enter your first number :"))
# num_2=int(input("Enter your second number :"))
# operator=input("enter your operator (+,-,*,/) :")
# if operator=="+":
#     print(num_1+num_2)
# elif operator=="-":
#     print(num_1-num_2)
# elif operator=="*":
#     print(num_1*num_2)
# elif operator=="/":
#     print(num_1/num_2)
# else:
#     print("enter a operator between this (+,-,*,/)")


'''6.Short Hand If:'''
# x=8
# print("even ") if x%2==0 else print("odd")

'''7.Discount Calculator:
 Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as 
input. '''

# original_price=float(input("enter your original price:"))
# discount_percentage=float(input("enter your discount percentage:"))
# dis_amount=(original_price*discount_percentage)/100
# final_price=original_price-dis_amount
# print(final_price)


'''8. BMI Calculator'''
''' Write a program that calculates the Body Mass Index BMI using the 
formula: BMI  weight (kg) / (height (m))^2. The program should take 
weight and height as input'''
# weight=float(input("Enter your weight in kg :"))
# height=float(input("Enter your height in m : "))
# BMI=weight/(height)**2
# print(f"your BMI  is {BMI}")
