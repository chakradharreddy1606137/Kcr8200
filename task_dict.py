''' Write Python code to add a new key-value pair to the following dictionary:
 my_dict = {'name': 'python', 'age': 25}
 # Your code here
 # Output should be: {'name': 'python', 'age': 25, 'city': 'we
 st godavari'''

# my_dict={
#     'name':'python',
#      'age':'25',
# }

# my_dict['city']='i am from vijayawada'
# print(my_dict)

''' Task 2: Dictionary Access
 Write Python code to access and print the value associated with the key 'price' in 
the following dictionary:'''


# product_info={
#     'name':'Laptop',
#     'brands':'Dell',
#     'price':'1200',
    
# }
# e=product_info.get('price')
# e=product_info['price']
# print(e)

'''Task 3: Dictionary Removal
 Write Python code to remove the key-value pair with the key 'city' from the 
following dictionary:'''

my_dict={
    'name':'python',
    'age':'30',
    'city':'Bhimavaram',
    
    }

# my_dict.pop('city')
del my_dict['city']
print(my_dict)

''' Task 4: Dictionary Keys
 Write Python code to print all the keys present in the following dictionary'''

# my_dict={
#     'name':'python',
#     'age':'25',
#     'city':'Vijayawda',
    
# }
# e=my_dict.keys()
# print(e)


''' Task 5: Dictionary Values
 Write Python code to print all the values present in the following dictionary:'''

# my_dict={
#     'name':'chakradharreddy',
#     'age':'21',
#     'city':'Vijayawada',
    
# }
# e=my_dict.values()
# print(e)


''' Exercise 1: Dictionary Update
 Write a Python script that updates a dictionary with a new key-value pair'''
 
# my_dict={
#     'name':'chakradharreddy',
#     'age':'21',
#     'city':'vijayawada',
    
# }
# new_key=input("Enter your new key:")
# new_value=input("Enter your new value: ")
# my_dict['currency']='indian'

# my_dict[new_key]=new_value

# print(f"updated dictionary is {my_dict}")

'''Exercise 2: Dictionary Access
 Write a Python script that accesses and prints the value associated with a specific 
key in a dictionary'''

# my_dict={
#     'name':'KCr',
#     'age':'21',
#     'height':'170cm',
#     'city':'vijayawada',
#     'clg':' VNIT',
    
# }
# name=input("enter your name:")

# print(my_dict.get(name))#if not found in get it will give us None


''' Exercise 3: Dictionary Removal
 Write a Python script that removes a key-value pair from a dictionary.'''
 
# my_dict={
#     'name':'K CH reddy',
#     'age':'21',
#     'city':'Vijayawada',
#     'clg':'Nagpur',
    
    
# }
# given_name=input("Enter your specificed name :")
# if given_name in my_dict:
#     my_dict.pop(given_name)
#     print(f"{given_name} has been removed")
# else:
#     print(f"{given_name} not found in  the dictionary")
    

# print("upadetd dictionaty ",my_dict)