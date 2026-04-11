def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    m = len(pattern)
    pi = [0] * m
    
    # Initialize the length of the longest proper prefix which is also a suffix
    j = 0
    
    # Traverse through the pattern string from the second character to the last
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        
        # Update the prefix function value for the current position
        pi[i] = j
    
    return pi

def knuth_morris_pratt_search(text, pattern):
    # Compute the prefix function for the pattern
    pi = compute_prefix_function(pattern)
    
    # Initialize the index for the text and pattern
    i = 0
    j = 0
    
    while i < len(text):
        if j == 0 or text[i] == pattern[j]:
            i += 1
            j += 1
            
        if j == len(pattern):
            return i - j
        
        elif text[i] != pattern[j]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
    
    # If the pattern is not found in the text
    return -1

# Example usage
text = "ABCDABCA"
pattern = "ABC"

result = knuth_morris_pratt_search(text, pattern)

if result != -1:
    print(f"Pattern '{pattern}' found at index {result} in the text '{text}'.")
else:
    print(f"Pattern '{pattern}' not found in the text '{text}'.")