def factorial(n):
    if n <0:
        return "factorial does not exist"
    elif n==0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact=fact*i
        return fact
    
a = int(input("enter the number here to calculate factorial:"))
print("Factorial of the number is:", factorial(a))

