def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization.
    """
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # If the result is already in the memo dictionary, return it
    if n in memo:
        return memo[n]
    # Otherwise, calculate the result and store it in the memo dictionary
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

# Test the function
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")