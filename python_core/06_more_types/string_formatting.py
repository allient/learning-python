name:str = input()
age:int = int(input())

#your code goes here

txt:str = "{name} is {age} years old".format(name = name, age = age)


print(txt)


""""
String Formatting


The .format() method provides an easy way to format strings.
Take as input a name and an age, and generate the output "name is age years old".

Sample Input
James
42

Sample Output
James is 42 years old

Recall, you can use braces to embed variable values into strings.
"""