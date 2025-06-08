'''1.Create a Tuple Write a program that creates a tuple containing three 
elements: your name, your age, and your favorite color. Then print the tuple'''
# name=input("enter your name: ")
# age=int(input("Enter your age :"))
# color=input("Enter your favouite color : ")

# my_tuple=(f" my name is {name} my age is {age} and favourite color is {color}" )
# print(my_tuple)

''' 2.Access Tuple Elements Write a program that creates a tuple containing the 
days of the week. Then, print the third element of the tuple'''

# weeks=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
# print("the third element from the list :",weeks[2])

'''3. Tuple Concatenation Write a program that creates two tuples, one 
containing odd numbers from 1 to 5 and another containing even numbers 
from 2 to 6. Concatenate these two tuples and print the result.'''
# new=(1,2,3,4,5,6)
# new1=new[0:6:2]
# new2=new[1:7:2]
# # print(new1)
# # print(new2)
# new3=new1+new2
# print(new3)

'''4.Tuple Unpacking Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle'''

# input=(23,35)
# lenght=input[0]
# width=input[1]
# area=lenght*width
# print(area)

'''5.Check if an Element Exists Write a program that checks if a given element 
exists in a tuple.'''

# tuple=(1,2,34,2,426,5,27,5754,3,73,'reddy')
# word=input("enter your word or number:")
# # Try converting input to int
# try:
#     element=int(word)
# except ValueError:
#     element=word
    
# print(element in tuple)


''' Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items
 Sample Input:
 items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
 Sample Output:
 Item
 Price-------------------
Apple
 99.00
 Banana 99.00
 Milk
 49.00-------------------
Total
 247.0 '''
 
dict = [("Apple", 99.00), ("Banana", 99.00), ("Milk", 49.00)]

print("Item\tPrice")
print("-"*30)

total=0
for i,j in dict:
    print(f"{i}\t {j:.2f}")
    total +=j
    
discount=(10/100)*total
final=total-discount
print("-"*30)
print(f"Total      {final:.2f}")




