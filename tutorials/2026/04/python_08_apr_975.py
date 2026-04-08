def fib(n, memo = {}):
    # Base cases for Fibonacci sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Check if result is already in memo dictionary
    if n not in memo:
        # If not, calculate and store the result in memo dictionary
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    
    # Return the calculated result from memo dictionary
    return memo[n]

# Test the function with some examples
print("Fibonacci numbers:")
for i in range(10):
    print(f"i: {i}, fib(i): {fib(i)}")