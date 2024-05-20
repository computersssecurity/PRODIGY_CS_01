def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    try:
        plaintext = input("Enter your message: ")
        shift = int(input("Enter the shift value (positive integer): "))

        encrypted_message = caesar_encrypt(plaintext, shift)
        print("Encrypted message:", encrypted_message)

    except ValueError:
        print("Invalid input. Please enter a valid shift value (positive integer).")

if __name__ == "__main__":
    main()
