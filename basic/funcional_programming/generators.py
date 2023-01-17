txt = input()

def words():
    #your code goes here
    for word in txt.split(" "):
        yield word

print(list(words()))


""""
Generators


Given a string as input, create a generator function that splits the string into separate words and outputs the resulting list.

Sample Input
This is some text

Sample Output
['This', 'is', 'some', 'text']

You can use the split() function to split the input string.
"""