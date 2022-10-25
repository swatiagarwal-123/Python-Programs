#Program to find factorial of a number with recursive approach

def factorial(number):
    #base case
    if number<=1:
        return 1
    else:   #recursive call
        return number   *   factorial(number  -   1)
x=int(input("Enter the number:"))
y=(factorial(x))
print("Factorial of",x,"is",y)
