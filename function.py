# Q1:- Calculate the sum of all numbers from 1 to a given number

# Q2:- Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# Q3:-  Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop/ for loop.
# For example, the number is 75869, so the output should be 5.

# def sum(a):
#     sum=0
#     for i in range(a+1):
#         sum=sum+i
#     print("Sum : "+str(sum))

# sum(5)

# def display(numbers):
#     for x in numbers:
#         if x > 150:
#             continue
#         elif x>500:
#             break
#         elif x%5==0:
#             print(x)
# numbers=[5,10,155,60,555,350,450]
# display(numbers)


# def countNo(number):
#     count=0
#     while(number !=0):
#         number=number//10
#         count=count+1
#     print(count)
# countNo(169872)

# Q4:- Print list in reverse order using a loop
# Given:
# list1 = [10, 20, 30, 40, 50]
# def reverseOrder(list):
#     size=len(list)
#     for x in range(size):
#         print(list[size-x-1])
        
# list1 = [10, 20, 30, 40, 50]
# reverseOrder(list1)

# Use a loop to display elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: list index always starts at 0
# def display(elements):
#     size=len(elements)
#     for x in range(size):
#         if(x%2!=0):
#             print(elements[x])

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# display(my_list)

list1 = []
n=5
print("Enter elements: ")
for i in range(0, n):
    ele = int(input())
  
    list1.append(ele)

print(list1)