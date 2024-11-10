# Caesar Cipher Encryption and Decryption

def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = 65 if char.isupper() else 97  # ASCII value for 'A' (65) and 'a' (97)
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shift = 65 if char.isupper() else 97  # ASCII value for 'A' (65) and 'a' (97)
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Non-alphabetic characters are not changed
    return decrypted_text

# Example usage:
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key (number of shifts): "))
    
    encrypted = encrypt(plaintext, key)
    print(f"Encrypted text: {encrypted}")
    
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted text: {decrypted}")
