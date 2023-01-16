txt = input()

#your code goes here
words = txt.split(" ")
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)


""""
Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome

Recall the split(' ') method, which returns a list of words of the string.
"""