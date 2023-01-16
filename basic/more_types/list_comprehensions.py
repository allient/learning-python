x = int(input()) 
#your code goes here
result = [i for i in range(0,x) if i % 3 == 0 and i % 5 == 0]
print(result)


""""
List Comprehensions


Write a program to take a number as input, and output a list of all the numbers below that number, that are a multiple of both, 3 and 5.

Sample Input
42

Sample Output
[0, 15, 30]

Use a list comprehension to generate the list of numbers that satisfy the condition.
"""