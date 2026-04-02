def fib(n, memo={}):
    # Base case for recursion 
    if n <=0:
        return 0
    elif n ==1:
        return 1
    
    # If the value is already in memo, then we can use it and avoid redundant computation.
    if n not in memo:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
    
    # Return the computed value
    return memo[n]

# Test the function with a few values
for i in range(10):
    print(f'Fibonacci number for {i} is: ',fib(i))

def fibonacci(n, memo={}):
    # Base case for recursion 
    if n <=0:
        return 0
    elif n ==1:
        return 1
    
    # If the value is already in memo, then we can use it and avoid redundant computation.
    if n not in memo:
        memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
    
    # Return the computed value
    return memo[n]

def fibonacci_iterative(n):
    # Create a list to hold values of fibonaccis
    fib_sequence = [0, 1]
    
    # Compute Fibonacci numbers iteratively and store them in the sequence.
    for i in range(2,n+1):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)

    # Return the nth fibonacci number
    return fib_sequence[n]

# Test the functions with a few values
print('Fibonacci Number using Dynamic Programming (Memoization): ',fib(10))
print('Fibonacci Number using Iterative Approach: ',fibonacci_iterative(10))

def fibonacci_recursive(n):
    # Base case for recursion 
    if n <=0:
        return 0
    elif n ==1:
        return 1
    
    # Recursive call to compute the nth Fibonacci number.
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function with a few values
print('Fibonacci Number using Dynamic Programming (Memoization): ',fib(10))
print('Fibonacci Number using Recursive Approach: ',fibonacci_recursive(10))