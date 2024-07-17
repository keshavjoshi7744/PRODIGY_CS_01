# Caesar Cipher Program

def caesar_cipher(text, shift, operation):
    result = []

    # Adjust the shift for decryption
    if operation == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Shift character within the bounds of alphabet
            shift_base = 65 if char.isupper() else 97
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(new_char)
        else:
            # Non-alphabet characters remain unchanged
            result.append(char)

    return ''.join(result)

def main():
    print("Welcome to the Caesar Cipher Program made by Keshav Joshi!")
    operation = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt'): ").strip().lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation! Please enter 'encrypt' or 'decrypt'.")
        return

    text = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value (an integer): ").strip())

    result = caesar_cipher(text, shift, operation)
    print(f"The {operation}ed message is: {result}")

if __name__ == "__main__":
    main()
