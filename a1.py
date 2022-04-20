# a. Program to add two numbers
def sum(a, b):
    return a + b


# b. Maximum of two numbers
def max(a, b):
    if a > b:
        return a
    else:
        return b


# c. Program for factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# d. Program to check Armstrong number
def armstrong(n):
    sum = 0
    for i in str(n):
        sum += int(i)**3
    if sum == n:
        return True
    else:
        return False


# Examples
# a
print(sum(1, 2))
# b
print(max(1, 2))
# c
print(factorial(5))
# d
print(armstrong(153))
