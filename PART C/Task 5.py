# Factorial using Iterative and Recursive methods

# This is using Iterative factorial method #
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# This is for using Recursive factorial method #
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Enter any user Input to check #
num = int(input("Enter number: "))

# Output
print("The Iterative factorial is =", factorial_iterative(num))
print("The Recursive factorial is =", factorial_recursive(num))