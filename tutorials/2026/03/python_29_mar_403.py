# knuth_morris_pratt.py
def compute_prefix_function(pattern):
    # Initialize the prefix function with zeros
    m = len(pattern)
    pi = [0] * (m + 1)

    # Iterate over the pattern to fill the prefix function
    for i in range(1, m):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    return pi


def kmp_search(text, pattern):
    # Compute the prefix function for the pattern
    pi = compute_prefix_function(pattern)

    # Initialize variables to track search progress
    m = len(pattern)
    n = len(text)
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            # If we've matched the entire pattern, return its index
            if j == m:
                return i - m
        elif j > 0:
            j = pi[j - 1]
        else:
            i += 1

    # Pattern not found in text
    return None


# Example usage
if __name__ == "__main__":
    pattern = "abab"
    text = "abababab"

    index = kmp_search(text, pattern)

    if index is not None:
        print(f"Pattern '{pattern}' found at position {index} in the text.")
    else:
        print("Pattern not found in the text.")