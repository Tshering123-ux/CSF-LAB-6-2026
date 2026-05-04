# This is a Fibonacci Comparison between: Iterative vs Recursive #

# This is for Iterative Fibonacci sequence #
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Next, This is for Recursive Fibonacci sequence with call counter #
call_count = 0

def fib_recursive(n):
    global call_count
    call_count += 1
    
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Enter any user Input #
num = int(input("Enter number: "))

# This is the Iterative result #
iter_result = fib_iterative(num)

# This is the Recursive result #
call_count = 0
rec_result = fib_recursive(num)

# Output
print("The Iterative Fibonacci is=", iter_result)
print("The Recursive Fibonacci is =", rec_result)
print("The Number of recursive calls is =", call_count)

# Efficiency comparison
print("\nEfficiency Comparison:")
print("Overall, Iterative method is faster and uses less memory.")
print("While Recursive method is slower due to repeated calculations.")