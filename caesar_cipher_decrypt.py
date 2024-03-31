def caesar_decrypt(ciphertext, shift=None):
    """Decrypt Caesar cipher text."""
    decrypted_text = ''
    if shift is None:  # Brute force all possible shifts
        for shift in range(26):
            decrypted_text += decrypt_with_shift(ciphertext, shift)
            decrypted_text += "\n"
    else:  # Decrypt with the provided shift
        decrypted_text = decrypt_with_shift(ciphertext, shift)
    return decrypted_text

def decrypt_with_shift(ciphertext, shift):
    """Decrypt Caesar cipher text with a specific shift."""
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            shifted_ascii = ord(char) - shift
            if char.islower():
                if shifted_ascii < ord('a'):
                    shifted_ascii += 26
            elif char.isupper():
                if shifted_ascii < ord('A'):
                    shifted_ascii += 26
            decrypted_text += chr(shifted_ascii)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    ciphertext = input("Enter Caesar cipher text: ")
    choice = input("Enter '1' to enter shift key" "\n" "      '2' to bruteforce: ")
    
    if choice == '1':
        shift = int(input("Enter the shift value (0-25): "))
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print("Decrypted text:", decrypted_text)
    elif choice == '2':
        decrypted_text = caesar_decrypt(ciphertext)
        print("All possible decryptions:")
        print(decrypted_text)

if __name__ == "__main__":
    main()
