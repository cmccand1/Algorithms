# A recursive function that returns the factorial of a number
user_input = input("Enter a number: ")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print factorial(user_input)
