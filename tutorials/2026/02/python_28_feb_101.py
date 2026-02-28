def compute_prefix_function(pattern):
    # Create a list to store the prefix function values
    prefix = [0] * len(pattern)
    
    # Initialize the prefix function value for the first character
    j = 0
    for i in range(1, len(pattern)):
        # If the current character matches the character at position j
        while j > 0 and pattern[j] != pattern[i]:
            # Move to the previous prefix function value
            j = prefix[j - 1]
        # If the current character matches the character at position j
        if pattern[j] == pattern[i]:
            # Move to the next character
            j += 1
        # Update the prefix function value for the current character
        prefix[i] = j
    
    return prefix

def knuth_morris_pratt_search(text, pattern):
    # Create a list to store the prefix function values
    prefix = compute_prefix_function(pattern)
    
    # Initialize the text and pattern pointers
    i = j = 0
    
    # Search for the pattern in the text
    while i < len(text):
        # If the current character matches the character at position j
        if text[i] == pattern[j]:
            # Move to the next character
            i += 1
            j += 1
        # If the entire pattern has been found
        if j == len(pattern):
            # Return the starting index of the pattern in the text
            return i - j
        # If the current character does not match the character at position j
        elif i < len(text) and text[i] != pattern[j]:
            # If the prefix function value is not zero, move to the previous character
            if j != 0:
                j = prefix[j - 1]
            # If the prefix function value is zero, move to the next character
            else:
                i += 1
    
    # If the pattern is not found in the text
    return -1

# Test the implementation
text = "ABABDABACDABABCABAB"
pattern = "ABAB"
print(knuth_morris_pratt_search(text, pattern))  # Output: 0