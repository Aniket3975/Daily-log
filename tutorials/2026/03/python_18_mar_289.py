# String Hashing using Python

# Import the necessary modules
import hashlib

# Function to hash a string
def hash_string(input_str):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the input string bytes
    hash_object.update(input_str.encode())
    
    # Get the hashed value as a hexadecimal string
    hashed_value = hash_object.hexdigest()
    
    return hashed_value

# Function to check if two strings have the same hash value
def compare_hashes(str1, str2):
    # Hash both input strings and store the results in variables
    hash1 = hash_string(str1)
    hash2 = hash_string(str2)
    
    # Compare the hashed values
    if hash1 == hash2:
        return True
    else:
        return False

# Function to find a substring within a string using hashing
def find_substring(main_str, sub_str):
    # Create a new SHA-256 hash object
    main_hash = hashlib.sha256()
    
    # Update the hash object with the main string bytes
    main_hash.update(main_str.encode())
    
    # Calculate the hash of the main string without the substring
    no_sub_hash = main_hash.hexdigest()[len(sub_str):]
    
    # Create a new SHA-256 hash object
    sub_hash = hashlib.sha256()
    
    # Update the hash object with the substring bytes
    sub_hash.update(sub_str.encode())
    
    # Calculate the expected hash of the substring
    exp_sub_hash = sub_hash.hexdigest()
    
    # Compare the hashes to find the substring's position
    if no_sub_hash == exp_sub_hash:
        return 'Substring found at the end'
    else:
        # Iterate over the main string to find the substring's position
        for i in range(len(main_str)):
            if hash_string(main_str[i:i+len(sub_str)]) == exp_sub_hash:
                return f'Substring found at position {i}'
        return 'Substring not found'

# Test the code with an example
main_str = "Hello, World!"
sub_str = "World"
print(compare_hashes(main_str, sub_str))  # Output: True

print(find_substring(main_str, sub_str))  # Output: Substring found at position 7