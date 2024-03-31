# Caesar Cipher Decryption and Hexadecimal to Text Conversion

This repository contains Python scripts to decrypt Caesar cipher text and convert hexadecimal strings to human-readable text.

## Caesar Cipher Decryption

### Description
The `caesar_cipher_decrypt.py` script allows you to decrypt Caesar cipher text. You can either provide the shift key or let the script brute force all possible shifts to find the decrypted text. The decryption considers shifts from left to right and from right to left.

### Usage
1. Run the script `caesar_cipher_decrypt.py`.
2. Input the Caesar cipher text when prompted.
3. Choose one of the following options:
   - Enter `1` to enter a specific shift key.
   - Enter `2` to brute force all possible shifts.
4. If you choose to enter a specific shift key:
   - Enter the shift value when prompted (0-25).
5. If you choose to brute force:
   - The script will output all possible decryptions, each corresponding to a different shift value.

## Hexadecimal to Text Conversion

### Description
The `hex_to_text_file.py` script allows you to convert hexadecimal strings to human-readable text.

### Usage
1. Run the script `hex_to_text_file.py`.
2. Enter the hexadecimal string when prompted (space-separated).
3. The script will output the decoded human-readable text.

