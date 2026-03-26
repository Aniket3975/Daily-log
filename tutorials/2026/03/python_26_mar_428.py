# Dynamic Programming Memoization Example

def fibonacci(n, memo={}):
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if result is already in memo dictionary
    if n not in memo:
        # If not, calculate and store it in memo dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return stored or calculated value from memo dictionary
    return memo[n]

# Test the function with different inputs
print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765

def longest_common_subsequence(s1, s2):
    # Initialize a 2D array to store lengths of common subsequences
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Fill the dp array using bottom-up dynamic programming
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct the longest common subsequence from the dp array
    lcs = []
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    # Return the longest common subsequence in reverse order
    return ''.join(reversed(lcs))

# Test the function with different inputs
print(longest_common_subsequence("AGGTAB", "GXTXAYB"))  # Output: AB