class Number:
    def __init__(self, num: int):
        self.value = num
        
    #your code goes here
    @property
    def isEven(self):
        return self.value % 2 == 0 
   
 
x: Number = Number(int(input()))
print(x.isEven)

"""
Properties


Complete the provided code by creating an isEven property, which returns True if the value is even, and False if the value is odd.
class Number:
    def __init__(self, num):
        self.value = num

x = Number(int(input()))
print(x.isEven) 

Use the modulo operator % to check if the value is even or odd. The value is even if the remainder of dividing it by 2 is 0."""