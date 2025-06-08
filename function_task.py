'''Task 1: Add Function
 Write a Python function named add that takes two arguments a and 
b and 
returns their sum.
 
 '''

# def add(a,b):
#     return a+b
# num1=int(input("enter your 1st number : "))
# num2=int(input("enter your second number: "))
# obj=add(num1,num2)
# print(obj)

"oR "
# def add(a,b):
#     print(a+b)
# num1=int(input("enter your 1 number: "))
# num2=int(input("enter your 2 nd number: "))
# add(num1,num2)

'''Task 2: Square Function'''
'''Write a Python function named square that takes a number x as input and returns its square.'''
# def square(a):
#     return a*a
# num1=int(input("enter your number: "))
# print(square(num1))

'''Task 3: Factorial Function
Write a Python function named factorial that takes a positive integer   
input and returns its factorial
'''

# def factorial(a):
#     mul=1
#     for i in range(1,a+1,1):#like the array starts with0 so i take from 1 onwarss
#         mul*=i
#     return mul
      
# number=int(input("enter your required number: "))
# b=factorial(number)
# print(f"the factorail of your number is {b}")


        


'''Task 4: Maximum Function
 Write a Python function named maximum that takes a list of numbers as input and 
returns the maximum value in the list.'''

# numbers=[1,2,9,23,32436,462,62,5,54445,6346,]
# def maximum(numbers):
#     return max(numbers) if numbers else None

# a=maximum(numbers)
# print(a)

" here the user input  and link compreshion split is used to split the numbers "

# def maximun(numbers):
#     return max(numbers)

# nums=input("enter numbers: ").split()
# nums=[int(x) for x in nums]

# print("max",maximun(nums))



'''Task 5: Reverse Function
 Write a Python function named reverse that takes a string returns its reverse'''

# def reverse(name):
#     return name[::-1]

# kid=input("enter your name::") 
# a=reverse(kid)
# print(a)
   

'''Task 6: Check Prime Function'''
'''write a python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise false'''
 
# from sympy import *#install sympy 'pip install sympy'

# def is_prime(n):
#     return isprime(n)

# num=int(input("enter a postive number: "))
# if is_prime(num):
#     print(f"{num} true  is a prime number ")
# else:
#     print(f"{num} False it is not a prime number ")


'''Task 7: Fibonacci Function
 Write a Python function named fibonacci and returns the fibonacci that takes a positive integer n as 
n th Fibonacci number.'''



# def fibonacci(num):
#     a=0
#     b=1
#     for i in range(num-1):
#       c=a+b
#       a=b
#       b=c
      
#     return c
# n=int(input("enter your number: "))
# fibo=fibonacci(n)
# print(fibo)

'''Task 8: Palindrome Function'''
'''Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome,otherwise False  '''

# def is_palindrome(s):
#     return s == s[::-1]

# # Example usage
# text = input("Enter a string: ")
# if is_palindrome(text):
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")

    

'''Task 9: Sum of Squares Function'''
''' Write a Python function named  sum_of_squares that takes a list of numbers as 
input and returns the sum of the squares of those numbers.'''
" here the sum of squares is for first n numbers"
# def sum_of_squares(num):
#     sum=0
#     for i in range(num+1):
#         sum=sum+(i**2)
#     return sum

# s=sum_of_squares(5)
# print(s)

" insert into a list and later find sum of squares"

# def sum_of_squares(numbers):
#     return sum(x**2 for x in numbers)
# nums=input("enter the numbers: ").split()
# nums=[int(x) for x in nums]
# print("sum of squares is :",sum_of_squares(nums))


'''Task 10: Average Function'''
'''Write a Python function named average that takes a list of numbers as input and returns the average value.'''
# def average(numbers):
#     return sum(numbers)/len(numbers)

# nums=input("enter your numbers :").split()
# nums=[int(x) for x in nums]
# print("Average: ",average(nums))