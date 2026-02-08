# String Hashing in Python

def calculate_hash(s):
    # Initialize the hash value to 0
    hash_value = 0
    
    # Use a prime number as a multiplier for better distribution of hash values
    prime_multiplier = 31
    
    # Iterate over each character in the string
    for char in s:
        # Calculate the ASCII value of the current character
        ascii_val = ord(char)
        
        # Update the hash value by multiplying it with the prime number and adding the ASCII value of the current character
        hash_value = (hash_value * prime_multiplier + ascii_val) % 2**32
    
    return hash_value

def main():
    s1 = "Hello, World!"
    s2 = "Python Programming"
    
    # Calculate the hash values for each string
    hash_s1 = calculate_hash(s1)
    hash_s2 = calculate_hash(s2)
    
    print("Hash Value of", s1, ":", hash_s1)
    print("Hash Value of", s2, ":", hash_s2)

if __name__ == "__main__":
    main()

# Run the program to see the hash values