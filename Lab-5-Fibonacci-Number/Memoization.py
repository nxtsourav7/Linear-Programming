import numpy as np
import time

# Recursive function with memoization
def fib(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Get the number from the user
# n = int(input("Enter the position of the Fibonacci number you want: "))
n = 1

# Initialize the memoization table with -1
memo = np.full((n + 1,), -1, dtype=np.int64)
# print(memo)

# Measure the time taken to compute the Fibonacci number
start_time = time.time()
result = fib(n, memo)
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the Fibonacci number and the elapsed time
print(f"The {n}th Fibonacci number is: {result}")
print(f"Time taken to compute: {elapsed_time} seconds")
# print(memo)
