#Program to find factorial of a number without recursive approach

def factorial(number):
    result=1
    for k in range(number,1,-1):
        result=result*k
    return(result)

x=int(input("Enter the number:"))
y=(factorial(x))
print("Factorial of",x,'is',y)
