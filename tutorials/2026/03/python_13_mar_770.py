# String Hashing in Python
# ===========================

import hashlib

def calculate_hash(string):
    """
    Calculate the hash of a given string using SHA256.
    
    Parameters:
    string (str): The input string for which to calculate the hash.

    Returns:
    str: A hexadecimal representation of the hash value.
    """
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Convert the input string into bytes and update the hash object
    hash_object.update(string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash value
    return hash_object.hexdigest()

def calculate_rabin_karp_hash(string, d):
    """
    Calculate the Rabin-Karp hash of a given string.
    
    Parameters:
    string (str): The input string for which to calculate the hash.
    d (int): The size of the hash table.

    Returns:
    int: A numerical representation of the hash value.
    """
    # Initialize the hash value and the polynomial
    hash_value = 0
    poly_value = 1
    
    # Calculate the hash value using the Rabin-Karp algorithm
    for char in string:
        hash_value = (hash_value + ord(char) * poly_value) % d
        
        # Update the polynomial for the next character
        poly_value = (poly_value * 31) % d
    
    return hash_value

def calculate_jenkins_hash(string):
    """
    Calculate the Jenkins hash of a given string.
    
    Parameters:
    string (str): The input string for which to calculate the hash.

    Returns:
    int: A numerical representation of the hash value.
    """
    # Initialize the hash values for M and B
    m = 0x811C9DC5
    b = 0x01000000
    
    # Calculate the hash value using the Jenkins algorithm
    for char in string:
        # Update the hash values for M and B
        m = (m * 11 + ord(char)) % 2**32
        
        # If we're at a certain position, adjust the hash values
        if b == 0:
            m = (m + ord(string[ord(b) - 1]) * 3) % 2**32
            b = 1
        else:
            b = 0
    
    return m

# Example usage of string hashing functions
if __name__ == "__main__":
    # Test the SHA256 hash function
    print("SHA256 Hash:")
    print(calculate_hash("Hello, World!"))
    
    # Test the Rabin-Karp hash function
    print("\nRabin-Karp Hash:")
    print(calculate_rabin_karp_hash("Hello, World!", 1000007))
    
    # Test the Jenkins hash function
    print("\nJenkins Hash:")
    print(calculate_jenkins_hash("Hello, World!"))