# String Hashing in Python
#=====================================

def calculate_hash(string):
    """
    Calculate the hash value of a given string.

    :param string: The input string to be hashed.
    :return: A unique integer representing the hash value.
    """
    # Initialize the hash value to 0.
    hash_value = 0
    
    # Use a prime number as the multiplier for efficient hashing.
    prime_multiplier = 31
    
    # Iterate through each character in the input string.
    for char in string:
        # Convert the character to its ASCII value and add it to the hash value.
        # Multiply by the prime multiplier for each iteration.
        hash_value += ord(char) * pow(prime_multiplier, len(string))
    
    # Return the calculated hash value.
    return hash_value

def main():
    """
    Demonstrate string hashing with a sample input string.
    """
    # Define a test string.
    test_string = "Hello World"
    
    # Calculate and print the hash value of the test string.
    print("Hash Value:", calculate_hash(test_string))

if __name__ == "__main__":
    main()