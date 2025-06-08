'''task-1 
 Write Python code to reverse the order of elements in the given list 
Print the reversed list.'''

# my_list=[10,20,30,40,50,11]
# my_list.reverse()
# new_list=my_list
# print(new_list)
# new_list.append(8)
# new_list=my_list[::-1]


# print(new_list)

''' TASK-2
 Common Elements:
 Given two lists  list1 and 
list2 , find and print the common elements between
them.
'''
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# new_list=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             new_list.append(i)
# print(new_list)


'''Task 3:
 Unique Elements:
 Create a new list 
unique_list containing only the unique elements from the 
given list 
original_list . Print the unique list.'''

# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list=set(original_list)
# new_elem=list(unique_list)
# print(new_elem)

# original_list = [1, 2, 2, 3, 4, 4, 5]
# empty_list=[]
# for i in original_list:
#     if i not in empty_list:
#         empty_list.append(i)
# print(empty_list)

'''Task 4:
 Remove Duplicates:
 Remove duplicate elements from the given list 
without duplicates while preserving the order.
 duplicated_list and print the list 
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
 # Your code here
 # Output should be: [1, 2, 3, 4, 5]'''
 
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# new_list=[]
# for i in duplicated_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

#  Exercise 1: List Concatenation
# Write a Python script that concatenates two lists and prints the result

# list_1=[1,2,3,4,5,6,78,89,90]
# list_2=[23,34,56,46,435,890]
# sum=list_1+list_2
# print(sum)


#  Exercise 2 List Repetition
#  Write a Python script that repeats a list three times and prints the result

# list=[1,2,3,4,5,6,7,9]
# repeat_list=list*3
# print(repeat_list)

''' Exercise 3 List Removal
 Write a Python script that removes the elements at even indices from a list'''


# list=[1,2,3,4,5,6,7,90,23,34]
# for i in range(len(list)):
#     if i%2==0:
#         print(list[i])
        
'''Exercise 4 List Insertion'''
# write a Python script that inserts the numbers 10, 11, and 12 at the beginning of list

# list=[23,24,56,7,89,90,24]
# list.insert(0,10)
# list.insert(0,11)
# list.insert(0,12)
# print(list)

" List comprehensions"
" 1.Square Numbers: Create a list of squares of numbers from 1 to 10."

# squares=print([i**2 for i in range(11)])

" 2.Even Numbers; Generate a list of even numbers from 1 to 20."

# numbers=print([i for i in range(21) if i%2==0])

'''3.Words Lengths: Given a list of words, create a list containing the lengths of 
each word'''
# words = ["apple", "banana", "cherry", "date"]
# sen=print([len(i) for i in words])