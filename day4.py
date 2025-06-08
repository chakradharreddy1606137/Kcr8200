'''5. Identity operators'''
# a=[1,2,3]
# b=a
# c=[1,2,3]
# print(a is b)
# print(b is a)
# print(b is not c)
# print(a is not c)

'''6.Membership operators'''
# my_list=[1,2,3,4,5,6,8]
# print(3 in my_list)
# print(10 in my_list)

# my_data=8200
# con_str=str(my_data)
# print(con_str)
# print(id(con_str))
# print(type(con_str))
# print(f"my data is {my_data}and the cponversion is {con_str}")


'''Create a program that takes user input for their name and age. 
 Use formatted strings (f-strings) to print a message welcoming the user and
  stating their age.'''
# name=input("Enter your good name :")
# age=int(input("Enter your age: "))
# print(f"welcome the user :{name} and stating their age is {age}")

'''Create a list called 
numbers that contains integers from 1 to 10
Check if the number 5 is in the list.
 Check if the number 15 is not in the list.'''
 
# my_numbers=[1,2,3,4,5,6,7,8,9,10]

# print(5 is my_numbers)
# print(15 is not my_numbers)

'''Coding Exercise:'''
''' Write a Python program to calculate the area of a rectangle using the given 
formula: 
area = length * width . Take the values of length and width as inputs from 
the user.'''
# rec_length=int(input("Enter rectangle length:"))
# rec_width=int(input("Enter your rectangle width:"))
# area= rec_length*rec_width
# print(f"length of the rectangle is :{rec_length} and width of the rectangle :{rec_width} and area of the rectangle is :{area}")


'''Write a Python program to demonstrate incrementing and decrementing a variable'''

# my_data=int(input("Enter your data in the following space:"))
# my_data+=1
# print(my_data)
# my_data-=1
# print(my_data)
# my_data*=3
# print(my_data)
'''Exercise 3: Write a Python program to convert temperature from Celsius to Fahrenheit. The 
formula for conversion is: 
F = (C * 9/5) + 32 . Take the temperature in Celsius as nput from the user.'''

# tem_cel=float(input("enter your temperature in Celsius(C):"))
# F=(tem_cel*9/5)+32
# print(f"temperature in celsius is {tem_cel} the conversion is {F}")


'''    Exercise 4:   Write a Python program to calculate the simple interest given the principal 
amount, rate, and time (in years).'''
# amount=int(input("Enter your amount :"))
# rate=float(input("Enter your rate: ") )
# time=float(input("Enter your time in years: "))
# simple_interest=(amount*rate*time)/100
# print(f"amount {amount} rate is {rate} and time {time} and simple interest {simple_interest}")

'''Exercise 5: '''
'''Write a Python program to concatenate two strings and display the result. The 
strings should be taken as input from the user
'''

# start_name=input("Enter your starting name : ")
# middle_name=input("enter your middle name: ")
# last_name=input("Enter your last name: ")
# name=start_name+middle_name+last_name
# print(f"name is {name}")


''' Exercise 6:'''
''' Write a Python program to convert a distance from kilometers to miles.'''
# dis=float(input("Enter your total distance in km:"))
# con_mil=dis*0.621371
# print(f"dis is {dis} and the conversion is {con_mil}  ")
