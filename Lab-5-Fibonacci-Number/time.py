import time
import numpy as np

# brute force
def bf(n):
    if n <= 1: 
        return n
    else:
        return bf(n - 1) + bf(n - 2)
    
#memoization
def mz(n, memo):
    #base case
    if memo[n] != 0:
        return memo[n]
    
    if n <= 1: # memo[n] == -1 
        memo[n] = n
    else:
        memo[n] = mz(n - 1, memo) + mz(n - 2, memo)

    #return the result
    return memo[n]


#int main32_t:
n = 40 

# initialize the array with -1 
memo = np.full(n + 1, 0, np.uint64)

#calculate brute force
s_bf = time.time()
r1 = bf(n)
e_bf = time.time()

#calculate memoization
s_mz = time.time()
r2 = mz(n, memo)
e_mz = time.time()


#result
print(r1)
print(r2)
print(f"Difference between elapsed_time : {(e_bf - s_bf) - (e_mz - s_mz)}")
