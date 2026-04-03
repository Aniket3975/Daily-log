# String Hashing using Python

# Import the required module for prime numbers
import random

class Djb2Hasher:
    def __init__(self):
        # Initialize the prime number and modulus values
        self.prime = 131
        self.modulus = 2**32

    def hash(self, s):
        # Set the initial hash value to 5381 (a common starting point for djb2)
        hash_value = 5381
        
        # Iterate over each character in the string
        for char in s:
            # Update the hash value using a combination of multiplication and addition
            # The multiplication by prime helps to distribute values evenly across the range
            # The addition of the ASCII value of the current character ensures uniqueness
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
            
            # Apply modulo operation to keep the hash value within the range
            hash_value %= self.modulus
        
        # Return the final hash value as an integer
        return hash_value

    def reverse(self, s):
        # Reverse the string using slicing
        reversed_s = s[::-1]
        
        # Calculate the hash of the reversed string
        return self.hash(reversed_s)

def main():
    # Create a Djb2Hasher instance
    hasher = Djb2Hasher()
    
    # Test with a simple string
    input_str = "Hello World"
    print(f"Original String: {input_str}")
    hash_value = hasher.hash(input_str)
    print(f"Hash Value: {hash_value}")
    reversed_hash_value = hasher.reverse(input_str)
    print(f"Reversed Hash Value: {reversed_hash_value}")

if __name__ == "__main__":
    main()