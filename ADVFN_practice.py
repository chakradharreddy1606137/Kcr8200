# lambda arg:expressions

# def square(a,b):
#     return a*b
# res=square(4,6)
# print(res)

# res=lambda a,b:a*b
# print(res(5,10))

# def multiplication(a,b):
#     return a*b
# res=multiplication(4,5)
# print(res)

# res=lambda a,b:a*b
# print(res(5,5))

# print even numbers from list
# list_1=[1,2,35,133,546,6,7,8,9,10,12,15,16,89]
# empty_list=[]
# for i in list_1:
#     if i%2==0:
#        empty_list.append(i)
# print(empty_list)
   
'''filter'''
# list_1=[1,2,35,133,546,6,7,8,9,10,12,15,16,89]
# res=filter(lambda a:a%2==0,list_1)
# print(list(res))

'''squares of a list'''
# list_1=[1,2,35,133,546,6,7,8,9,10,12,15,16,89]
# res=map(lambda a:a*a,list_1)
# print(list(res))

'''reduce '''
'it gives only one result '
# from functools import *
# list_1=[1,2,35,133,546,6,7,8,9,10,12,15,16,89]
# d=reduce(lambda a,b:a+b**2,list_1)
# print(d)
# d=reduce(lambda a,b: a+b,[23,21,45,98])
# print(d)

'''generator'''

# def fun():
#     yield 1
#     yield 2
#     yield 3
# x=fun()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

    
