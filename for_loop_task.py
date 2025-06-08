# for i in range(-10,0):
#     print(i)

# for i in range(1,20):
#     print(f"2 X{i} = {i*2}")
    
# for i in range(17,240):
#     print(f"17X {i}={i*17}")

# num=int(input("Enter your number :"))
# for i in range(2,19):
#     print(f"{num}X{i}={i*num}")
'''Exercise 1: Sum of Squares'''
'''  Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a  for loop'''
# s=0
# for i in range(1,6):
#     i=i**2
#     s+=i
    
#     print(f"the sum of square s :{s}") 
   
''' Exercise 2 Countdown'''
''' Write a Python program that uses a 
while loop to print a countdown from 5 to 1.'''

# i=5
# while i>0:
#     print(i)
#     i-=1
    
''' Multiplication Table with Nested For Loop
 Write a Python program to print the multiplication table for a user-specified 
number using a nested for loop'''

# num=int(input("enter your multiply number: "))

# for i in range(1,11):
#     for j in range(1,2):
#         print(f"{num}X{i}={num*i}")
        
'''  Exercise 4 
Write a Python program that uses a "for" loop to find the sum of all even 
numbers between 0 and 10 (inclusive). '''

# s=0
# for i in range(1,10):
#     if i%2==0:
#         print(i)
#         s+=i
# print(s)
'''   Exercise 5
 Calculate the sum of all numbers from 1 to a given number'''
 
'''for loop'''
# num=int(input("Enter your number:"))
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum) 

'''while loop'''
# num=int(input("Enter your number:"))
# count=1
# sum=0
# while(count<=num):
#     sum+=count
#     count+=1
# print(sum)

''' Exercise 6
 Display numbers from a list using loop'''
# list=[1,2,3,4,5,6,34,43,52]
# for i in list:
#     print(i)

'''Exercise 7
 Display numbers from 10 to 1 using for loop'''

# for i in range(-10,0):
#     print(i)
    
''' Exercise 8 
Write a Python program to print the cube of all numbers from 1 to a given 
number'''

# num=int(input("enter your number:"))
# res=0
# for i in range(1,num+1):
#     res=i**3
#     print(res)
    
