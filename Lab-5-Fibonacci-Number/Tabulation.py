import numpy as np
import time

# Tabulation method to calculate Fibonacci number
def fib_tabulation(n):
    if n <= 1:
        return n

    # Initialize the table to store Fibonacci numbers up to n
    table = np.zeros(n + 1, dtype=np.uint64)
    table[1] = 1

    # Build the table iteratively
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

# Get the number from the user
# n = int(input("Enter the position of the Fibonacci number you want: "))
n = 40

# Measure the time taken to compute the Fibonacci number
start_time = time.time()
result = fib_tabulation(n)
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the Fibonacci number and the elapsed time
print(f"The {n}th Fibonacci number is: {result}")
print(f"Time taken to compute: {elapsed_time} seconds")
