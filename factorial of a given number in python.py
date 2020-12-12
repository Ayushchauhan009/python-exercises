'''def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);
n=5
print("Factorial of the given number is:", factorial(n))'''

#alternate way to find the factorial of a number in python

def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while (n>1):
            fact*=n
            n-=1
        return fact
n=5
print("Factorial of the given number",n, "is:", factorial(n))
