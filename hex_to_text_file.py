def hex_to_text(hex_string):
    """Convert hexadecimal string to human-readable text."""
    try:
        # Split the hexadecimal string into pairs of two characters
        hex_pairs = hex_string.split()
        # Convert each pair of hexadecimal characters to its corresponding ASCII character
        text = ''.join(chr(int(pair, 16)) for pair in hex_pairs)
        return text
    except ValueError:
        print("Invalid hexadecimal input.")
        return None

def main():
    hex_input = input("Enter hexadecimal string (space-separated): ")
    decoded_text = hex_to_text(hex_input)
    if decoded_text:
        print("Decoded text:", decoded_text)

if __name__ == "__main__":
    main()
