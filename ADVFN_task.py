''' Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the 
map() function with a lambda function to implement this.'''
# def square_all(numbers):
#     return list(map(lambda a:a**2,numbers))

# num=list(map(int,input("enter your numbers: ").split()))
# res=square_all(num)
# print("result of squares:",res)


'''Write a Python function 
filter_positive(numbers) that takes a list of numbers 
as input and returns a new list containing only the positive numbers from 
filter() function with a lambda function to implement the input list. Use the this.'''

# def filter_positive(numbers):
#     return list(filter(lambda a:a>0,numbers))

# num=list(map(int,input("enter your numbers : ").split()))
# res=filter_positive(num)
# print("positive numbers : ",res)


''' Write a Python function 
calculate_factorial(n) that calculates the factorial of a given number n. Use the reduce() function with an appropriate lambda function to implement this.'''

# from functools import reduce

# def calculate_factorial(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return reduce(lambda a, b: a * b, range(1, n + 1))

# # Example usage:
# num = int(input("Enter a number: "))
# result = calculate_factorial(num)
# print(f"Factorial of {num} is: {result}")

''' Write a Python function 
count_vowels(string) that takes a string as input and 
returns the count of vowels (a, e, i, o, u) in the input string. Use the 
function with an appropriate lambda function to implement this'''
# def count_vowels(string):
#     vowels="aeiouAEIOU"
#     return len(list(filter(lambda char:char in vowels,string)))
# text=input("Enter a string: ")
# res=count_vowels(text)
# print("Number of elemenxt in list :",res)

